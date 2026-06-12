#!/usr/bin/env python3
"""Tests for prompt_length_advisor.py."""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "prompt_length_advisor.py"
SPEC = importlib.util.spec_from_file_location("prompt_length_advisor", SCRIPT_PATH)
assert SPEC is not None and SPEC.loader is not None
advisor = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(advisor)


REQUIRED = """
## CONTROLLO INTEGRITÀ PROMPT

Verifica sentinella e regole.

## REGOLE FINALI

Non fare commit.
Non fare push.
Non aprire PR.
Non fare merge.
Non fare deploy.

END_OF_PROMPT_0001
"""


def prompt_with_size(target_chars: int) -> str:
    filler_len = max(0, target_chars - len(REQUIRED))
    return ("a" * filler_len) + REQUIRED


class PromptLengthAdvisorTests(unittest.TestCase):
    def test_short_prompt_with_sentinel_and_final_rules_is_ok(self) -> None:
        result = advisor.analyze_prompt("Prompt breve.\n" + REQUIRED)

        self.assertEqual(result["status"], "OK")
        self.assertTrue(result["final_sentinel_present"])
        self.assertTrue(result["final_rules_present"])
        self.assertTrue(result["integrity_check_present"])
        self.assertTrue(result["required_sections_pass"])

    def test_35k_prompt_is_ok_grande(self) -> None:
        result = advisor.analyze_prompt(prompt_with_size(35_000))

        self.assertEqual(result["status"], "OK_GRANDE")

    def test_50k_prompt_is_review(self) -> None:
        result = advisor.analyze_prompt(prompt_with_size(50_000))

        self.assertEqual(result["status"], "REVIEW")

    def test_80k_prompt_is_split_consigliato(self) -> None:
        result = advisor.analyze_prompt(prompt_with_size(80_000))

        self.assertEqual(result["status"], "SPLIT_CONSIGLIATO")

    def test_110k_prompt_is_split_forte(self) -> None:
        result = advisor.analyze_prompt(prompt_with_size(110_000))

        self.assertEqual(result["status"], "SPLIT_FORTE")

    def test_prompt_without_sentinel_reports_risk(self) -> None:
        text = REQUIRED.replace("END_OF_PROMPT_0001", "")
        result = advisor.analyze_prompt(text)

        self.assertFalse(result["final_sentinel_present"])
        self.assertFalse(result["required_sections_pass"])
        self.assertEqual(result["initial_prompt_risk"], "high")

    def test_unclosed_code_fence_fails_integrity(self) -> None:
        result = advisor.analyze_prompt(REQUIRED + "\n```python\nprint('x')\n")

        self.assertFalse(result["code_fences_pass"])
        self.assertEqual(result["initial_prompt_risk"], "high")

    def test_broad_repository_read_and_full_diff_is_high_runtime_risk(self) -> None:
        text = REQUIRED + "\nLeggi tutto il repository e stampa tutto il diff con output completo.\n"
        result = advisor.analyze_prompt(text)

        self.assertEqual(result["runtime_context_growth_risk"], "high")

    def test_negative_commit_push_merge_bans_are_not_positive_publish(self) -> None:
        text = REQUIRED + "\nNon fare commit, non fare push, non fare merge.\n"
        result = advisor.analyze_prompt(text)

        self.assertEqual(result["publish_safety"], "pass")

    def test_positive_commit_and_push_without_gate_fails_publish_safety(self) -> None:
        text = REQUIRED + "\nFai commit e push appena finito.\n"
        result = advisor.analyze_prompt(text)

        self.assertEqual(result["publish_safety"], "fail")

    def test_stdin_mode_works(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(SCRIPT_PATH), "--json"],
            input=REQUIRED,
            text=True,
            capture_output=True,
            check=True,
        )
        data = json.loads(completed.stdout)

        self.assertEqual(data["status"], "OK")
        self.assertTrue(data["required_sections_pass"])

    def test_json_output_is_valid_and_stable(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            prompt_path = Path(tmp) / "prompt.md"
            prompt_path.write_text(REQUIRED, encoding="utf-8")

            first = subprocess.run(
                [sys.executable, str(SCRIPT_PATH), str(prompt_path), "--json"],
                text=True,
                capture_output=True,
                check=True,
            ).stdout
            second = subprocess.run(
                [sys.executable, str(SCRIPT_PATH), str(prompt_path), "--json"],
                text=True,
                capture_output=True,
                check=True,
            ).stdout

        self.assertEqual(first, second)
        data = json.loads(first)
        self.assertEqual(data["status"], "OK")
        self.assertIn("estimated_tokens", data)

    def test_missing_file_returns_nonzero_with_clear_message(self) -> None:
        completed = subprocess.run(
            [sys.executable, str(SCRIPT_PATH), "missing-prompt-file.md"],
            text=True,
            capture_output=True,
        )

        self.assertNotEqual(completed.returncode, 0)
        self.assertIn("File prompt non trovato", completed.stderr)


if __name__ == "__main__":
    unittest.main(verbosity=2)
