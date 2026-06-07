#!/usr/bin/env python3
"""Run the local reproducibility checks for the skill repository."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def display_command(args: list[str]) -> str:
    return " ".join(args)


def run_check(label: str, args: list[str]) -> int:
    print()
    print(f"== {label} ==", flush=True)
    print(display_command(args), flush=True)
    try:
        result = subprocess.run(
            args,
            cwd=REPO_ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
    except FileNotFoundError:
        print(f"Command not found: {args[0]}")
        return 1
    if result.stdout:
        print(result.stdout, end="")
    return result.returncode


def main() -> int:
    checks = [
        (
            "Skill catalog validator",
            [sys.executable, str(REPO_ROOT / "validators" / "check_agent_skills.py"), "--root", str(REPO_ROOT)],
        ),
        (
            "Validator unit tests",
            [
                sys.executable,
                "-m",
                "unittest",
                "discover",
                "-s",
                str(REPO_ROOT / "validators"),
                "-p",
                "test_*.py",
            ],
        ),
        (
            "Smoke trial cases",
            [sys.executable, str(REPO_ROOT / "validators" / "smoke_trial_cases.py")],
        ),
        (
            "Release workflow wiring",
            [sys.executable, str(REPO_ROOT / "validators" / "release_workflow_check.py")],
        ),
        (
            "Git whitespace check",
            ["git", "--no-pager", "diff", "--check"],
        ),
    ]

    failures: list[tuple[str, int]] = []
    for label, args in checks:
        exit_code = run_check(label, args)
        if exit_code != 0:
            failures.append((label, exit_code))

    print()
    if failures:
        print("REPOSITORY HEALTH: FAIL")
        for label, exit_code in failures:
            print(f"- {label}: exit code {exit_code}")
        return 1

    print("REPOSITORY HEALTH: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
