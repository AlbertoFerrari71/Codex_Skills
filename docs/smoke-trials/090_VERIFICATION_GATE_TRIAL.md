# 090 Verification Gate Trial

Skill under trial: `as-common-verification-gate-test-eval-pack`

## Cases

| Case | Input / condition | Expected behavior | Decision |
|---:|---|---|---|
| 1 | Validator PASS, tests OK, diff check OK, status expected. | Publish gate may proceed. | GO |
| 2 | Report says "all OK" but no test command is listed. | Missing evidence blocks acceptance until fixed. | NO_GO_FIXABLE |
| 3 | `git diff --check` exits 0 with LF/CRLF warnings. | Treat as attention point, not failed gate. | GO_WITH_WARNINGS |
| 4 | `git --no-pager diff --cached --check` missing before commit. | Require staged diff check before commit. | NO_GO_FIXABLE |
| 5 | Golden sample missing for risky output generation. | Add warning or require sample depending on risk. | GO_WITH_WARNINGS or NO_GO_FIXABLE |
| 6 | Health check not applicable to docs-only change. | Mark NOT_RUN with reason, not failure. | GO |
| 7 | AI report eval with minimum criteria. | Use eval matrix and pass criteria before decision. | GO or NO_GO_FIXABLE |

## Case 1 - Gate positive

Mandatory checks:

- `python validators/test_check_agent_skills.py`
- `python validators/check_agent_skills.py`
- `python validators/check_agent_skills.py --write-index --write-score`
- `git --no-pager diff --check`
- `git status --porcelain=v1`

Expected decision: GO.

## Case 2 - Test not executed

Problem: the report claims success but provides no command evidence.

Expected decision: NO_GO_FIXABLE.

Corrective action: ask Codex to run or report the exact test command, output summary, and failure reason if unavailable.

## Case 3 - LF/CRLF warning with exit code 0

Condition: Git prints line-ending notices, but `git --no-pager diff --check` returns 0.

Expected decision: GO_WITH_WARNINGS.

Rationale: warning is tracked, but publication is not blocked when the diff check itself passes.

## Case 4 - Missing staged diff check

Condition: unstaged diff check passed, files were staged, but `git --no-pager diff --cached --check` was not run.

Expected decision: NO_GO_FIXABLE before commit.

## Case 5 - Golden sample missing

Condition: output quality depends on generated docs or AI output.

Expected behavior:

- low risk: warning and next-step note;
- high risk: require golden sample before GO.

## Case 6 - Health check not applicable

Condition: documentation-only step with no service or endpoint.

Expected behavior: mark health check as NOT_RUN with reason "not applicable to docs-only change".

## Case 7 - Eval output AI

| Eval item | Input | Expected behavior | Pass criteria | Decision impact |
|---|---|---|---|---|
| Final Codex report | Report text | Lists files, tests, warnings, status, next step. | All mandatory fields present. | Missing fields block acceptance. |
| Warning classification | LF/CRLF warning | Distinguishes warning from error. | Exit code evidence included. | Wrong classification blocks publication. |
| Scope match | Requested files vs changed files | No unexpected files. | Status/diff evidence supports claim. | Unexpected files require fix. |
