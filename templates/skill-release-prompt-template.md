# Skill Release Prompt Template

## Step name

`<step-number>) <step-title>`

## Objective

Describe the skill release objective, expected outcome, and publication policy.

## Context

- Repository: `AlbertoFerrari71/Codex_Skills`
- Branch: `main`
- Skill or workflow involved: `<skill-name-or-doc-area>`
- Prior step: `<commit-or-step>`

## Known commits

- `<hash> <message>`

## Preflight

```powershell
Clear-Host
pwd
git --no-pager branch --show-current
git status --porcelain=v1
git --no-pager log --oneline --max-count=10
git remote -v
python validators/test_check_agent_skills.py
python validators/check_agent_skills.py
python validators/check_agent_skills.py --write-index --write-score
python validators/check_agent_skills.py
if (Test-Path "validators/smoke_trial_cases.py") { python validators/smoke_trial_cases.py }
# terminatore copia-incolla

```

## Files to create/modify

- `<path>`
- `<path>`

## Validation commands

```powershell
Clear-Host
python validators/test_check_agent_skills.py
python validators/check_agent_skills.py
python validators/check_agent_skills.py --write-index --write-score
python validators/check_agent_skills.py
if (Test-Path "validators/smoke_trial_cases.py") { python validators/smoke_trial_cases.py }
if (Test-Path "validators/release_workflow_check.py") { python validators/release_workflow_check.py }
git --no-pager diff --check
git status --porcelain=v1
git --no-pager diff --stat
# terminatore copia-incolla

```

## Smoke trial requirements

- Define at least one happy path.
- Define at least one negative or borderline case.
- Use temporary directories for destructive or invalid cases.
- Do not modify real project state during negative tests.

## Catalog update

Run:

```powershell
Clear-Host
python validators/check_agent_skills.py --write-index --write-score
# terminatore copia-incolla

```

## Changelog update

Add:

```markdown
## <step-number>) <step-title>

- release workflow documented;
- validator/catalog update;
- tests and smoke gates executed.
```

## Commit/push policy D3-C

Direct `git push origin main` is allowed only if all mandatory local gates pass and the current step authorizes publication. Use branch plus PR if remote protection rejects direct push or Alberto asks for review.

```powershell
Clear-Host
git add .
git --no-pager diff --cached --check
git commit -m "<step-number>) <message>"
git push origin main
git status --short
git --no-pager log --oneline --max-count=10
git remote -v
# terminatore copia-incolla

```

## Final report format

A. Step executed

B. Status

C. Branch

D. Files created/modified

E. Release workflow output

F. Tests executed

G. Commit/push

H. Git status final

I. Risks / attention points

J. Next recommended step

K. Final standard line
