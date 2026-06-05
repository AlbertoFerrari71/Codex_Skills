# Sample NO-GO Corrective Prompt

Use this when a report lacks required verification, shows unexpected files, or did not regenerate catalogs.

```markdown
# Corrective Codex Prompt

## Situation

The final report cannot be accepted yet. The intake gate found missing verification, unexpected files, and stale generated catalogs.

## What passed

- Branch was reported as `main`.
- The requested skill file appears to exist.

## What failed or is missing

- Tests were not listed with exact commands.
- Git status includes unexpected files.
- `SKILLS_INDEX.md` and `SKILL_SCORE.md` were not regenerated after the new skill.

## Exact files to inspect

- `SKILLS_INDEX.md`
- `SKILL_SCORE.md`
- `<unexpected-file>`
- `<new-skill-folder>/SKILL.md`

## Constraints

- Do not commit.
- Do not push.
- Do not create a PR.
- Do not delete or revert files without explicit approval.
- Keep changes limited to the requested step.

## Required commands

- `python validators/test_check_agent_skills.py`
- `python validators/check_agent_skills.py`
- `python validators/check_agent_skills.py --write-index --write-score`
- `python validators/check_agent_skills.py`
- `git --no-pager diff --check`
- `git status --short`
- `git --no-pager diff --stat`

## Expected final report

Report exact commands, results, warnings, not-run checks, changed files, final Git status, and whether the corrected gate is PASS or still blocked.

## Do not commit/push

Stop after the corrective report.
```
