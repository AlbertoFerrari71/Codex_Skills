# Evidence Check Standard

Evidence is stronger when it is current, local, command-backed, and directly tied to the requested scope.

## Evidence Hierarchy

1. Current command output from the target repository.
2. Current Git diff/status/log evidence.
3. Generated files produced by documented commands.
4. Source file content.
5. Prior Codex reports.
6. Assumptions or user-provided summary without local verification.

## Required Evidence By Task Type

| Task type | Required evidence | Optional evidence | Missing evidence consequence |
|---|---|---|---|
| Skill repository change | Validator, unit tests, regenerated index/score, diff check, status. | Targeted diff. | NO_GO_FIXABLE if catalog or validator evidence is missing. |
| Python/FastAPI change | Unit tests, import/compile smoke, route or health check when relevant. | Coverage or integration suite. | NO_GO_FIXABLE or NO_GO_BLOCKER depending on risk. |
| PowerShell automation | Script syntax/read review, non-destructive dry run if available, Git gate. | PSScriptAnalyzer when available. | NEEDS_CLARIFICATION if command safety is unclear. |
| VBA/Excel tool | Code review, manual test instructions, fixture-free sample where possible. | Workbook smoke test. | NEEDS_CLARIFICATION if runtime cannot be verified. |
| C++/OpenCV change | Build/test command, sample image or fixture check, output review. | Performance-light timing. | NO_GO_FIXABLE if sample check is missing. |
| Documentation-only change | Diff review, link/heading consistency, changelog if required. | Markdown lint. | GO_WITH_WARNINGS or NO_GO_FIXABLE depending on missing item. |
| GitHub workflow change | YAML parse/review, local command if available, CI plan. | Remote workflow run. | NEEDS_CLARIFICATION if CI cannot be observed. |
| UI/Playwright change | Smoke check, screenshot or trace when practical, console error review. | Mobile viewport check. | NO_GO_FIXABLE if primary flow was not tested. |

## Test Evidence

Record:

- exact command;
- result;
- failure text when relevant;
- whether the command was rerun after fixes;
- not-run reason when skipped.

## Warning Evidence

Every warning needs:

- source;
- classification;
- reason it is or is not blocking;
- follow-up action if any.
