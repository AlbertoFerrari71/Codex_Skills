#!/usr/bin/env python3
"""Run the local reproducibility checks for the skill repository."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]


def display_command(args: list[str]) -> str:
    return " ".join(args)


def extract_result_status(output: str) -> str | None:
    for line in output.splitlines():
        if line.startswith("RESULT:"):
            return line.split(":", 1)[1].strip()
    return None


def run_check(label: str, args: list[str]) -> tuple[int, str | None]:
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
        return 1, None
    if result.stdout:
        print(result.stdout, end="")
    status = extract_result_status(result.stdout)
    if label == "Installed Skills Sync Check" and status:
        print(f"Installed Skills Sync Check: {status}")
    return result.returncode, status


def run_eol_report() -> list[str]:
    print()
    print("== Git EOL report ==", flush=True)
    args = ["git", "ls-files", "--eol"]
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
        return ["git command not found; EOL report skipped."]
    if result.stdout:
        print(result.stdout, end="")
    if result.returncode != 0:
        return [f"git ls-files --eol returned exit code {result.returncode}."]

    warnings: list[str] = []
    for line in result.stdout.splitlines():
        if "w/mixed" in line:
            warnings.append(f"EOL mixed worktree entry: {line}")
    return warnings


def main() -> int:
    checks = [
        (
            "Skill catalog validator and catalog freshness",
            [
                sys.executable,
                str(REPO_ROOT / "validators" / "check_agent_skills.py"),
                "--root",
                str(REPO_ROOT),
                "--fail-on-warning",
                "--check-catalog-freshness",
            ],
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
            "Installed Skills Sync Check",
            [
                sys.executable,
                str(REPO_ROOT / "validators" / "installed_skills_sync_check.py"),
                "--root",
                str(REPO_ROOT),
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
    non_blocking_warnings: list[str] = []
    for label, args in checks:
        exit_code, status = run_check(label, args)
        if exit_code != 0:
            failures.append((label, exit_code))
        elif label == "Installed Skills Sync Check" and status == "PASS WITH NON-BLOCKING WARNINGS":
            non_blocking_warnings.append("Installed Skills Sync Check: PASS WITH NON-BLOCKING WARNINGS")

    non_blocking_warnings.extend(run_eol_report())

    print()
    if failures:
        print("REPOSITORY HEALTH: FAIL")
        for label, exit_code in failures:
            print(f"- {label}: exit code {exit_code}")
        return 1

    if non_blocking_warnings:
        print("REPOSITORY HEALTH: PASS WITH NON-BLOCKING WARNINGS")
        for warning in non_blocking_warnings:
            print(f"- WARNING: {warning}")
        return 0

    print("REPOSITORY HEALTH: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
