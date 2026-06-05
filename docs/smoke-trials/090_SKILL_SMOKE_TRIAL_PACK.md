# 090 Skill Smoke Trial Pack

## Purpose

This pack records a realistic smoke trial for the strategic Codex skills and the PowerShell command pack standards in this repository.

It verifies happy paths, negative paths, borderline cases, and historical failure modes without modifying real project state outside the repository documentation and validator smoke script.

## Skills under trial

| Skill | Trial file | Result |
|---|---|---|
| `as-common-agent-context-governor` | `090_CONTEXT_GOVERNOR_TRIAL.md` | PASS |
| `as-common-verification-gate-test-eval-pack` | `090_VERIFICATION_GATE_TRIAL.md` | PASS |
| `as-common-codex-report-intake-decision-gate` | `090_REPORT_INTAKE_TRIAL.md` | PASS |
| `as-common-pwsh-command-pack` | `090_POWERSHELL_COMMAND_PACK_TRIAL.md` | PASS |
| `as-common-powershell-git-safe-flow` | `090_POWERSHELL_COMMAND_PACK_TRIAL.md` | PASS |

## Smoke method

1. Review each target skill against its intended use.
2. Simulate realistic user inputs and Codex reports.
3. Classify expected outputs as GO, GO_WITH_WARNINGS, NO_GO_FIXABLE, NO_GO_BLOCKER, NEEDS_CLARIFICATION, or NOT_RUN.
4. Cover historical PowerShell command pack bugs from step 080 and 085.
5. Run an optional Python smoke checker in temporary directories only.
6. Regenerate `SKILLS_INDEX.md` and `SKILL_SCORE.md`.
7. Run validator, diff checks, and staged diff check before publication.

## Expected gate

| Gate | Expected result | Blocks publication |
|---|---|---|
| `python validators/test_check_agent_skills.py` | Pass | Yes |
| `python validators/check_agent_skills.py` | PASS, 0 errors, 0 warnings | Yes |
| `python validators/check_agent_skills.py --write-index --write-score` | Pass | Yes |
| `python validators/smoke_trial_cases.py` | PASS | Yes |
| `git --no-pager diff --check` | Exit code 0 | Yes |
| `git --no-pager diff --cached --check` | Exit code 0 | Yes |

LF/CRLF warnings from Git are attention points only when the command exit code is 0.

## Outcome

The smoke trial confirms that the strategic skills are usable together:

- context governance decides the active instruction set;
- verification gate defines mandatory evidence and stop policy;
- report intake compares Codex claims with evidence;
- PowerShell command pack rules prevent historical paste, Git, DOCX, clipboard, and success-state errors.

## Files in this pack

- `090_CONTEXT_GOVERNOR_TRIAL.md`
- `090_VERIFICATION_GATE_TRIAL.md`
- `090_REPORT_INTAKE_TRIAL.md`
- `090_POWERSHELL_COMMAND_PACK_TRIAL.md`
- `090_EDGE_CASES_AND_WEIRD_TESTS.md`
