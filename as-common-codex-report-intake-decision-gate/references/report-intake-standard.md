# Report Intake Standard

Report intake is the review step between a Codex final report and a GO / NO-GO decision. The reviewer must not accept the report by trust alone. Claims need evidence from commands, diffs, files, and prompt scope.

## What To Extract

- Step number and title.
- Stated objective.
- Files created, modified, moved, or deleted.
- Tests and verification commands.
- Reported failures, warnings, and not-run checks.
- Git branch, status, log, and diff summary.
- Claimed next step.
- Any publication action already performed.

## Mapping Claims To Evidence

For each claim, identify the evidence:

- file claim -> `git status --short`, `git --no-pager diff --name-status`;
- test claim -> exact command and pass/fail output;
- generated catalog claim -> regenerated file diff;
- warning claim -> warning text and classification;
- branch claim -> `git --no-pager branch --show-current`.

## Missing Or Vague Test Claims

If a report says tests passed without commands, do not classify the gate as GO. Ask for command output, rerun the check, or mark the decision as NEEDS_CLARIFICATION or NO_GO_FIXABLE.

## Scope And File Changes

Compare the changed files with the original prompt:

- expected files: allowed by prompt or required by generated catalog updates;
- unexpected files: outside scope, unclear, or not explained;
- generated files: acceptable only when regeneration was requested or required;
- deleted/renamed files: require explicit explanation.

## Report Completeness

A complete report includes:

- step executed;
- status;
- branch;
- changed files;
- commands and results;
- warnings and not-run checks;
- Git status;
- risks;
- next step.

## Summary For Alberto

Keep the intake summary compact:

- decision;
- why;
- blocking issues;
- safe next action;
- corrective prompt if needed.

| Report section | What to extract | Evidence needed | Red flags |
|---|---|---|---|
| Status | Claimed completion state | Commands, diff, final status | "Tests passed" without commands. |
| Files changed | Created/modified/moved/deleted files | `git status --short`, name-status, diff stat | File modified outside prompt scope. |
| Tests | Commands and outcomes | Exact command output or rerun result | Test not executed but described as OK. |
| Git state | Branch, status, log | Branch/status/log commands | Unexpected branch or dirty tree. |
| Diff | Scope and content | Diff stat, targeted diff | Claimed fix without diff evidence. |
| Warnings | Warning type and handling | Warning text and reason | Warning not explained. |
| Publication | Commit/push/PR/merge/deploy action | Git log, remote, PR evidence | Publication despite explicit ban. |

## Red Flags

- "tests passed" without commands.
- "fixed" without diff.
- Files modified outside requested scope.
- Unexpected branch.
- Working tree dirty beyond expected files.
- Tests not run but described as OK.
- Warnings not explained.
- Commit/push done despite a no-publication rule.
