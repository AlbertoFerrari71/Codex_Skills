#!/usr/bin/env python3
"""Check that the skill release workflow pack is present and wired."""

from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]

REQUIRED_PATHS = (
    "SKILLS_INDEX.md",
    "SKILL_SCORE.md",
    "CHANGELOG.md",
    "docs/roadmap.md",
    "docs/release-workflow",
    "docs/release-workflow/100_SKILL_RELEASE_WORKFLOW_PACK.md",
    "docs/release-workflow/100_SKILL_RELEASE_CHECKLIST.md",
    "docs/release-workflow/100_SKILL_AUTHORING_RELEASE_FLOW.md",
    "docs/release-workflow/100_SKILL_MODIFICATION_RELEASE_FLOW.md",
    "docs/release-workflow/100_AI_SOFTWARE_FACTORY_HANDOFF.md",
    "docs/release-workflow/100_RELEASE_DECISION_GATE.md",
    "templates/skill-release-prompt-template.md",
)

STRATEGIC_SKILLS = (
    "as-common-agent-context-governor",
    "as-common-verification-gate-test-eval-pack",
    "as-common-codex-report-intake-decision-gate",
)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def main() -> int:
    failures: list[str] = []

    for rel_path in REQUIRED_PATHS:
        path = REPO_ROOT / rel_path
        if not path.exists():
            failures.append(f"Missing required path: {rel_path}")

    for skill in STRATEGIC_SKILLS:
        if not (REPO_ROOT / skill / "SKILL.md").is_file():
            failures.append(f"Missing strategic skill: {skill}")

    index_path = REPO_ROOT / "SKILLS_INDEX.md"
    score_path = REPO_ROOT / "SKILL_SCORE.md"
    index_text = read_text(index_path) if index_path.is_file() else ""
    score_text = read_text(score_path) if score_path.is_file() else ""

    for skill in STRATEGIC_SKILLS:
        if skill not in index_text:
            failures.append(f"SKILLS_INDEX.md does not cite: {skill}")
        if skill not in score_text:
            failures.append(f"SKILL_SCORE.md does not cite: {skill}")

    if failures:
        print("RELEASE WORKFLOW CHECK: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("RELEASE WORKFLOW CHECK: PASS")
    print(f"Required paths checked: {len(REQUIRED_PATHS)}")
    print(f"Strategic skills checked: {len(STRATEGIC_SKILLS)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
