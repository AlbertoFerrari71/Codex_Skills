# Decision Gate Matrix

Use this matrix after reviewing report claims, evidence, tests, warnings, Git status, and diff.

| Decision | Conditions | Allowed next action | Typical message |
|---|---|---|---|
| GO | Mandatory checks passed, status expected, scope matches prompt, warnings none or trivial. | Prepare commit/push only if explicitly requested. | Gate positive: evidence matches report and scope. |
| GO_WITH_WARNINGS | Mandatory checks passed, warnings are known, non-blocking, and documented. | Proceed with stated caution; do not hide warning. | Gate positive with warning: proceed only with noted attention. |
| NO_GO_FIXABLE | Missing regeneration, missing command output, failed check with clear local fix, or expected untracked files not handled. | Create corrective prompt or ask Codex to rerun/fix. | Not ready: fixable evidence or scope gap remains. |
| NO_GO_BLOCKER | Wrong branch, destructive change, failed mandatory test, sensitive values found, or unsafe publication action. | Stop and ask Alberto or open a corrective step. | Not ready: blocker must be resolved before publication. |
| NEEDS_CLARIFICATION | Scope unclear, report lacks enough evidence, or requested action conflicts with repo rules. | Ask for missing evidence or decision. | Cannot decide: clarification required. |

## Classification Notes

- GO requires evidence, not confidence.
- GO_WITH_WARNINGS still requires mandatory checks to pass.
- NO_GO_FIXABLE is for clear, bounded corrections.
- NO_GO_BLOCKER is for safety, branch, mandatory gate, or destructive issues.
- NEEDS_CLARIFICATION is better than guessing.
