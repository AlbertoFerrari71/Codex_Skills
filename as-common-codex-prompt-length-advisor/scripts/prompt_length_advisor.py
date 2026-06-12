#!/usr/bin/env python3
"""Analyze Codex prompt length, integrity, noise, and runtime context risk."""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any


STATUS_THRESHOLDS = (
    (30_000, "OK"),
    (45_000, "OK_GRANDE"),
    (70_000, "REVIEW"),
    (100_000, "SPLIT_CONSIGLIATO"),
)

RISK_IT = {"low": "basso", "medium": "medio", "high": "alto"}
PUBLISH_IT = {"pass": "PASS", "warning": "WARNING", "fail": "FAIL"}


def length_status(characters: int) -> str:
    for limit, status in STATUS_THRESHOLDS:
        if characters <= limit:
            return status
    return "SPLIT_FORTE"


def estimate_tokens(characters: int, words: int) -> int:
    return max(math.ceil(characters / 4), math.ceil(words * 1.3))


def count_words(text: str) -> int:
    return len(re.findall(r"\b\w+\b", text, flags=re.UNICODE))


def count_lines(text: str) -> int:
    if not text:
        return 0
    return len(text.splitlines())


def markdown_headings(text: str) -> list[str]:
    headings: list[str] = []
    for line in text.splitlines():
        match = re.match(r"^\s{0,3}#{1,6}\s+(.+?)\s*$", line)
        if match:
            headings.append(match.group(1).strip())
    return headings


def code_fence_count(text: str) -> int:
    return sum(1 for line in text.splitlines() if re.match(r"^\s*(```|~~~)", line))


def final_sentinel_present(text: str) -> bool:
    return bool(re.search(r"\bEND_OF_PROMPT_[A-Za-z0-9_-]+\b", text))


def final_rules_present(text: str) -> bool:
    return "REGOLE FINALI" in text.upper()


def integrity_check_present(text: str) -> bool:
    return "CONTROLLO INTEGRITÀ PROMPT" in text.upper()


def deterministic_report_present(text: str) -> bool:
    lowered = text.lower()
    return "report finale" in lowered and (
        "formato report" in lowered
        or "formato obbligatorio" in lowered
        or "deterministico" in lowered
        or "stato finale" in lowered
    )


def publish_ban_present(text: str) -> bool:
    lowered = text.lower()
    targets = ("commit", "push", "pr", "pull request", "merge", "deploy")
    bans = 0
    for target in targets:
        if re.search(rf"\bnon\s+(?:fare|eseguire|aprire|creare|pubblicare)?\s*{re.escape(target)}\b", lowered):
            bans += 1
    return bans >= 3


def _strip_negative_publish_phrases(lowered: str) -> str:
    patterns = (
        r"\bnon\s+(?:fare|eseguire|aprire|creare|pubblicare)?\s*(?:commit|push|pr|pull request|merge|deploy)\b",
        r"\b(?:commit|push|pr|pull request|merge|deploy)\s*:\s*non\s+eseguit[oa]\b",
        r"\bnon\s+(?:committare|pushare|mergiare|deployare)\b",
    )
    cleaned = lowered
    for pattern in patterns:
        cleaned = re.sub(pattern, " ", cleaned)
    return cleaned


def detect_publish_safety(text: str) -> tuple[str, list[str]]:
    lowered = text.lower()
    cleaned = _strip_negative_publish_phrases(lowered)
    findings: list[str] = []

    positive_patterns = (
        r"\bfai\s+(?:il\s+)?commit\b",
        r"\bfai\s+commit\s+e\s+push\b",
        r"\besegui\s+(?:il\s+)?commit\b",
        r"\bpusha\b",
        r"\bpushare\b",
        r"\bapri\s+(?:una\s+)?pr\b",
        r"\bapri\s+(?:una\s+)?pull request\b",
        r"\bcrea\s+(?:una\s+)?pr\b",
        r"\bmergia\b",
        r"\bpubblica\b",
        r"\bdeploya\b",
        r"\bfai\s+(?:il\s+)?deploy\b",
    )
    for pattern in positive_patterns:
        if re.search(pattern, cleaned):
            findings.append("Richiesta publish positiva o ambigua rilevata.")
            break

    has_gate = any(
        phrase in lowered
        for phrase in (
            "autorizzazione esplicita",
            "solo se autorizzato",
            "gate",
            "previa autorizzazione",
            "se autorizzato",
            "publish safety",
        )
    )
    if findings and has_gate:
        return "warning", findings
    if findings:
        findings.append("Manca una sezione di autorizzazione o gate esplicito.")
        return "fail", findings
    return "pass", []


def detect_noise(text: str, headings: list[str]) -> tuple[str, list[str]]:
    findings: list[str] = []
    lowered = text.lower()

    heading_counts = Counter(heading.strip().lower() for heading in headings)
    repeated_headings = [heading for heading, count in heading_counts.items() if count > 1]
    if repeated_headings:
        findings.append(f"Heading ripetuti: {len(repeated_headings)}.")

    paragraphs = [
        re.sub(r"\s+", " ", paragraph.strip().lower())
        for paragraph in re.split(r"\n\s*\n", text)
        if len(paragraph.strip()) >= 100
    ]
    repeated_paragraphs = [item for item, count in Counter(paragraphs).items() if count > 1]
    if repeated_paragraphs:
        findings.append(f"Paragrafi duplicati: {len(repeated_paragraphs)}.")

    diff_signals = len(re.findall(r"(?m)^(diff --git|@@ |\+\+\+ |--- a/)", text))
    if diff_signals:
        findings.append("Possibile diff incollato nel prompt.")

    traceback_signals = len(re.findall(r"Traceback \(most recent call last\)|^\s*File \".+\", line \d+", text))
    if traceback_signals:
        findings.append("Possibile traceback esteso nel prompt.")

    log_signals = sum(
        lowered.count(term)
        for term in (
            "pytest",
            "failed",
            "error collecting",
            "====",
            "stdout",
            "stderr",
            "exit code",
        )
    )
    if log_signals >= 8:
        findings.append("Possibili log/test output estesi.")

    if diff_signals >= 5 or traceback_signals >= 3 or log_signals >= 12:
        return "high", findings
    if findings:
        return "medium", findings
    return "low", []


def detect_runtime_context_growth(text: str) -> tuple[str, list[str]]:
    lowered = text.lower()
    findings: list[str] = []
    patterns = (
        (r"leggi\s+tutto\s+il\s+repository", "Richiede di leggere tutto il repository."),
        (r"leggere\s+tutto\s+il\s+repository", "Richiede di leggere tutto il repository."),
        (r"leggi\s+intere\s+directory|aprire\s+intere\s+directory", "Richiede lettura ampia di directory."),
        (r"stampa\s+tutto\s+il\s+diff|stampare\s+output\s+completi", "Richiede output completo invece di sintesi."),
        (r"log\s+complet[oi]|output\s+complet[oi]", "Richiede log o output completi."),
        (r"scansion[ei]\s+indiscriminat[ae]", "Richiede scansioni indiscriminate."),
        (r"report\s+troppo\s+proliss[oi]|report\s+molto\s+proliss[oi]", "Richiede report prolissi."),
        (r"accumulare\s+log\s+completi", "Richiede accumulo di log completi."),
        (r"file\s+enormi", "Menziona apertura di file enormi."),
    )
    for pattern, message in patterns:
        if re.search(pattern, lowered):
            findings.append(message)

    if "git diff" in lowered and "git --no-pager diff" not in lowered:
        findings.append("Menziona git diff senza git --no-pager.")

    if len(findings) >= 2:
        return "high", findings
    if findings:
        return "medium", findings
    return "low", []


def detect_integrity_findings(text: str, code_fences_pass: bool) -> list[str]:
    findings: list[str] = []
    stripped_lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not final_sentinel_present(text):
        findings.append("Sentinella finale END_OF_PROMPT_XXXX assente.")
    elif stripped_lines and not re.fullmatch(r"END_OF_PROMPT_[A-Za-z0-9_-]+", stripped_lines[-1]):
        findings.append("Sentinella END_OF_PROMPT presente ma non come ultima riga non vuota.")
    if not final_rules_present(text):
        findings.append("Sezione REGOLE FINALI assente.")
    if not integrity_check_present(text):
        findings.append("Sezione CONTROLLO INTEGRITÀ PROMPT assente.")
    if not code_fences_pass:
        findings.append("Code fence Markdown non chiusi.")
    if re.search(r"(?m)^\s*\d+\.\s*$", text):
        findings.append("Elenco numerato apparentemente interrotto.")
    if re.search(r"[A-Za-z]:\\(?:[^\s\\]+\\)*\s*$", text):
        findings.append("Possibile path Windows spezzato a fine riga.")
    return findings


def initial_prompt_risk(status: str, required_sections_pass: bool, code_fences_pass: bool, noise_risk: str) -> str:
    if not required_sections_pass or not code_fences_pass:
        return "high"
    if status in {"SPLIT_CONSIGLIATO", "SPLIT_FORTE"} or noise_risk == "high":
        return "high"
    if status in {"OK_GRANDE", "REVIEW"} or noise_risk == "medium":
        return "medium"
    return "low"


def suggestion_for(status: str, noise_risk: str, runtime_risk: str, required_sections_pass: bool) -> str:
    if not required_sections_pass:
        return "verificare integrita"
    if status == "OK" and noise_risk == "low" and runtime_risk == "low":
        return "mantenere prompt unico"
    if status in {"OK", "OK_GRANDE", "REVIEW"}:
        return "alleggerire" if noise_risk != "low" or runtime_risk != "low" else "mantenere prompt unico"
    return "dividere"


def recommendation_for(suggestion: str, status: str) -> str:
    if suggestion == "verificare integrita":
        return "Verifica integrita' e completezza prima di usare il prompt."
    if suggestion == "mantenere prompt unico":
        return "Usa prompt unico."
    if suggestion == "alleggerire":
        return "Usa prompt unico ma alleggerisci queste parti."
    if status == "SPLIT_CONSIGLIATO":
        return "Dividi solo le sezioni storiche in file riferimento."
    return "Dividi in prompt index + task file."


def analyze_prompt(text: str) -> dict[str, Any]:
    characters = len(text)
    words = count_words(text)
    headings = markdown_headings(text)
    fence_count = code_fence_count(text)
    code_fences_pass = fence_count % 2 == 0
    status = length_status(characters)
    sentinel = final_sentinel_present(text)
    rules = final_rules_present(text)
    integrity = integrity_check_present(text)
    required_sections_pass = sentinel and rules and integrity
    noise_risk, noise_findings = detect_noise(text, headings)
    runtime_risk, runtime_findings = detect_runtime_context_growth(text)
    publish_safety, publish_findings = detect_publish_safety(text)
    integrity_findings = detect_integrity_findings(text, code_fences_pass)
    prompt_risk = initial_prompt_risk(status, required_sections_pass, code_fences_pass, noise_risk)
    suggestion = suggestion_for(status, noise_risk, runtime_risk, required_sections_pass)
    recommendation = recommendation_for(suggestion, status)

    findings = integrity_findings + noise_findings + runtime_findings + publish_findings
    if deterministic_report_present(text):
        findings.append("Report finale deterministico presente.")
    if publish_ban_present(text):
        findings.append("Divieti publish espliciti presenti.")

    return {
        "status": status,
        "characters": characters,
        "lines": count_lines(text),
        "words": words,
        "estimated_tokens": estimate_tokens(characters, words),
        "markdown_headings": len(headings),
        "code_blocks": fence_count // 2,
        "code_fences": fence_count,
        "code_fences_pass": code_fences_pass,
        "final_sentinel_present": sentinel,
        "final_rules_present": rules,
        "integrity_check_present": integrity,
        "deterministic_final_report_present": deterministic_report_present(text),
        "publish_ban_present": publish_ban_present(text),
        "required_sections_pass": required_sections_pass,
        "initial_prompt_risk": prompt_risk,
        "runtime_context_growth_risk": runtime_risk,
        "noise_risk": noise_risk,
        "publish_safety": publish_safety,
        "suggestion": suggestion,
        "recommendation": recommendation,
        "findings": findings,
    }


def format_text_report(result: dict[str, Any]) -> str:
    findings = result["findings"] or ["Nessun dettaglio critico rilevato."]
    lines = [
        f"PROMPT_LENGTH_STATUS: {result['status']}",
        "",
        f"Caratteri: {result['characters']}",
        f"Righe: {result['lines']}",
        f"Parole: {result['words']}",
        f"Stima token approssimata: {result['estimated_tokens']}",
        f"Rischio prompt iniziale: {RISK_IT[result['initial_prompt_risk']]}",
        f"Rischio crescita durante run: {RISK_IT[result['runtime_context_growth_risk']]}",
        f"Sentinella finale: {'presente' if result['final_sentinel_present'] else 'assente'}",
        f"REGOLE FINALI: {'presente' if result['final_rules_present'] else 'assente'}",
        f"CONTROLLO INTEGRITÀ PROMPT: {'presente' if result['integrity_check_present'] else 'assente'}",
        f"Sezioni obbligatorie: {'PASS' if result['required_sections_pass'] else 'FAIL'}",
        f"Code fence: {'PASS' if result['code_fences_pass'] else 'FAIL'}",
        f"Rumore/duplicazioni: {RISK_IT[result['noise_risk']]}",
        f"Publish safety: {PUBLISH_IT[result['publish_safety']]}",
        f"Suggerimento: {result['suggestion']}",
        "",
        "Dettagli:",
    ]
    lines.extend(f"- {finding}" for finding in findings)
    lines.extend(["", "Raccomandazione:", result["recommendation"]])
    return "\n".join(lines)


def read_input(path: str | None) -> str:
    if path is None:
        return sys.stdin.read()
    prompt_path = Path(path)
    try:
        return prompt_path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"File prompt non trovato: {prompt_path}") from exc
    except OSError as exc:
        raise OSError(f"Impossibile leggere il file prompt {prompt_path}: {exc}") from exc


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Analyze Codex prompt length and integrity.")
    parser.add_argument("prompt_file", nargs="?", help="Prompt file to analyze. Reads stdin when omitted.")
    parser.add_argument("--json", action="store_true", help="Emit deterministic JSON output.")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        text = read_input(args.prompt_file)
    except (FileNotFoundError, OSError) as exc:
        print(str(exc), file=sys.stderr)
        return 2

    result = analyze_prompt(text)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(format_text_report(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
