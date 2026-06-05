# Test Matrix Template

Use this matrix to decide what must run for a step.

| Area | Risk | Required check | Command | Expected result | Blocks publication | Notes |
|---|---|---|---|---|---|---|
| Git state | high | Branch and status | `git status --short` | Only expected changes | Yes | Include branch check when relevant. |
| Whitespace | medium | Diff check | `git --no-pager diff --check` | No errors | Yes | CRLF/LF notices can be advisory if command passes. |

## Risk levels

- blocker: cannot proceed without a passing check or user decision.
- high: failure can break users, data flow, publication, or release.
- medium: failure can break a feature or repeated workflow.
- low: failure affects docs, wording, or non-critical workflow.
- note: record only; does not block by itself.

## Test types

- unit;
- integration;
- smoke;
- regression;
- UI;
- data/schema;
- performance-light;
- security-light;
- documentation.

## Minimal test matrix

| Area | Risk | Required check | Command | Expected result | Blocks publication | Notes |
|---|---|---|---|---|---|---|
| Preflight | high | Branch/status/log | `git status --short` | Expected state only | Yes | Add log command when step order matters. |
| Validator | high | Local validator | `python validators/check_agent_skills.py` | PASS | Yes | For skill catalog work. |
| Unit tests | medium | Focused test file | `python validators/test_check_agent_skills.py` | All tests pass | Yes | Replace with project test command. |
| Diff | medium | Whitespace check | `git --no-pager diff --check` | No errors | Yes | Report line-ending notices separately. |
| Final state | medium | Status and stat | `git status --short` | Expected files only | Yes | Include `git --no-pager diff --stat`. |

## Extended test matrix

| Area | Risk | Required check | Command | Expected result | Blocks publication | Notes |
|---|---|---|---|---|---|---|
| FastAPI syntax | high | Import or compile check | `python -m compileall backend` | No failures | Yes | Add app import smoke if available. |
| FastAPI routes | high | Route smoke | `python scripts/check_routes.py` | Expected routes present | Yes | Use project script when present. |
| API health | high | Health endpoint | `GET /health` | 200 and expected payload | Yes for deploy | Capture URL and status. |
| UI smoke | medium | Render primary flow | Playwright smoke check | Page loads and key action works | Yes for UI change | Include screenshot if useful. |
| Workflow script | high | Verify pack | `pwsh -NoProfile -ExecutionPolicy Bypass -File scripts/verify.ps1` | Exit code 0 | Yes | Keep script non-destructive by default. |
| Docs | low | Changelog/index check | Project-specific command | Docs updated | Depends | Mandatory for docs-only steps. |
| Regression | medium | Representative scenario | Project-specific command | Same or approved output | Yes when behavior changed | Pair with golden samples if useful. |
