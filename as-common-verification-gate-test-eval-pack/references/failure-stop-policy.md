# Failure Stop Policy

A verification gate is useful only if failures change behavior. Do not continue to publication steps when mandatory checks fail.

## Operating Rules

- Stop immediately on blocker failures.
- Apply a simple fix only when the cause is clear and inside scope.
- Do not retry blindly.
- Do not commit or push when a mandatory gate fails.
- Do not turn a failed check into a warning without a documented reason.
- Ask Alberto when the correct action changes scope, risk, or publication timing.
- Generate a corrective Codex prompt when the fix needs a focused follow-up step.

## Classification

- FAIL_BLOCKER: cannot proceed without user input or an external-state change.
- FAIL_FIXABLE: cause is clear, scoped, and can be corrected now.
- PASS_WITH_WARNINGS: mandatory checks pass, but advisory items remain.
- PASS: mandatory checks pass and no relevant warnings remain.

| Condition | Classification | Action | Publish allowed |
|---|---|---|---|
| Mandatory test fails and cause is unclear | FAIL_BLOCKER | Stop and report evidence. | No |
| Mandatory test fails and cause is clear | FAIL_FIXABLE | Fix if in scope, then rerun gate. | No until rerun passes |
| Branch is not expected | FAIL_BLOCKER | Stop and ask or switch only if explicitly allowed. | No |
| `git --no-pager diff --check` returns errors | FAIL_FIXABLE | Correct whitespace or report blocker. | No |
| Optional check unavailable | PASS_WITH_WARNINGS | Record not-run reason and substitute evidence if available. | Yes if mandatory checks pass |
| Health check fails before deploy | FAIL_BLOCKER | Stop publication path. | No |
| All mandatory checks pass | PASS | Report evidence and proceed as authorized. | Yes |

## When To Ask Alberto

Ask when:

- the fix requires a broader refactor;
- a deployment or merge decision is involved;
- the expected baseline is ambiguous;
- a not-run check affects confidence materially;
- the gate result conflicts with the requested next action.
