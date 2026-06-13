# Commit Push Readiness Template

Use this only after the decision gate is GO or GO_WITH_WARNINGS and Alberto explicitly wants publication commands.

## Rules

- Use `git --no-pager` for long output.
- Run tests, validators, and diff checks first.
- Check Git status with `git status --porcelain=v1` before staging.
- Block unexpected paths with an explicit `$allowedPaths` list.
- Stage only intended paths.
- Run `git diff --cached --check` after staging and before commit.
- If cached diff check fails, stop publication, read the real output, fix only reported files, back them up before automatic edits, restage only those files, and rerun `git diff --cached --check` plus `git diff --check`.
- Use direct Git diagnostics for fragile gates: `git status --short`, `git status -sb`, `git diff --cached --name-status`, `git diff --cached --check`, `git diff --name-status`, `git diff --check`.
- Commit only after gates pass.
- Push only after commit succeeds.
- Direct push to `main` is allowed when Alberto requested publication and all local gates pass.
- Use branch plus PR as an alternative when the repository is protected or Alberto asks for review.
- Verify final status, log, and remote.
- Use `$ErrorActionPreference = "Stop"`.
- Prefer `.ps1` execution for long or critical flows.
- Avoid long pasted here-strings for Markdown reports; build `$Lines` arrays and write with `Set-Content` or UTF-8 helpers.
- If a multiline block is still provided for paste, start it with `Clear-Host` and end with `# terminatore copia-incolla` followed by one real blank final line.
- Treat CRLF/LF notices as attention only when `git --no-pager diff --check` exits successfully.

## Generic PowerShell Template

```powershell
Clear-Host
$ErrorActionPreference = "Stop"

$RepoRoot = (Resolve-Path ".").Path
$Branch = "main"
$CommitMessage = "070) Add codex report intake decision gate skill"
$PathsToAdd = @(
    "CHANGELOG.md",
    "SKILLS_INDEX.md",
    "SKILL_SCORE.md",
    "docs/roadmap.md",
    "as-common-codex-report-intake-decision-gate"
)
$allowedPaths = $PathsToAdd

Set-Location -Path $RepoRoot
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

$statusLines = @(git status --porcelain=v1)
$unexpected = @()
foreach ($line in $statusLines) {
    if ([string]::IsNullOrWhiteSpace($line)) { continue }
    $path = $line.Substring(3).Trim('"') -replace "\\", "/"
    $isAllowed = $false
    foreach ($allowedPath in $allowedPaths) {
        $normalized = $allowedPath.TrimStart(".", "/") -replace "\\", "/"
        if ($normalized.EndsWith("/")) {
            if ($path.StartsWith($normalized)) {
                $isAllowed = $true
                break
            }
        } elseif ($path -eq $normalized -or $path.StartsWith("$normalized/")) {
            $isAllowed = $true
            break
        }
    }
    if (-not $isAllowed) { $unexpected += $line }
}
if ($unexpected.Count -gt 0) {
    throw "Unexpected Git changes:`n$($unexpected -join "`n")"
}

git status --porcelain=v1

git add -- $PathsToAdd
if ($LASTEXITCODE -ne 0) { throw "git add failed." }

git diff --cached --check
if ($LASTEXITCODE -ne 0) { throw "Cached diff check failed." }

git commit -m $CommitMessage
if ($LASTEXITCODE -ne 0) { throw "git commit failed." }

git push origin $Branch
if ($LASTEXITCODE -ne 0) { throw "git push failed." }

git status --short
git --no-pager log --oneline --max-count=5
git remote -v

# terminatore copia-incolla

```

## Readiness Checklist

- Decision gate is GO or GO_WITH_WARNINGS.
- Alberto explicitly requested commit/push.
- Mandatory checks passed.
- Warnings are documented.
- Staged paths are intentional.
- Final status and log are included in the publication report.
