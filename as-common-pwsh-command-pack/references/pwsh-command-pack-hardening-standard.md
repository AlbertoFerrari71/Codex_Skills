# PowerShell Command Pack Hardening Standard

This standard records the hardening audit for `as-common-pwsh-command-pack`.

| N. | Rule | Status before | Action taken | Final location |
|-:|---|---|---|---|
| 1 | Wrapper unico `& { ... }` | Incomplete | Added as required wrapper model for paste payloads and template logic. | `SKILL.md`, `pwsh-command-pack-template.ps1` |
| 2 | Nessun falso messaggio di successo | Partial | Added controlled `$StepOk` success state. | `pwsh-command-pack-template.ps1` |
| 3 | UTF-8 senza BOM via `.NET` | Partial | Standardized `.NET` write/append helpers. | `pwsh-command-pack-template.ps1` |
| 4 | Stringhe vuote nei parametri | Partial | Added `[AllowEmptyString()]` and `[AllowNull()]` where content can be empty. | `pwsh-command-pack-template.ps1` |
| 5 | Parsing Git robusto con `git status --porcelain=v1` | Missing | Added porcelain guidance and parser guardrail. | `pwsh-command-pack-standard.md`, `pwsh-command-pack-template.ps1` |
| 6 | Guardrail file attesi con `$allowedPaths` | Missing | Added allowed-path guardrail model. | `pwsh-command-pack-template.ps1` |
| 7 | `git --no-pager diff --cached --check` obbligatorio prima del commit | Missing | Added staged diff check requirement. | `pwsh-command-pack-standard.md`, `pwsh-command-pack-template.ps1`, `commit-push-readiness-template.md` |
| 8 | Routine fix EOF/whitespace | Missing | Added conservative text-only cleanup helper. | `pwsh-command-pack-template.ps1` |
| 9 | Push diretto su main consentito se gate locale passa | Incomplete | Documented Alberto D3-C policy. | `pwsh-command-pack-standard.md`, `pwsh-git-pr-workflow-standard.md` |
| 10 | Workflow PR standard come alternativa documentata, non default obbligatorio | Incomplete | Added optional PR workflow reference. | `pwsh-git-pr-workflow-standard.md` |
| 11 | Backup prima di `reset --hard` | Partial | Added backup branch rule. | `pwsh-command-pack-standard.md`, `pwsh-git-pr-workflow-standard.md` |
| 12 | DOCX compatto non bloccante | Partial | Made DOCX guidance non-blocking. | `pwsh-command-pack-standard.md`, `pwsh-command-pack-template.ps1` |
| 13 | Temp DOCX fuori Dropbox | Present | Confirmed temp path uses `$env:TEMP` / system temp. | `pwsh-command-pack-template.ps1` |
| 14 | `Write-CompactOutput` deve tornare nel repo con `Set-Location -Path $RepoRoot` | Missing | Added repo-location guard to compact output routine. | `pwsh-command-pack-template.ps1` |
| 15 | `gh pr checks` exit code 8 da gestire come pending/controllato | Missing | Added exit code 8 controlled handling. | `pwsh-command-pack-template.ps1`, `pwsh-git-pr-workflow-standard.md` |
| 16 | Warning LF/CRLF non bloccanti se exit code e' 0 | Present | Preserved and restated. | `pwsh-command-pack-standard.md`, linked workflow docs |
| 17 | Funzioni standard obbligatorie per command pack non banali | Missing | Added required helper list. | `SKILL.md`, `pwsh-command-pack-standard.md`, `pwsh-command-pack-template.ps1` |
| 18 | Payload `.ps1` reale salvato e poi lanciato | Partial | Documented hard requirement. | `SKILL.md`, `pwsh-command-pack-template.ps1` |
| 19 | Output compatto sempre su file; clipboard solo esplicita | Updated | Ensure compact output is written in `finally`; if clipboard copy is explicitly requested, use `Get-Content -Path $File -Raw | Set-Clipboard`. | `pwsh-command-pack-template.ps1` |
| 20 | Demo trial storica che riproduce bug reali dello STEP 490 e successivi | Missing | Added regression-test reference. | `pwsh-known-bugs-regression-tests.md` |
| 21 | Bridge progressivo prima di `LAST-*` | Missing | Added retrieval order and stale LAST policy. | `SKILL.md`, `pwsh-command-pack-standard.md`, `codex-command-pack-standard.md` |
| 22 | Diagnostiche Git dirette per gate critici | Partial | Added direct-command diagnostic rule and exit-code capture. | `SKILL.md`, `pwsh-command-pack-standard.md`, `as-common-powershell-git-safe-flow/SKILL.md` |
| 23 | No here-string Markdown fragili | Partial | Added line-array Markdown generation rule for pasted/generated reports. | `SKILL.md`, `pwsh-command-pack-standard.md`, `as-common-powershell-git-safe-flow/SKILL.md` |
| 24 | Stop su `git diff --cached --check` prima di Phase B | Partial | Added recovery sequence: read output, fix only reported files, restage, rerun cached and unstaged checks. | `SKILL.md`, `pwsh-command-pack-standard.md`, `pwsh-known-bugs-regression-tests.md` |
| 25 | Fix mirato `new blank line at EOF` | Partial | Added backup plus scoped EOF blank-line recovery rule. | `SKILL.md`, `pwsh-command-pack-standard.md`, `pwsh-known-bugs-regression-tests.md` |

## Final Rule

Use direct `git push origin main` only when local gates pass and Alberto's step allows publication. If the remote blocks main, fall back to the documented branch + PR workflow.
