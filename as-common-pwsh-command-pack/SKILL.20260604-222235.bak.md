---
name: as-common-pwsh-command-pack
description: "Generate safe logged PowerShell command packs for Alberto with stop-on-error, verification/publication separation, compact output, clipboard copy, Dropbox ChatGPT_Bridge copies, and LAST files."
---

# as-common-pwsh-command-pack

## Purpose

Use this skill whenever Alberto asks for PowerShell commands for repository work, tests, verification, Git operations, GitHub PR operations, deployment checks, Codex/ChatGPT automation, or output capture for ChatGPT.

The goal is to generate one direct PowerShell block that Alberto can copy and run quickly, while preserving safety, traceability, and a compact output suitable for ChatGPT.

## Core rule

When proposing PowerShell commands:

1. Generate a direct PowerShell block, ready to copy and paste.
2. Include stop-on-error behavior for every mandatory step.
3. Separate verification from publication whenever publication exists.
4. Save command request, command executed, full output, compact output, and LAST files.
5. Copy the compact output to the clipboard.
6. Optionally mirror outputs to Alberto's Dropbox ChatGPT bridge.
7. Never continue to commit, push, create a PR, merge, deploy, or publish if local verification failed.

## Default bridge root

For Alberto, the default Dropbox bridge root is:

```text
D:\FG-SAB Dropbox\Alberto Ferrari\ChatGPT_Bridge
```

Default repository-local command directory:

```text
<repo-root>\pwsh_command
```

Default bridge command directory:

```text
D:\FG-SAB Dropbox\Alberto Ferrari\ChatGPT_Bridge\<ProjectKey>\pwsh_command
```

The `<ProjectKey>` should normally be the repository folder name, sanitized for filesystem use. Examples:

```text
AI_Software_Factory
Family_Photo_Organizer
Mansionario_Vivo
AggloDetect
```

## Numbering

Use a 4-digit command pack number:

```text
0001
0002
0003
```

If the previous number is unknown, use `0001` and explicitly tell Alberto:

```text
Numero progressivo assunto: 0001. Se esiste già, incrementarlo prima dell'esecuzione.
```

## File naming standard

For each command pack, generate these numbered files:

```text
<NNNN>-Richiesta_Generazione_<pack_name>.txt
<NNNN>-Comando_Eseguito_<pack_name>.ps1
<NNNN>-Output_Completo_<pack_name>.txt
<NNNN>-Output_Compatto_<pack_name>.md
<NNNN>-Output_Compatto_<pack_name>.docx
```

Also update these fixed LAST files:

```text
LAST-Richiesta_Generazione.txt
LAST-Comando_Eseguito.ps1
LAST-Output_Completo.txt
LAST-Output_Compatto.md
LAST-Output_Compatto.docx
```

The `.md` file is for local readability and clipboard. The `.docx` file is for Dropbox/ChatGPT bridge compatibility.

## Important Dropbox note

When Dropbox bridge is enabled, always generate `LAST-Output_Compatto.docx` in addition to `.md`/`.txt`, because the ChatGPT Dropbox app with sync is documented primarily for document types such as `.pdf`, `.docx`, `.pptx`, and `.xlsx`.

Do not rely on `.txt`, `.md`, or `.ps1` as the only files ChatGPT will be able to index through Dropbox.

## Mandatory phases

### Verification only

Use this phase naming:

```text
FASE A - Verifica locale
```

### Verification plus publication

Use this phase naming:

```text
FASE A - Verifica locale
FASE B - Pubblicazione
FASE C - Verifica finale
```

Publication means any command such as:

```text
git add
git commit
git push
gh pr create
gh pr merge
git pull origin main/master
deployment commands
```

FASE B must not run if FASE A fails.

## Mandatory safety rules

1. Start long scripts with:

```powershell
Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"
```

2. Use `git --no-pager` for long Git outputs:

```powershell
git --no-pager diff --stat
git --no-pager diff --check
git --no-pager log --oneline --max-count=10
```

3. Never use `setx PATH`.

4. Never use destructive commands unless Alberto explicitly asked and the command is isolated and explained:

```text
Remove-Item
del
rmdir
git reset --hard
git clean -fd
drop database
```

5. For `gh pr checks --watch`, handle the "no checks reported" or unavailable checks case without creating a large red error, while still preserving the exit code in the full output.

6. For multiline PowerShell blocks given to Alberto, keep a final blank line and do not add a useless `Write-Host ""` just to force execution.

7. For single-line PowerShell commands given to Alberto, add a second harmless line:

```powershell
Write-Host ""
```

8. If the expected branch is known, check it before running modifications or publication.

9. If a clean working tree is required and `git status --short` is not empty, stop and ask for review instead of continuing.

10. Do not put secrets, tokens, passwords, `.env`, database dumps, customer data, accounting exports, or personal data into `pwsh_command` or `ChatGPT_Bridge`.

## Compact output format

The compact output must be easy to paste into ChatGPT and must contain:

```text
=== OUTPUT COMPATTO PER CHATGPT ===

COMMAND PACK:
<NNNN> - <pack_name>

REPOSITORY:
<repo_path>

BRIDGE:
<bridge_path_or_disabled>

BRANCH INIZIALE:
<branch_initial>

BRANCH FINALE:
<branch_final>

STATO:
OK / KO

FASE COMPLETATA:
<phase>

TEST:
<summary>

VERIFY:
<summary>

GIT STATUS FINALE:
<git status --short>

ULTIMI COMMIT:
<git --no-pager log --oneline --max-count=5>

FILE GENERATI:
<important files>

NOTE / ATTENZIONI:
<warnings>

PROSSIMO STEP CONSIGLIATO:
<next step>
```

At the end of the PowerShell block, always print the path to the compact output and print the compact output itself:

```powershell
Write-Host ""
Write-Host "=== COPIA IN CHATGPT IL CONTENUTO QUI SOTTO ==="
Write-Host ""
Get-Content $OutputCompatto -Raw
```

Also copy it to the clipboard:

```powershell
Get-Content $OutputCompatto -Raw | Set-Clipboard
```

## Required script structure

When generating a command pack, the PowerShell block should follow this structure:

```powershell
Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$RepoPath = "<repo path>"
$PackNumber = "0001"
$PackName = "<short_pack_name>"
$DropboxBridgeRoot = "D:\FG-SAB Dropbox\Alberto Ferrari\ChatGPT_Bridge"
$EnableDropboxBridge = $true

Set-Location $RepoPath

# derive paths
# create folders
# initialize files
# write request file
# define Invoke-LoggedStep
# define New-SimpleDocxFromText if .docx is required
# define Update-LastFiles
# run FASE A verification
# run FASE B publication only if needed and only after FASE A passed
# run FASE C final verification
# write compact output
# copy compact output to clipboard
# mirror to Dropbox bridge
# print compact output
```

## Required logging wrapper

Use a logging wrapper equivalent to this:

```powershell
function Invoke-LoggedStep {
    param(
        [Parameter(Mandatory = $true)]
        [string]$Title,

        [Parameter(Mandatory = $true)]
        [scriptblock]$Command,

        [bool]$StopOnError = $true
    )

    Write-Host ""
    Write-Host "=== $Title ==="

    "=== $Title ===" | Tee-Object -FilePath $OutputCompleto -Append

    try {
        $global:LASTEXITCODE = 0
        & $Command 2>&1 | Tee-Object -FilePath $OutputCompleto -Append
        $exitCode = $LASTEXITCODE

        if ($null -eq $exitCode) {
            $exitCode = 0
        }

        "EXIT_CODE: $exitCode" | Tee-Object -FilePath $OutputCompleto -Append

        if ($StopOnError -and $exitCode -ne 0) {
            throw "Step fallito: $Title - Exit code: $exitCode"
        }
    }
    catch {
        "ECCEZIONE: $($_.Exception.Message)" | Tee-Object -FilePath $OutputCompleto -Append
        if ($StopOnError) {
            throw
        }
    }
}
```

## DOCX generation rule

When Dropbox bridge is enabled, generate a real `.docx` for compact output.

Preferred approach: use Python standard library to create a minimal OpenXML DOCX from the compact Markdown/text. Do not fake a `.docx` by renaming a `.txt`.

If Python is unavailable, continue with `.md`/`.txt`, copy compact output to clipboard, and warn Alberto that Dropbox may not index the compact file.

## Response style to Alberto

When providing a PowerShell block:

1. Briefly state pack number, pack name, repository, whether publication is included.
2. Give the PowerShell block.
3. State what file Alberto should paste back into ChatGPT.
4. If Dropbox bridge is enabled, state the expected bridge path and the `LAST-Output_Compatto.docx` file.

Do not bury the actual command block under long explanations.
