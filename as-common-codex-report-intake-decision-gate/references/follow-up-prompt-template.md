# Follow-Up Prompt Template

Use these templates when the intake gate is not ready for GO.

## 1. Missing Verification Prompt

```markdown
# Corrective Codex Prompt

## Situation

The final report does not provide enough verification evidence for the requested step.

## What passed

- Known passed checks:

## What failed or is missing

- Missing exact command output:
- Missing regenerated files:
- Missing final Git status:

## Exact files to inspect

- `<file>`

## Constraints

- Do not commit.
- Do not push.
- Do not create PRs.
- Do not modify unrelated files.

## Required commands

- `git status --short`
- `git --no-pager diff --check`
- `<project-specific-check>`

## Expected final report

Include commands, results, warnings, not-run checks, final status, and next step.

## Do not commit/push

Stop after the report.
```

## 2. Failed Test Correction Prompt

```markdown
# Corrective Codex Prompt

## Situation

A mandatory verification command failed during report intake.

## What passed

- Passed checks:

## What failed or is missing

- Failed command:
- Failure output:

## Exact files to inspect

- `<file>`

## Constraints

- Make the smallest clear fix.
- Do not change unrelated behavior.
- Do not commit or push.

## Required commands

- Rerun the failed command.
- Run `git --no-pager diff --check`.
- Run final `git status --short`.

## Expected final report

Report the fix, exact commands, pass/fail results, warnings, and remaining risks.

## Do not commit/push

Stop after verification.
```

## 3. Unexpected File Changes Prompt

```markdown
# Corrective Codex Prompt

## Situation

The report or Git status shows files outside the expected scope.

## What passed

- Known valid changes:

## What failed or is missing

- Unexpected files:
- Missing explanation:

## Exact files to inspect

- `<unexpected-file>`

## Constraints

- Do not delete or revert user changes without explicit approval.
- Explain whether each file is required.
- Keep only in-scope changes.
- Do not commit or push.

## Required commands

- `git status --short`
- `git --no-pager diff --name-status`
- `git --no-pager diff -- <unexpected-file>`

## Expected final report

Classify each unexpected file as required, user-owned, generated, or out of scope.

## Do not commit/push

Stop after classification or correction.
```
