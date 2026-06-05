# Commit Push Readiness Template

Use this only after the decision gate is GO or GO_WITH_WARNINGS and Alberto explicitly wants publication commands.

## Rules

- Use `git --no-pager` for long output.
- Run tests, validators, and diff checks first.
- Check Git status before staging.
- Stage only intended paths.
- Commit only after gates pass.
- Push only after commit succeeds.
- Verify final status, log, and remote.
- Use `$ErrorActionPreference = "Stop"`.
- End multiline PowerShell blocks with a real executable final line.
- Treat CRLF/LF notices as attention only when `git --no-pager diff --check` exits successfully.

## Generic PowerShell Template

```powershell
$ErrorActionPreference = "Stop"

$Branch = "main"
$CommitMessage = "070) Add codex report intake decision gate skill"
$PathsToAdd = @(
    "CHANGELOG.md",
    "SKILLS_INDEX.md",
    "SKILL_SCORE.md",
    "docs/roadmap.md",
    "as-common-codex-report-intake-decision-gate"
)

$currentBranch = git --no-pager branch --show-current
if ($currentBranch -ne $Branch) {
    throw "Unexpected branch: $currentBranch"
}

python validators/test_check_agent_skills.py
if ($LASTEXITCODE -ne 0) { throw "Validator tests failed." }

python validators/check_agent_skills.py
if ($LASTEXITCODE -ne 0) { throw "Skill validator failed." }

python validators/check_agent_skills.py --write-index --write-score
if ($LASTEXITCODE -ne 0) { throw "Catalog regeneration failed." }

python validators/check_agent_skills.py
if ($LASTEXITCODE -ne 0) { throw "Final skill validator failed." }

git --no-pager diff --check
if ($LASTEXITCODE -ne 0) { throw "Git diff check failed." }

git status --short

git add -- $PathsToAdd
if ($LASTEXITCODE -ne 0) { throw "git add failed." }

git commit -m $CommitMessage
if ($LASTEXITCODE -ne 0) { throw "git commit failed." }

git push origin $Branch
if ($LASTEXITCODE -ne 0) { throw "git push failed." }

git status --short
git --no-pager log --oneline --max-count=5
git remote -v

Write-Host ""
```

## Readiness Checklist

- Decision gate is GO or GO_WITH_WARNINGS.
- Alberto explicitly requested commit/push.
- Mandatory checks passed.
- Warnings are documented.
- Staged paths are intentional.
- Final status and log are included in the publication report.
