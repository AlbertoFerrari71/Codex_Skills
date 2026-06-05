---
name: as-common-codex-report-intake-decision-gate
description: Use this skill when reviewing a final Codex report, comparing it with the original prompt, Git status, diffs, tests, warnings, and verification evidence to decide GO, GO_WITH_WARNINGS, NO_GO, clarification needs, or a corrective follow-up prompt.
---

# as-common-codex-report-intake-decision-gate

## Purpose

Transform a final Codex report into a verified decision. Use this skill to compare claims against prompt scope, Git state, diffs, tests, warnings, and verification evidence before accepting a step or preparing publication commands.

## Use this skill when

- Alberto pastes a final Codex report;
- deciding whether commit/push is allowed;
- comparing a report with the original prompt;
- checking declared tests;
- verifying Git status and diff;
- classifying warnings;
- deciding whether a corrective prompt is needed;
- preparing a final PowerShell command;
- closing a step in a traceable way.

## Workflow

1. Identify the requested step and expected scope.
2. Extract Codex claims from the report.
3. Compare claims with evidence.
4. Review Git status and changed files.
5. Review tests and verification commands.
6. Classify warnings and missing checks.
7. Decide GO / GO_WITH_WARNINGS / NO_GO_FIXABLE / NO_GO_BLOCKER / NEEDS_CLARIFICATION.
8. Produce either commit/push instructions or corrective prompt.
9. Record next recommended step.

## Required outputs

- report intake summary;
- evidence checklist;
- changed-file review;
- test verification review;
- warning classification;
- decision gate;
- commit/push readiness checklist;
- corrective follow-up prompt when needed;
- next-step recommendation.

## Safety rules

- Never accept report claims without evidence.
- Never approve commit/push if mandatory tests failed.
- Never approve commit/push if Git status shows unexpected files.
- Never hide warnings.
- Distinguish warnings from blockers.
- If evidence is missing, ask for it or mark NO_GO_FIXABLE.
- Keep credentials and private data out of copied reports.
- Preserve Alberto's standard final status lines.

## References

- `references/report-intake-standard.md`
- `references/diff-review-checklist.md`
- `references/decision-gate-matrix.md`
- `references/evidence-check-standard.md`
- `references/follow-up-prompt-template.md`
- `references/commit-push-readiness-template.md`

## Examples

- `examples/demo-prompts.md`
- `examples/sample-report-intake.md`
- `examples/sample-no-go-corrective-prompt.md`
