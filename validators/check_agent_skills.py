#!/usr/bin/env python3
"""Validate Alberto Ferrari's local Codex skill catalog."""

from __future__ import annotations

import argparse
import fnmatch
import re
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Iterable


TECHNICAL_DIRS = {".git", "_archive", "docs", "templates", "validators", "__pycache__"}
SKILL_PREFIXES = ("as-common-", "as-")

BACKUP_PATTERNS = ("*.bak.md", "*.backup.md", "*~", "*.tmp")
SENSITIVE_FILE_PATTERNS = (
    ".env",
    "*.pem",
    "*.key",
    "*.pfx",
    "secrets*",
    "token*",
    "credentials*",
)
SUSPICIOUS_TERMS = (
    "password",
    "token",
    "api_key",
    "secret",
    "client_secret",
    "private_key",
    "pwd=",
    "uid=",
    "connection string",
)
OPERATIONAL_HEADING_TERMS = (
    "scopo",
    "quando usarla",
    "quando non usarla",
    "procedura",
    "metodo",
    "workflow",
    "regole",
    "output",
    "purpose",
    "use this skill",
    "core rules",
    "required",
    "response pattern",
    "default safety",
    "final report",
)

NAMING_ERROR_CODES = {
    "naming_lowercase",
    "naming_kebab_case",
    "naming_underscore",
    "naming_spaces",
    "naming_ascii",
}
SEVERE_ERROR_CODES = {
    "missing_skill_md",
    "missing_frontmatter",
    "missing_name",
    "missing_description",
    "name_mismatch",
}
SAFETY_WARNING_CODES = {"backup_file", "sensitive_file", "suspicious_terms"}


@dataclass
class Issue:
    level: str
    skill: str
    code: str
    message: str
    path: str = ""


@dataclass
class SkillReport:
    name: str
    path: Path
    declared_name: str = ""
    description: str = ""
    frontmatter_valid: bool = False
    has_references: bool = False
    has_examples: bool = False
    has_operational_body: bool = False
    backup_files: list[str] = field(default_factory=list)
    sensitive_files: list[str] = field(default_factory=list)
    errors: list[Issue] = field(default_factory=list)
    warnings: list[Issue] = field(default_factory=list)
    score: int = 0
    grade: str = "E"
    recommended_action: str = ""


def is_ascii(value: str) -> bool:
    try:
        value.encode("ascii")
    except UnicodeEncodeError:
        return False
    return True


def is_kebab_case(value: str) -> bool:
    return bool(re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", value))


def is_skill_dir(path: Path) -> bool:
    if not path.is_dir():
        return False
    name = path.name
    if name in TECHNICAL_DIRS:
        return False
    return any(name.startswith(prefix) for prefix in SKILL_PREFIXES)


def find_skill_dirs(root: Path) -> list[Path]:
    return sorted(path for path in root.iterdir() if is_skill_dir(path))


def read_text_file(path: Path) -> str | None:
    try:
        data = path.read_bytes()
    except OSError:
        return None
    if b"\x00" in data:
        return None
    for encoding in ("utf-8-sig", "utf-8", "cp1252"):
        try:
            return data.decode(encoding)
        except UnicodeDecodeError:
            continue
    return None


def relative_display(root: Path, path: Path) -> str:
    try:
        return path.relative_to(root).as_posix()
    except ValueError:
        return path.as_posix()


def unquote_yaml_scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


def parse_frontmatter(text: str) -> tuple[bool, dict[str, str], str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return False, {}, text

    closing_index = None
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            closing_index = index
            break
    if closing_index is None:
        return False, {}, text

    frontmatter: dict[str, str] = {}
    for raw_line in lines[1:closing_index]:
        line = raw_line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, raw_value = line.split(":", 1)
        key = key.strip()
        if key:
            frontmatter[key] = unquote_yaml_scalar(raw_value)

    body = "\n".join(lines[closing_index + 1 :])
    return True, frontmatter, body


def has_operational_section(body: str, skill_name: str) -> bool:
    if len(body.strip()) < 40:
        return False

    for raw_line in body.splitlines():
        match = re.match(r"^\s{0,3}#{1,6}\s+(.+?)\s*$", raw_line)
        if not match:
            continue
        heading = match.group(1).strip().lower()
        if heading == skill_name.lower():
            continue
        if any(term in heading for term in OPERATIONAL_HEADING_TERMS):
            return True
    return False


def add_error(report: SkillReport, code: str, message: str, path: str = "") -> None:
    report.errors.append(Issue("ERROR", report.name, code, message, path))


def add_warning(report: SkillReport, code: str, message: str, path: str = "") -> None:
    report.warnings.append(Issue("WARNING", report.name, code, message, path))


def matches_any_pattern(name: str, patterns: Iterable[str]) -> bool:
    lowered = name.lower()
    return any(fnmatch.fnmatch(lowered, pattern.lower()) for pattern in patterns)


def iter_skill_files(skill_dir: Path) -> Iterable[Path]:
    for path in skill_dir.rglob("*"):
        if path.is_dir():
            continue
        if "__pycache__" in path.parts:
            continue
        yield path


def scan_files(report: SkillReport, root: Path) -> None:
    for path in iter_skill_files(report.path):
        rel_path = relative_display(root, path)
        file_name = path.name

        if matches_any_pattern(file_name, BACKUP_PATTERNS):
            report.backup_files.append(rel_path)
            add_warning(report, "backup_file", f"File backup/temp rilevato: {rel_path}", rel_path)

        if matches_any_pattern(file_name, SENSITIVE_FILE_PATTERNS):
            report.sensitive_files.append(rel_path)
            add_warning(
                report,
                "sensitive_file",
                f"File potenzialmente sensibile rilevato: {rel_path}",
                rel_path,
            )

        text = read_text_file(path)
        if text is None:
            continue
        lowered = text.lower()
        found_terms = [term for term in SUSPICIOUS_TERMS if term.lower() in lowered]
        if found_terms:
            term_list = ", ".join(found_terms)
            add_warning(
                report,
                "suspicious_terms",
                f"Parole sospette in {rel_path}: {term_list}",
                rel_path,
            )


def validate_skill(skill_dir: Path, root: Path) -> SkillReport:
    report = SkillReport(name=skill_dir.name, path=skill_dir)
    name = skill_dir.name

    if name != name.lower():
        add_error(report, "naming_lowercase", "Nome cartella non completamente minuscolo.")
    if "_" in name:
        add_error(report, "naming_underscore", "Nome cartella contiene underscore.")
    if " " in name:
        add_error(report, "naming_spaces", "Nome cartella contiene spazi.")
    if not is_ascii(name):
        add_error(report, "naming_ascii", "Nome cartella contiene accenti o caratteri non ASCII.")
    if not is_kebab_case(name):
        add_error(report, "naming_kebab_case", "Nome cartella non kebab-case.")

    report.has_references = (skill_dir / "references").is_dir()
    report.has_examples = (skill_dir / "examples").is_dir()

    skill_md = skill_dir / "SKILL.md"
    if not skill_md.is_file():
        add_error(report, "missing_skill_md", "SKILL.md mancante.")
        scan_files(report, root)
        calculate_score(report)
        return report

    text = read_text_file(skill_md)
    if text is None:
        add_error(report, "missing_skill_md", "SKILL.md non leggibile come file testuale.")
        scan_files(report, root)
        calculate_score(report)
        return report

    frontmatter_valid, frontmatter, body = parse_frontmatter(text)
    report.frontmatter_valid = frontmatter_valid
    if not frontmatter_valid:
        add_error(report, "missing_frontmatter", "Frontmatter YAML delimitato da --- mancante o incompleto.")
    else:
        report.declared_name = frontmatter.get("name", "").strip()
        report.description = frontmatter.get("description", "").strip()

        if "name" not in frontmatter or not report.declared_name:
            add_error(report, "missing_name", "Campo name: mancante o vuoto.")
        elif report.declared_name != name:
            add_error(
                report,
                "name_mismatch",
                f"Campo name: '{report.declared_name}' diverso dalla cartella '{name}'.",
            )

        if "description" not in frontmatter or not report.description:
            add_error(report, "missing_description", "Campo description: mancante o vuoto.")
        else:
            description_len = len(report.description)
            if description_len < 20:
                add_warning(
                    report,
                    "description_short",
                    f"Description troppo breve ({description_len} caratteri).",
                )
            if description_len > 500:
                add_warning(
                    report,
                    "description_long",
                    f"Description troppo lunga ({description_len} caratteri).",
                )

    report.has_operational_body = has_operational_section(body, name)
    if not report.has_operational_body:
        add_warning(
            report,
            "missing_operational_body",
            "Body senza una sezione operativa chiaramente riconoscibile.",
        )

    scan_files(report, root)
    calculate_score(report)
    return report


def calculate_score(report: SkillReport) -> None:
    error_codes = {issue.code for issue in report.errors}
    warning_codes = {issue.code for issue in report.warnings}

    score = 0

    score += 4 if "naming_lowercase" not in error_codes else 0
    score += 4 if "naming_kebab_case" not in error_codes else 0
    score += 4 if "naming_underscore" not in error_codes else 0
    score += 4 if "naming_spaces" not in error_codes else 0
    score += 4 if "naming_ascii" not in error_codes else 0

    score += 10 if "missing_skill_md" not in error_codes else 0
    score += 10 if report.frontmatter_valid else 0

    score += 10 if report.declared_name and report.declared_name == report.name else 0
    score += 10 if report.description else 0

    score += 15 if report.has_operational_body else 0
    score += 10 if report.has_references else 0
    score += 10 if report.has_examples else 0

    if not (warning_codes & SAFETY_WARNING_CODES):
        score += 5

    if error_codes & SEVERE_ERROR_CODES:
        score = min(score, 60)

    report.score = max(0, min(100, score))
    report.grade = grade_for_score(report.score)
    report.recommended_action = recommended_action(report)


def grade_for_score(score: int) -> str:
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "E"


def recommended_action(report: SkillReport) -> str:
    if report.errors:
        return "Correggere errori bloccanti"
    if any(issue.code == "backup_file" for issue in report.warnings):
        return "Archiviare o rimuovere backup"
    if any(issue.code in {"sensitive_file", "suspicious_terms"} for issue in report.warnings):
        return "Verificare warning sicurezza"
    if not report.has_references and not report.has_examples:
        return "Valutare references/examples"
    if report.warnings:
        return "Rivedere warning"
    return "Mantenere"


def scan_skills(root: Path) -> list[SkillReport]:
    return [validate_skill(skill_dir, root) for skill_dir in find_skill_dirs(root)]


def all_errors(reports: Iterable[SkillReport]) -> list[Issue]:
    return [issue for report in reports for issue in report.errors]


def all_warnings(reports: Iterable[SkillReport]) -> list[Issue]:
    return [issue for report in reports for issue in report.warnings]


def escape_markdown_cell(value: object) -> str:
    text = str(value).replace("\n", " ").strip()
    return text.replace("|", "\\|")


def yes_no(value: bool) -> str:
    return "sì" if value else "no"


def timestamp(now: datetime | None = None) -> str:
    return (now or datetime.now()).strftime("%Y-%m-%d %H:%M:%S")


def write_index(root: Path, reports: list[SkillReport], now: datetime | None = None) -> Path:
    errors = all_errors(reports)
    warnings = all_warnings(reports)
    backup_files = sorted({item for report in reports for item in report.backup_files})

    lines = [
        "# SKILLS_INDEX",
        "",
        "Catalogo automatico delle skill presenti nella repository.",
        "",
        f"Aggiornato: {timestamp(now)}",
        "",
        "## Riepilogo",
        "",
        "| Voce | Valore |",
        "|---|---:|",
        f"| Skill totali | {len(reports)} |",
        f"| Skill con errors | {sum(1 for report in reports if report.errors)} |",
        f"| Skill con warnings | {sum(1 for report in reports if report.warnings)} |",
        "",
        "## Catalogo",
        "",
        "| Skill | Name dichiarato | Description | References | Examples | Errors | Warnings |",
        "|---|---|---|---:|---:|---:|---:|",
    ]

    for report in reports:
        lines.append(
            "| {skill} | {declared} | {description} | {references} | {examples} | {errors} | {warnings} |".format(
                skill=escape_markdown_cell(report.name),
                declared=escape_markdown_cell(report.declared_name),
                description=escape_markdown_cell(report.description),
                references=yes_no(report.has_references),
                examples=yes_no(report.has_examples),
                errors=len(report.errors),
                warnings=len(report.warnings),
            )
        )

    lines.extend(["", "## File backup rilevati", ""])
    if backup_files:
        lines.extend(f"- {path}" for path in backup_files)
    else:
        lines.append("- Nessuno.")

    lines.extend(
        [
            "",
            "## Note",
            "",
            "Il file è generato automaticamente da `validators/check_agent_skills.py`.",
            "",
        ]
    )

    output_path = root / "SKILLS_INDEX.md"
    output_path.write_text("\n".join(lines), encoding="utf-8")
    return output_path


def write_score(root: Path, reports: list[SkillReport], now: datetime | None = None) -> Path:
    lines = [
        "# SKILL_SCORE",
        "",
        "Pagella automatica delle skill.",
        "",
        f"Aggiornato: {timestamp(now)}",
        "",
        "| Skill | Score | Grade | Errori | Warning | Azione consigliata |",
        "|---|---:|---|---:|---:|---|",
    ]

    for report in reports:
        lines.append(
            "| {skill} | {score} | {grade} | {errors} | {warnings} | {action} |".format(
                skill=escape_markdown_cell(report.name),
                score=report.score,
                grade=report.grade,
                errors=len(report.errors),
                warnings=len(report.warnings),
                action=escape_markdown_cell(report.recommended_action),
            )
        )

    lines.append("")

    output_path = root / "SKILL_SCORE.md"
    output_path.write_text("\n".join(lines), encoding="utf-8")
    return output_path


def print_table(reports: list[SkillReport]) -> None:
    print("| Skill | Name | References | Examples | Errors | Warnings | Score | Grade |")
    print("|---|---|---:|---:|---:|---:|---:|---|")
    for report in reports:
        print(
            "| {skill} | {declared} | {references} | {examples} | {errors} | {warnings} | {score} | {grade} |".format(
                skill=escape_markdown_cell(report.name),
                declared=escape_markdown_cell(report.declared_name),
                references=yes_no(report.has_references),
                examples=yes_no(report.has_examples),
                errors=len(report.errors),
                warnings=len(report.warnings),
                score=report.score,
                grade=report.grade,
            )
        )


def print_issues(title: str, issues: list[Issue]) -> None:
    print()
    print(title)
    if not issues:
        print("- Nessuno.")
        return
    for issue in issues:
        path_part = f" [{issue.path}]" if issue.path else ""
        print(f"- {issue.skill}: {issue.message}{path_part}")


def final_recommendation(error_count: int, warning_count: int) -> str:
    if error_count:
        return "FAIL"
    if warning_count:
        return "PASS_WITH_WARNINGS"
    return "PASS"


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Validate Codex skill folders.")
    parser.add_argument("--root", default=".", help="Repository root to scan.")
    parser.add_argument("--write-index", action="store_true", help="Write SKILLS_INDEX.md.")
    parser.add_argument("--write-score", action="store_true", help="Write SKILL_SCORE.md.")
    parser.add_argument(
        "--fail-on-warning",
        action="store_true",
        help="Exit with code 1 when warnings are present.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    root = Path(args.root).resolve()
    if not root.is_dir():
        print(f"Root non valida: {root}")
        return 1

    reports = scan_skills(root)
    errors = all_errors(reports)
    warnings = all_warnings(reports)

    print_table(reports)
    print()
    print(f"Skill trovate: {len(reports)}")
    print(f"Errori: {len(errors)}")
    print(f"Warning: {len(warnings)}")

    print_issues("Errori", errors)
    print_issues("Warning", warnings)

    recommendation = final_recommendation(len(errors), len(warnings))
    print()
    print(f"Raccomandazione finale: {recommendation}")

    if args.write_index:
        output = write_index(root, reports)
        print(f"SKILLS_INDEX.md scritto: {relative_display(root, output)}")
    if args.write_score:
        output = write_score(root, reports)
        print(f"SKILL_SCORE.md scritto: {relative_display(root, output)}")

    if errors:
        return 1
    if args.fail_on_warning and warnings:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
