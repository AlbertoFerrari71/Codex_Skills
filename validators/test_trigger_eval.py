#!/usr/bin/env python3
"""Deterministic trigger-eval checks for skill routing fixtures."""

from __future__ import annotations

import json
import sys
import unittest
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))

import check_agent_skills as validator


REPO_ROOT = Path(__file__).resolve().parents[1]
CASE_FILE = Path(__file__).resolve().with_name("trigger_eval_cases.json")
REQUIRED_FIELDS = {"id", "input", "expected_skill", "negative_skills", "tags"}


def load_cases(path: Path = CASE_FILE) -> list[dict[str, Any]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("trigger_eval_cases.json must contain a list")
    return data


def skill_names(root: Path = REPO_ROOT) -> set[str]:
    return {path.name for path in validator.find_skill_dirs(root)}


def validate_cases(cases: list[dict[str, Any]], available_skills: set[str]) -> list[str]:
    errors: list[str] = []
    seen_ids: set[str] = set()

    for index, case in enumerate(cases, start=1):
        if not isinstance(case, dict):
            errors.append(f"case {index}: not an object")
            continue

        missing = REQUIRED_FIELDS - set(case)
        if missing:
            errors.append(f"case {index}: missing fields {sorted(missing)}")
            continue

        case_id = case.get("id")
        if not isinstance(case_id, str) or not case_id.strip():
            errors.append(f"case {index}: id is empty")
        elif case_id in seen_ids:
            errors.append(f"case {index}: duplicate id {case_id}")
        else:
            seen_ids.add(case_id)

        input_text = case.get("input")
        if not isinstance(input_text, str) or not input_text.strip():
            errors.append(f"{case_id or index}: input is empty")

        expected_skill = case.get("expected_skill")
        if not isinstance(expected_skill, str) or expected_skill not in available_skills:
            errors.append(f"{case_id or index}: expected skill does not exist: {expected_skill}")

        negative_skills = case.get("negative_skills")
        if not isinstance(negative_skills, list) or not negative_skills:
            errors.append(f"{case_id or index}: negative_skills must be a non-empty list")
            negative_skills = []

        for negative_skill in negative_skills:
            if not isinstance(negative_skill, str) or negative_skill not in available_skills:
                errors.append(f"{case_id or index}: negative skill does not exist: {negative_skill}")

        if isinstance(expected_skill, str) and expected_skill in negative_skills:
            errors.append(f"{case_id or index}: expected skill is also negative")

        tags = case.get("tags")
        if not isinstance(tags, list) or not tags or not all(isinstance(tag, str) and tag.strip() for tag in tags):
            errors.append(f"{case_id or index}: tags must be a non-empty string list")

    return errors


class TriggerEvalTests(unittest.TestCase):
    def test_trigger_eval_cases_are_valid(self) -> None:
        cases = load_cases()
        errors = validate_cases(cases, skill_names())

        self.assertGreaterEqual(len(cases), 20)
        self.assertEqual(errors, [])

    def test_trigger_eval_detects_unknown_skill(self) -> None:
        cases = [
            {
                "id": "unknown_skill",
                "input": "test",
                "expected_skill": "as-common-missing-skill",
                "negative_skills": ["as-common-codex-command-pack"],
                "tags": ["test"],
            }
        ]

        errors = validate_cases(cases, {"as-common-codex-command-pack"})

        self.assertTrue(any("expected skill does not exist" in error for error in errors))

    def test_trigger_eval_detects_duplicate_id(self) -> None:
        cases = [
            {
                "id": "duplicate",
                "input": "test 1",
                "expected_skill": "as-common-codex-command-pack",
                "negative_skills": ["as-common-codex-step-manager"],
                "tags": ["test"],
            },
            {
                "id": "duplicate",
                "input": "test 2",
                "expected_skill": "as-common-codex-step-manager",
                "negative_skills": ["as-common-codex-command-pack"],
                "tags": ["test"],
            },
        ]
        available = {"as-common-codex-command-pack", "as-common-codex-step-manager"}

        errors = validate_cases(cases, available)

        self.assertTrue(any("duplicate id" in error for error in errors))


if __name__ == "__main__":
    unittest.main(verbosity=2)
