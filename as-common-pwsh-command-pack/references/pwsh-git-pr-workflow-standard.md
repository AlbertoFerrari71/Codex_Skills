# PowerShell Git PR Workflow Standard

This reference documents publication choices for generated PowerShell command packs.

## Direct Main Push Policy

Alberto decision D3-C applies:

- direct `git push origin main` is allowed when local gates pass;
- do not make branch + PR the default mandatory workflow for this skill;
- if the remote blocks direct push, stop and use the optional PR workflow.

Mandatory local gates before direct push:

```powershell
Clear-Host
python validators/test_check_agent_skills.py
python validators/check_agent_skills.py
git --no-pager diff --check
git diff --cached --check
# terminatore copia-incolla

```

Use project-specific tests in place of validator commands when working outside this repository.

If `git diff --cached --check` fails, stop publication and do not rerun the push/PR phase. Read the real output, fix only the files named by Git, create a backup before automatic edits, restage only the fixed files, then rerun:

```powershell
Clear-Host
git diff --cached --check
git diff --check
# terminatore copia-incolla

```

Resume only after both pass. For `new blank line at EOF`, remove extra final blank lines only from the reported files and leave exactly one final newline.

## Optional PR Workflow

Use this alternative for protected repositories or when Alberto asks for branch review:

1. Create or switch to a dedicated branch.
2. Run local gates.
3. Push the branch.
4. Create or view the PR.
5. Run `gh pr checks --watch`.
6. Merge only after checks and local gates pass.
7. Fetch and realign local `main`.

## GitHub CLI Checks

`gh pr checks --watch` can return:

- exit code `1` with no checks reported;
- exit code `8` while checks are pending.

Treat those as controlled warnings only when all local mandatory gates pass and the output text confirms the pending/no-check condition.

## Fallback If Direct Push Is Blocked

If `git push origin main` is rejected by branch protection:

- do not force push;
- create a branch;
- push the branch;
- open or update a PR;
- report the fallback clearly.

## Backup Before Reset Hard

If a local `main` realignment requires `git reset --hard`, first create a backup branch:

```powershell
Clear-Host
$Stamp = Get-Date -Format "yyyyMMdd-HHmmss"
git branch "backup/main-before-$Stamp"
git reset --hard origin/main
# terminatore copia-incolla

```

Only use this when Alberto explicitly authorizes the reset path.
