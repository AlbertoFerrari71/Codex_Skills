---
name: as-common-codex-report-intake-decision-gate
description: Use this skill when Alberto provides a completed Codex final report and needs it compared with the original prompt, Git status, diffs, tests, warnings, and evidence to decide GO, GO_WITH_WARNINGS, NO_GO, clarification needs, or corrective follow-up. Do not use it to design test gates before work starts.
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

## Do Not Use This Skill When

- The work is still planning tests, smoke checks, evals, or evidence before implementation.
- Alberto needs a new verification matrix or golden sample policy, not a decision on a received report.
- The task is a generic repository readiness review before starting a step.

## Use Instead

- `as-common-verification-gate-test-eval-pack` to design verification gates, test matrices, smoke checks, evals, and stop policies.
- `as-common-repo-readiness-review` for read-only technical repository readiness before work begins.

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
