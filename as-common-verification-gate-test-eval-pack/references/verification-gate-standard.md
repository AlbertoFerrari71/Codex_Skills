# Verification Gate Standard

A verification gate is a defined set of checks that must pass before a step can be treated as ready for commit, push, pull request, merge, release, or deploy. It turns quality control from a vague final note into a repeatable decision.

In ChatGPT + Codex projects, gates matter because code, docs, prompts, generated files, and workflow scripts can all drift. A gate keeps evidence close to the change and makes the final report defensible.

## Check Types

- Preflight: confirms branch, working tree, recent log, remote, and expected baseline.
- Unit test: checks a focused function or module.
- Integration test: checks interaction between modules, services, files, or APIs.
- Smoke test: confirms the main path starts and performs a minimal useful action.
- Health check: confirms a running service responds as expected.
- UI check: confirms a visible flow renders and basic interaction works.
- Static check: checks syntax, formatting, lint, schema, or parseability.
- Diff check: checks Git whitespace and intended file scope.
- Documentation check: confirms docs, changelog, index, or generated catalogs are aligned.
- Final gate: repeats the mandatory checks after generation and edits are complete.

## Recommended verification order

| Order | Check | Purpose | Blocks publication | Evidence |
|----:|---|---|---|---|
| 1 | Preflight Git state | Confirm branch and clean or expected status. | Yes | `git status --short`, recent log. |
| 2 | Dependency-light static checks | Catch syntax and whitespace issues early. | Yes when mandatory. | Parser, compile, or lint output. |
| 3 | Unit tests | Verify focused logic. | Yes when code changed. | Test command and result. |
| 4 | Integration tests | Verify cross-module behavior. | Yes for shared behavior. | Test command and result. |
| 5 | Smoke / health checks | Verify primary runtime path. | Yes for runnable apps. | URL, endpoint, screenshot, or command output. |
| 6 | Evals / golden samples | Verify AI output or generated artifact quality. | Depends on scope. | Matrix, sample diff, grading notes. |
| 7 | Documentation checks | Confirm docs and generated indexes match. | Yes for docs/catalog work. | Generated files and diff summary. |
| 8 | Git diff check | Catch whitespace and unintended broad changes. | Yes | `git --no-pager diff --check`. |
| 9 | Final status | Confirm final working tree and next action. | Yes | `git status --short`, diff stat. |

## Mandatory, Optional, Advisory

- Mandatory check: must pass for publication or handoff approval.
- Optional check: useful but not required for the current risk level.
- Advisory check: non-blocking signal that should be recorded if available.

## Proceeding With Warnings

Proceed only when mandatory checks pass and warnings are explained. Examples:

- CRLF/LF notices that do not fail `git diff --check`;
- an optional tool is unavailable but equivalent evidence exists;
- a UI screenshot is not required for a docs-only change.

## Stop Conditions

Stop when:

- a mandatory test fails;
- `git diff --check` reports real whitespace errors;
- branch or working tree does not match the step contract;
- a generated artifact is stale and cannot be regenerated;
- a health check fails on a release or deploy path;
- evidence is missing for a required gate.

## Evidence Commands

Use commands that can be repeated:

```powershell
git status --short
git --no-pager diff --check
python -m pytest
python validators/test_check_agent_skills.py
python validators/check_agent_skills.py
pwsh -NoProfile -ExecutionPolicy Bypass -File scripts/verify.ps1
```

For services and UI flows, include a health endpoint check or Playwright smoke check when the project has a running app.
