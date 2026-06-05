# 100 Skill Release Checklist

## A. Preflight

- [ ] Confirm root path is `C:\Users\alberto.ferrari\.agents\skills`.
- [ ] Confirm branch is `main`.
- [ ] Confirm `git status --porcelain=v1` is clean before edits.
- [ ] Confirm remote is `origin`.
- [ ] Confirm latest commits match expected step history.

## B. Context review

- [ ] Identify active user step.
- [ ] Identify AGENTS.md and repository constraints.
- [ ] Identify applicable skills.
- [ ] Resolve commit/push policy.
- [ ] Record open questions before edits.

## C. Skill authoring

- [ ] Use lowercase kebab-case folder name.
- [ ] Keep `SKILL.md` compact.
- [ ] Put long details in `references/`, `examples/`, `docs/`, or `templates/`.
- [ ] Avoid changing existing skill behavior outside scope.

## D. Files expected

- [ ] List expected new files.
- [ ] List expected modified files.
- [ ] Confirm no unexpected files.
- [ ] Confirm no backup/temp files in active skills.

## E. Validator

- [ ] Run `python validators/test_check_agent_skills.py`.
- [ ] Run `python validators/check_agent_skills.py`.
- [ ] Confirm 0 errors and 0 warnings.

## F. Smoke trial

- [ ] Run targeted smoke trial for major skill changes.
- [ ] Run `python validators/smoke_trial_cases.py` when present.
- [ ] Document negative cases when relevant.

## G. Catalog update

- [ ] Run `python validators/check_agent_skills.py --write-index --write-score`.
- [ ] Confirm `SKILLS_INDEX.md` updated.
- [ ] Confirm `SKILL_SCORE.md` updated.

## H. Changelog update

- [ ] Add current step section to `CHANGELOG.md`.
- [ ] Summarize documents, templates, checker, catalog update, and remaining notes.

## I. Diff check

- [ ] Run `git --no-pager diff --check`.
- [ ] Treat LF/CRLF notices as non-blocking only if exit code is 0.

## J. Staged diff check

- [ ] Run `git add .`.
- [ ] Run `git --no-pager diff --cached --check`.
- [ ] Stop if staged diff check fails.

## K. Commit/push

- [ ] Commit with step number and concise message.
- [ ] Push direct to `main` only after all local gates pass.
- [ ] Use PR workflow instead if repository protection blocks direct push.

## L. Final status

- [ ] Run `git status --short`.
- [ ] Run `git --no-pager log --oneline --max-count=8`.
- [ ] Run `git remote -v`.

## M. Handoff

- [ ] State next recommended step.
- [ ] Include risks and not-run checks.
- [ ] Include final standard line.

## Base commands

```powershell
python validators/test_check_agent_skills.py
python validators/check_agent_skills.py
python validators/check_agent_skills.py --write-index --write-score
if (Test-Path "validators/smoke_trial_cases.py") { python validators/smoke_trial_cases.py }
git --no-pager diff --check
git status --porcelain=v1
git add .
git --no-pager diff --cached --check
git commit -m "<step>) <message>"
git push origin main
git status --short
git --no-pager log --oneline --max-count=8
Write-Host "Linea fake - se resta in attesa, premere Enter qui"
```
