# Sample Verification Gate

Project: Codex_Skills

Step: 060

Repository: `C:\Users\alberto.ferrari\.agents\skills`

## Risk Profile

| Area | Risk | Reason |
|---|---|---|
| Skill catalog | medium | New skill must be valid and indexed. |
| Markdown content | low | No runtime code change, but docs must be coherent. |
| Validator | high | Catalog quality depends on validator PASS. |
| Git state | high | Publication must not happen from an unexpected state. |

## Mandatory Checks

| Check | Command | Expected result | Blocks publication |
|---|---|---|---|
| Unit tests | `python validators/test_check_agent_skills.py` | All tests pass | Yes |
| Skill validator | `python validators/check_agent_skills.py` | PASS, 0 errors, 0 warnings | Yes |
| Catalog regeneration | `python validators/check_agent_skills.py --write-index --write-score` | Catalogs updated | Yes |
| Final validator | `python validators/check_agent_skills.py` | PASS, 0 errors, 0 warnings | Yes |
| Diff check | `git --no-pager diff --check` | No errors | Yes |
| Final status | `git status --short` | Expected files only | Yes |

## Optional Checks

| Check | Command | Expected result | Notes |
|---|---|---|---|
| Diff stat | `git --no-pager diff --stat` | Reviewable scope | Required for final report, not a quality test by itself. |
| Targeted diff | `git --no-pager diff -- CHANGELOG.md SKILLS_INDEX.md SKILL_SCORE.md docs/roadmap.md as-common-verification-gate-test-eval-pack/SKILL.md` | Expected changes | Used for human review. |

## Stop Policy

- Stop on failed validator or test command.
- Stop on real `git diff --check` errors.
- Do not commit, push, create PR, merge, or deploy in this step.
- If a check is not run, report it with the reason.

## Final Go/No-Go Report

Decision: GO for local review only when all mandatory checks pass.

Publication: NO-GO unless Alberto explicitly requests commit, push, PR, merge, or deploy in a later step.
