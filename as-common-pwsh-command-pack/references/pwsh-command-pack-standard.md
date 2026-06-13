# PowerShell Command Pack Standard

## Purpose

This standard defines how `as-common-pwsh-command-pack` prepares robust PowerShell command packs for Alberto. The goal is to avoid fragile paste-heavy command lines by generating a complete `.ps1` script that logs execution, creates stable artifacts, keeps the compact report recoverable from Bridge files, and keeps publication actions human-gated.

## Required Launcher

Use this launcher shape:

```powershell
Clear-Host
pwsh -NoProfile -ExecutionPolicy Bypass -File "D:\FG-SAB Dropbox\Alberto Ferrari\ChatGPT_Bridge\AI_Software_Factory\pwsh_command\NNNN-Comando_Eseguito_<nome>.ps1"
# terminatore copia-incolla

```

For long or conditional work, do not ask Alberto to paste a large inline command. Generate a script file and give only the short launcher.

## PowerShell Paste Termination

Every operational PowerShell block intended for copy/paste into PowerShell or Windows Terminal must start with `Clear-Host` and end with the sentinel comment `# terminatore copia-incolla` followed by one real blank final line.

```powershell
Clear-Host
<useful command>
# terminatore copia-incolla

```

For long or critical workflows, write a `.ps1` file and run it with:

```powershell
Clear-Host
pwsh -NoProfile -ExecutionPolicy Bypass -File <script.ps1>
# terminatore copia-incolla

```

Use this terminator by default, including one-line blocks. Do not use `WScript.Shell`, `SendKeys`, or auto-Enter as automatic paste-completion workarounds. `WScript.Shell` is only an explicit fallback for rare cases.

Do not rely on a final `Write-Host ";";` to force execution. It is only a visual marker and does not replace the sentinel terminator.

## Command Wrapper

For pasteable PowerShell payloads, use one wrapper:

```powershell
& {
    # all logic here
}
```

Do not generate separable `if` / `else` blocks for paste-heavy work. For long or critical work, save a real `.ps1` payload and launch it.

## Success/Failure State

Use a controlled state variable:

```powershell
$StepOk = $false
```

Print completion only after all mandatory gates pass:

```powershell
if ($StepOk) {
    Add-Log "=== COMPLETATO ==="
}
```

Do not print success text outside the controlled success path.

## Encoding

Use `.NET` UTF-8 without BOM helpers for generated text. Do not rely on `Set-Content -Encoding utf8NoBOM` for compatibility with older Windows PowerShell hosts.

## Parameters and Empty Strings

Helpers that write logs or files must allow empty content where valid:

```powershell
[AllowNull()]
[AllowEmptyString()]
```

## Native Command Capture

Non-trivial packs should include:

- `Invoke-NativeCapture`;
- `Invoke-NativeStep`;
- `Get-NativeText`.

Capture output and `$LASTEXITCODE` immediately. Never infer success from printed text alone.

For fragile Git diagnostics, use direct commands in the generated script and make the real command visible in logs. Avoid a generic wrapper when diagnosing failures caused by argument passing or Git option ordering. Prefer:

```powershell
git status --short
git status -sb
git diff --cached --name-status
git diff --cached --check
git diff --name-status
git diff --check
```

Save the full output and the exit code for each command. If the purpose is evidence collection, do not stop at the first non-zero exit code unless a later command would be unsafe. Use `git --no-pager` only when the exact direct form is known to work.

## Git Status Parsing

Use `git status --porcelain=v1` for parsing. Do not parse `git status --short` with `.Trim()`, and do not blindly remove the first two characters of each row. Parse status and path separately.

## Allowed Paths Guardrail

When a script modifies, stages, or commits files, define:

```powershell
$allowedPaths = @(
    "path/expected-file-1",
    "path/expected-folder/"
)
```

Block if porcelain status reports paths outside the allow-list.

## Diff Checks

Before relaunching Phase B or before commit/push/PR when files are staged, the cached check is mandatory:

```powershell
git diff --cached --check
```

If it fails:

- do not relaunch Phase B;
- do not commit, push, open a PR, or merge;
- read the real output;
- identify only the files reported by Git;
- back up those files before automatic edits;
- fix only those files;
- stage only those fixed files;
- rerun both checks:

```powershell
git diff --cached --check
git diff --check
```

Proceed only when both checks pass. Use `git --no-pager` for long output when the direct command form has already been verified.

## EOF/Whitespace Cleanup

Use only conservative cleanup on text files explicitly named by `git diff --cached --check`:

- add missing newline at EOF;
- remove extra final blank lines such as `new blank line at EOF`;
- leave exactly one final newline;
- create a backup in the Bridge output folder or another explicit backup folder before automatic edits;
- restage only the files touched by the fix;
- rerun `git diff --cached --check` and `git diff --check`;
- never run cleanup on binary files or broad paths.

Do not use reset, clean, checkout, or broad repository-wide whitespace cleanup for this recovery path.

## Direct Main Push Policy

Alberto decision D3-C applies: direct `git push origin main` is allowed when every local gate passes and the current step allows publication. Do not make PR workflow mandatory for this skill.

## Optional PR Workflow

Document branch + PR as an alternative for protected repositories:

- push branch;
- create/view PR;
- run `gh pr checks`;
- merge only after gates pass;
- fetch and realign local `main`.

## Reset Hard Backup Policy

Before any authorized `git reset --hard` realignment, create a backup branch named:

```text
backup/main-before-YYYYMMDD-HHMMSS
```

## Compact Output and DOCX

Compact Markdown is mandatory. DOCX is useful but non-blocking: if DOCX generation fails, log a warning and continue with Markdown.

For Markdown generated by PowerShell, prefer line arrays and explicit joins. Avoid long pasted here-strings with Markdown, triple backticks, JSON, interpolation, or non-trivial multiline text because a truncated paste can leave PowerShell waiting at `>>`.

```powershell
$Lines = @()
$Lines += "# Titolo"
$Lines += ""
$Lines += "## Sezione"
$Lines += "testo"
Set-Content -Path $File -Value ($Lines -join "`r`n") -Encoding UTF8
```

Here-strings are acceptable only for short controlled text without triple backticks and without truncation risk.

## Repository Location Guard

Before final Git evidence collection, return to the repository:

```powershell
Set-Location -Path $RepoRoot
```

## GitHub CLI Checks

`gh pr checks --watch` exit code `1` for no checks and exit code `8` for pending checks can be controlled warnings only when local gates pass and command output confirms the condition.

## LF/CRLF Warning Policy

LF/CRLF warnings do not block when `git --no-pager diff --check` or `git --no-pager diff --cached --check` exits with code 0. Real diff-check errors still block.

## Standard Functions

Non-trivial packs should include or adapt:

- `Write-Utf8NoBomFile`;
- `Append-Utf8NoBomFile`;
- `Add-Log`;
- `Invoke-NativeCapture`;
- `Invoke-NativeStep`;
- `Get-NativeText`;
- `Assert-CleanWorkingTree`;
- `Write-CompactOutput`.

## Real `.ps1` Payload

The generated payload must be saved as:

```text
NNNN-Comando_Eseguito_<nome>.ps1
```

Then launch that file. Do not save only a narrative description of the command.

## Compact Output Handoff

The `finally` path must try to create `Output_Compatto.md` even when a command fails. Do not write to the OS clipboard automatically by default.

If Alberto explicitly requests clipboard handoff for a file, copy file content with:

```powershell
Clear-Host
Get-Content -Path $File -Raw | Set-Clipboard
# terminatore copia-incolla

```

Never use `Set-Clipboard -Path`.

## Regression/Demo Trial

Validate this skill with demo trials that reproduce the historical bugs documented in `pwsh-known-bugs-regression-tests.md`, including STEP 490 and later command-pack failures.

## Output Roots

Standard Bridge root:

```text
D:\FG-SAB Dropbox\Alberto Ferrari\ChatGPT_Bridge
```

AI Software Factory command pack root:

```text
D:\FG-SAB Dropbox\Alberto Ferrari\ChatGPT_Bridge\AI_Software_Factory\pwsh_command
```

Temporary files created by generated scripts must stay inside the command pack output folder or another explicit ignored/temp location.

## Bridge Retrieval and LAST Policy

When ChatGPT must read an output/log/report under the Bridge, try the Dropbox/Bridge connector before asking Alberto to paste content.

Operational order:

1. Search the exact numbered/progressive file first, for example `0910A-Output_Diagnostica_Diretta_Git_Cached_Diff.txt`.
2. Only if the progressive file is not found, try `LAST-Output_Compatto.md` or `LAST-Output_Completo.txt`.
3. If `LAST` exists but step, name, timestamp, or server_modified is stale or incoherent, declare it and do not use `LAST` as evidence.
4. If the Bridge is unavailable or Dropbox has not synced/indexed the file, ask only for the minimum excerpt, such as `## Cached diff check`, `## Cached diff names`, `## Git status short`, or the exact progressive path.

Do not ask for the whole report by default.

## Required Artifacts

Every generated pack must create the numbered artifacts:

```text
NNNN-Richiesta_Generazione_<nome>.txt
NNNN-Comando_Eseguito_<nome>.ps1
NNNN-Output_Completo_<nome>.txt
NNNN-Output_Compatto_<nome>.md
NNNN-Output_Compatto_<nome>.docx
```

Create matching `LAST-*` artifacts only when Alberto explicitly requests compatibility pointers:

```text
LAST-Richiesta_Generazione.txt
LAST-Comando_Eseguito.ps1
LAST-Output_Completo.txt
LAST-Output_Compatto.md
LAST-Output_Compatto.docx
```

If `LAST-Output_Compatto.md` is explicitly requested, it must remain readable from the Bridge. If Alberto explicitly requests clipboard handoff, copy its content with `Get-Content -Path $File -Raw | Set-Clipboard`; never use `Set-Clipboard -Path`. If clipboard access fails, the script must log a warning and still write the file.

The numbered/progressive artifact is the authoritative retrieval target. `LAST-*` is only a convenience pointer and can be stale after retries, partial reruns, or Dropbox sync delays.

## Script Structure

A robust script must include:

- `#Requires -Version 7.0`;
- `Set-StrictMode -Version Latest`;
- `$ErrorActionPreference = 'Stop'`;
- explicit UTF-8 without BOM writes;
- `try/catch/finally` around the full run;
- wrapper functions for logging and native commands;
- `$LASTEXITCODE` captured immediately after native commands;
- compact Markdown generation;
- DOCX generation or a documented fallback if DOCX cannot be produced;
- optional final artifact copy to `LAST-*` names only when explicitly requested;
- a non-zero process exit on failed required gates.

Use splatting for commands with many named parameters. Use `Tee-Object` or explicit logging wrappers when console output and file output both matter. Avoid relying only on `Start-Transcript`: transcripts are useful as a supplemental record but can miss or format streams in ways that are less suitable than explicit command logs.

## Phase Model

Use phases whenever the pack contains publication or state-changing steps.

- FASE A: local verification, read-only checks, syntax checks, tests, `git --no-pager status --short`, `git --no-pager diff --check`, health checks, and report generation.
- FASE B: commit, push, PR creation, or PR checks. This phase is human-gated and must stop if FASE A fails.
- FASE C: merge, release, deploy, restart, publication, or cleanup that affects external state. This phase is human-gated and must stop if FASE A or FASE B gates fail.

Publication must not proceed when tests, verify, health check, or guardrails fail. Do not hide failures behind warnings. The known `gh pr checks --watch` cases with `no checks reported`, exit code `1`, or pending exit code `8` can be reported as controlled warnings only when every other required local gate has passed.

## Git, Codex, and ASF Guardrails

- Use branch and working-tree checks before any Git work.
- Use `git --no-pager` for long Git output.
- Never run `git reset --hard`, `git clean`, force push, merge, deploy, release, or destructive commands unless the current prompt explicitly authorizes that action and the generated pack keeps it in a separate human-gated phase.
- Do not use `setx PATH`; prefer process-local environment variables or explicit executable paths.
- Keep sensitive values out of request files, logs, compact outputs, DOCX outputs, and clipboard output.
- For Codex/ASF command packs, keep target repository behavior read-only unless Alberto explicitly asks for a later write-controlled phase.
- If a gate fails, produce the compact report and stop before publication.

## Encoding and Line Endings

PowerShell 6+ defaults are centered on UTF-8 without BOM for many text outputs, but scripts should still write explicitly with UTF-8 without BOM to avoid Windows ambiguity. Recommend this `.gitattributes` baseline when line-ending policy is relevant:

```gitattributes
* text=auto eol=lf
*.bat text eol=crlf
*.cmd text eol=crlf
*.ps1 text eol=crlf
```

Use `git diff --check` before publication to detect whitespace errors.

## Technical Principles Integrated

- Microsoft documents an 8191 character limit for `cmd.exe` command-line strings; use `.ps1` files instead of long pasted commands.
- `CreateProcessW` documents a 32767 character maximum command line, including the terminating null; generated scripts reduce exposure to this limit too.
- PowerShell character encoding docs explain the UTF-8 without BOM behavior in PowerShell 6+; generated text should be explicit.
- PowerShell error-handling docs support `try/catch/finally`, `$ErrorActionPreference = 'Stop'`, and checking automatic variables such as `$LASTEXITCODE` for native commands.
- PowerShell preference variable docs cover `$PSNativeCommandUseErrorActionPreference`; enable it where supported, while still checking `$LASTEXITCODE` explicitly.
- PowerShell redirection docs cover streams, `Out-File`, `Tee-Object`, width, and UTF-8 output; prefer explicit wrappers for stable logs.
- Splatting docs support readable commands with many parameters.
- `Set-StrictMode` catches uninitialized variables and other coding issues early; use it in generated scripts.
- PSScriptAnalyzer is the preferred static checker when available; use warning/error severity and report absence as a warning, not a failure.
- Git attributes and `git diff --check` protect line endings and whitespace before publication.
- GitHub CLI `gh pr checks` documents `--watch`, JSON fields, and exit code behavior; handle pending checks and no-check warnings conservatively.
- OpenAI Codex skill examples use `SKILL.md` YAML frontmatter with `name` and `description`, and optional `references/`, `scripts/`, `examples/`, or assets for progressive disclosure.

## Primary References

- Microsoft command line limit: https://learn.microsoft.com/en-us/troubleshoot/windows-client/shell-experience/command-line-string-limitation
- Microsoft CreateProcessW: https://learn.microsoft.com/en-us/windows/win32/api/processthreadsapi/nf-processthreadsapi-createprocessw
- PowerShell character encoding: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_character_encoding
- PowerShell Start-Transcript: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.host/start-transcript
- PowerShell try/catch/finally: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_try_catch_finally
- PowerShell automatic variables: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_automatic_variables
- PowerShell preference variables: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_preference_variables
- PowerShell redirection: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_redirection
- PowerShell splatting: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_splatting
- PowerShell Set-StrictMode: https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/set-strictmode
- PSScriptAnalyzer overview: https://learn.microsoft.com/en-us/powershell/utility-modules/psscriptanalyzer/overview
- Git attributes: https://git-scm.com/docs/gitattributes
- Git diff: https://git-scm.com/docs/git-diff
- GitHub CLI PR checks: https://cli.github.com/manual/gh_pr_checks
- GitHub CLI exit codes: https://cli.github.com/manual/gh_help_exit-codes
- OpenAI Codex skill creator sample: https://github.com/openai/codex/blob/main/codex-rs/skills/src/assets/samples/skill-creator/SKILL.md
- OpenAI skills catalog: https://github.com/openai/skills
