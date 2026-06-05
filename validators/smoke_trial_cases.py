#!/usr/bin/env python3
"""Smoke cases for the Codex skill validator.

The script creates temporary repositories only. It does not modify the real
repository except for reading the validator script.
"""

from __future__ import annotations

import subprocess
import sys
import tempfile
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
VALIDATOR = REPO_ROOT / "validators" / "check_agent_skills.py"


def write_skill(
    root: Path,
    folder_name: str,
    *,
    declared_name: str | None = None,
    description: str | None = None,
    include_references: bool = True,
    include_examples: bool = True,
) -> Path:
    skill_dir = root / folder_name
    skill_dir.mkdir(parents=True, exist_ok=True)
    name = declared_name if declared_name is not None else folder_name
    desc = description or "Use this temporary skill to validate smoke trial behavior."
    (skill_dir / "SKILL.md").write_text(
        "\n".join(
            [
                "---",
                f"name: {name}",
                f"description: {desc}",
                "---",
                "",
                f"# {folder_name}",
                "",
                "## Purpose",
                "",
                "Validate one temporary smoke case.",
                "",
                "## Workflow",
                "",
                "1. Create the case.",
                "2. Run the validator.",
                "3. Inspect the result.",
                "",
            ]
        ),
        encoding="utf-8",
    )
    if include_references:
        (skill_dir / "references").mkdir()
        (skill_dir / "references" / "standard.md").write_text("# Standard\n", encoding="utf-8")
    if include_examples:
        (skill_dir / "examples").mkdir()
        (skill_dir / "examples" / "demo.md").write_text("# Demo\n", encoding="utf-8")
    return skill_dir


def run_validator(root: Path, *extra_args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(VALIDATOR), "--root", str(root), *extra_args],
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )


def expect(condition: bool, label: str, failures: list[str]) -> None:
    status = "PASS" if condition else "FAIL"
    print(f"{status} - {label}")
    if not condition:
        failures.append(label)


def main() -> int:
    failures: list[str] = []
    with tempfile.TemporaryDirectory(prefix="codex-skill-smoke-") as tmp:
        temp_root = Path(tmp)

        write_skill(temp_root, "as-common-valid-smoke")
        result = run_validator(temp_root)
        expect(result.returncode == 0, "valid skill returns exit code 0", failures)
        expect("Raccomandazione finale: PASS" in result.stdout, "valid skill reports PASS", failures)

        write_skill(temp_root, "as-common-no-examples", include_examples=False)
        result = run_validator(temp_root)
        expect(result.returncode == 0, "skill without examples is not an error", failures)
        expect("as-common-no-examples" in result.stdout and "| no |" in result.stdout, "missing examples visible in table", failures)

        write_skill(temp_root, "as-common-bad_skill")
        result = run_validator(temp_root)
        expect(result.returncode == 1, "underscore skill returns exit code 1", failures)
        expect("underscore" in result.stdout.lower(), "underscore error is reported", failures)

        archive_skill = temp_root / "_archive" / "as-common-archived_bad"
        archive_skill.mkdir(parents=True)
        (archive_skill / "SKILL.md").write_text("invalid archived skill\n", encoding="utf-8")
        result = run_validator(temp_root)
        expect("as-common-archived_bad" not in result.stdout, "_archive skill is ignored", failures)

        generation_root = temp_root / "generation"
        generation_root.mkdir()
        write_skill(generation_root, "as-common-generation-smoke")
        result = run_validator(generation_root, "--write-index", "--write-score")
        expect(result.returncode == 0, "temporary index/score generation returns exit code 0", failures)
        expect((generation_root / "SKILLS_INDEX.md").is_file(), "temporary SKILLS_INDEX.md created", failures)
        expect((generation_root / "SKILL_SCORE.md").is_file(), "temporary SKILL_SCORE.md created", failures)

    print()
    if failures:
        print(f"SMOKE RESULT: FAIL ({len(failures)} failure(s))")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("SMOKE RESULT: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
