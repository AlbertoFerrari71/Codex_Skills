# 090 Codex Report Intake Trial

Skill under trial: `as-common-codex-report-intake-decision-gate`

## Cases

| Case | Report condition | Evidence expected | Decision |
|---:|---|---|---|
| 1 | Complete and coherent report. | Prompt scope, files, tests, status, diff, next step. | GO |
| 2 | "Tests passed" without commands. | Missing command evidence. | NO_GO_FIXABLE |
| 3 | Unexpected files modified. | `git status --porcelain=v1`, diff stat. | NO_GO_BLOCKER or NO_GO_FIXABLE |
| 4 | Working tree dirty. | `git status --porcelain=v1`. | NO_GO_FIXABLE |
| 5 | Wrong branch. | `git --no-pager branch --show-current`. | NO_GO_BLOCKER |
| 6 | CRLF/LF warning with diff check exit 0. | Exit code 0 and no whitespace errors. | GO_WITH_WARNINGS |
| 7 | Commit/push done despite prompt ban. | Log and remote evidence. | NO_GO_BLOCKER |
| 8 | Real step 085 report synthesis. | 20 rules, validator PASS, commit `408e81b`, LF/CRLF warning. | GO_WITH_WARNINGS |

## Case 1 - Complete report

Expected intake summary:

- requested step matched;
- changed files are expected;
- validator and tests passed;
- warnings none or documented;
- final status is GO.

## Case 2 - Missing test commands

Red flag: report says "tests passed" but gives no command.

Decision: NO_GO_FIXABLE.

Corrective prompt: ask Codex to run the missing checks and report exact commands and exit status.

## Case 3 - Unexpected file changes

Decision rule:

- harmless generated catalog missed by report: NO_GO_FIXABLE;
- unrelated source/config change: NO_GO_BLOCKER until inspected.

## Case 4 - Dirty working tree

Decision: NO_GO_FIXABLE.

Action: classify every changed/untracked path before accepting the report.

## Case 5 - Wrong branch

Decision: NO_GO_BLOCKER.

Action: stop publication and ask for branch correction or explicit authorization.

## Case 6 - LF/CRLF warning

Decision: GO_WITH_WARNINGS when `git --no-pager diff --check` exits 0.

## Case 7 - Commit/push despite ban

Decision: NO_GO_BLOCKER.

Action: do not continue publication. Identify commit, pushed ref, and required recovery path.

## Case 8 - Step 085 report synthesis

Input facts:

- 20 PowerShell hardening rules integrated;
- validator PASS with 17 skills, 0 errors, 0 warnings;
- parser PowerShell OK;
- commit `408e81b 085) Add PowerShell command pack hardening rules`;
- push to `origin/main` completed;
- LF/CRLF warnings were non-blocking because diff checks passed.

Decision: GO_WITH_WARNINGS, already published.

Next step: 090. Skill Smoke Trial Pack.
