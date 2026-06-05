# PowerShell Command Pack Standard

## Purpose

This standard defines how `as-common-pwsh-command-pack` prepares robust PowerShell command packs for Alberto. The goal is to avoid fragile paste-heavy command lines by generating a complete `.ps1` script that logs execution, creates stable artifacts, copies the compact report to the clipboard, and keeps publication actions human-gated.

## Required Launcher

Use this launcher shape:

```powershell
pwsh -NoProfile -ExecutionPolicy Bypass -File "D:\FG-SAB Dropbox\Alberto Ferrari\ChatGPT_Bridge\AI_Software_Factory\pwsh_command\NNNN-Comando_Eseguito_<nome>.ps1"
```

For long or conditional work, do not ask Alberto to paste a large inline command. Generate a script file and give only the short launcher.

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

## Required Artifacts

Every generated pack must create the numbered artifacts:

```text
NNNN-Richiesta_Generazione_<nome>.txt
NNNN-Comando_Eseguito_<nome>.ps1
NNNN-Output_Completo_<nome>.txt
NNNN-Output_Compatto_<nome>.md
NNNN-Output_Compatto_<nome>.docx
```

And the matching LAST artifacts:

```text
LAST-Richiesta_Generazione.txt
LAST-Comando_Eseguito.ps1
LAST-Output_Completo.txt
LAST-Output_Compatto.md
LAST-Output_Compatto.docx
```

`LAST-Output_Compatto.md` must be copied to the clipboard with `Set-Clipboard`. If clipboard access fails, the script must log a warning and still write the file.

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
- final artifact copy to `LAST-*` names;
- a non-zero process exit on failed required gates.

Use splatting for commands with many named parameters. Use `Tee-Object` or explicit logging wrappers when console output and file output both matter. Avoid relying only on `Start-Transcript`: transcripts are useful as a supplemental record but can miss or format streams in ways that are less suitable than explicit command logs.

## Phase Model

Use phases whenever the pack contains publication or state-changing steps.

- FASE A: local verification, read-only checks, syntax checks, tests, `git --no-pager status --short`, `git --no-pager diff --check`, health checks, and report generation.
- FASE B: commit, push, PR creation, or PR checks. This phase is human-gated and must stop if FASE A fails.
- FASE C: merge, release, deploy, restart, publication, or cleanup that affects external state. This phase is human-gated and must stop if FASE A or FASE B gates fail.

Publication must not proceed when tests, verify, health check, or guardrails fail. Do not hide failures behind warnings. The known `gh pr checks --watch` case with `no checks reported` or exit code `1` can be reported as a controlled warning only when every other required local gate has passed.

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
