# 100 Release Decision Gate

Use this gate before accepting, committing, pushing, or handing off a skill release step.

| Decision | Conditions | Required evidence | Allowed next action |
| -------- | ---------- | ----------------- | ------------------- |
| GO | All mandatory checks pass; files match scope; catalog and changelog are updated. | Test output, validator PASS, smoke result, diff checks, Git status. | Commit and push direct to `main` if authorized. |
| GO_WITH_WARNINGS | Mandatory checks pass; warnings are understood and non-blocking. | Warning classification and exit code evidence. | Commit/push if warning is documented. |
| NO_GO_FIXABLE | Missing catalog update, missing changelog, missing smoke trial, or expected file not staged. | Diff/status evidence and corrective action. | Fix and rerun gates. |
| NO_GO_BLOCKER | Validator fail, failed staged diff check, wrong branch, failed mandatory test, unsafe file, or unexpected destructive change. | Command output and affected files. | Stop and correct before publication. |
| NEEDS_CLARIFICATION | Scope, authority, publication policy, or expected output is unclear. | Open question list. | Ask Alberto or prepare clarification prompt. |

## Specific rules

- Validator fail -> NO_GO_BLOCKER.
- Missing catalog update -> NO_GO_FIXABLE.
- Missing smoke trial on major skill -> GO_WITH_WARNINGS or NO_GO_FIXABLE depending on risk.
- LF/CRLF warning with exit code 0 -> GO_WITH_WARNINGS.
- Unexpected files -> NO_GO_FIXABLE or NO_GO_BLOCKER depending on risk.
- Failed staged diff check -> NO_GO_BLOCKER.
- Direct push to `main` is allowed only after all mandatory local gates pass and the current step authorizes publication.
- PR workflow is an alternative for protected repositories or explicit review requests.

## Evidence order

1. Branch and status.
2. Validator tests.
3. Skill validator.
4. Catalog regeneration.
5. Smoke script or targeted smoke trial.
6. Release workflow checker when present.
7. Diff check.
8. Staged diff check.
9. Commit/push evidence.
10. Final status and log.
