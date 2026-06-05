---
name: "as-common-pwsh-command-pack"
description: "Generate safe logged PowerShell command packs for Alberto with robust .ps1 scripts, numbered and LAST outputs, compact Markdown/DOCX reports, clipboard copy, and Git/Codex/ASF guardrails."
---

# as-common-pwsh-command-pack

Use this skill when Alberto asks for PowerShell command packs, robust Windows command sequences, ASF/Git/Codex verification command packs, or logged scripts that produce reusable output files.

## Core Rules

- Prefer a generated `.ps1` script over long inline PowerShell whenever commands are long, phased, conditional, logged, or likely to exceed shell limits.
- Use `pwsh -NoProfile -ExecutionPolicy Bypass -File <script.ps1>` as the launcher.
- Build scripts with `#Requires -Version 7.0`, `Set-StrictMode -Version Latest`, `$ErrorActionPreference = 'Stop'`, `try/catch/finally`, and explicit `$LASTEXITCODE` checks after native commands.
- Write all generated command packs under `D:\FG-SAB Dropbox\Alberto Ferrari\ChatGPT_Bridge`; for ASF use `D:\FG-SAB Dropbox\Alberto Ferrari\ChatGPT_Bridge\AI_Software_Factory\pwsh_command`.
- Always generate numbered artifacts and matching `LAST-*` files, including compact Markdown and DOCX outputs, then copy `LAST-Output_Compatto.md` to the clipboard with `Set-Clipboard`.
- Split FASE A / FASE B / FASE C when commit, push, PR, merge, release, deploy, restart, or publication may appear. Publication phases must stop if tests, verify, health checks, or guardrails fail.
- Use `git --no-pager` for potentially long Git output.
- Avoid `setx PATH`, unrequested destructive commands, sensitive-value leakage, and any attempt to bypass failed gates.
- Treat `gh pr checks --watch` with `no checks reported` or exit code `1` as a controlled warning only when all other local gates pass.
- Prefer UTF-8 without BOM for generated text and recommend `.gitattributes` line-ending policy for mixed Windows/Git work.

## Reference Files

Read these files when preparing a non-trivial command pack:

- `references/pwsh-command-pack-standard.md` for the full operating standard, guardrails, source principles, file contract, and phase rules.
- `references/pwsh-command-pack-template.ps1` for the robust PowerShell template to adapt.
- `examples/demo-prompts.md` for progressive demo prompts and expected pack shapes.

## Response Pattern

When returning a command pack to Alberto, keep the answer concise:

1. State the output folder and the launcher command.
2. State which phases are included and which are manual/human-gated.
3. State the verification gates that block publication.
4. State that the compact Markdown is copied to clipboard by the generated script.
5. Do not claim commit, push, PR, merge, release, deploy, or restart unless Alberto explicitly asked for and ran those phases.

## PowerShell paste termination

Do not describe a final `Write-Host ";";` as an execution guarantee. It is only a visual marker.

For one useful PowerShell command meant for copy/paste, prefer a three-line block:

```powershell
<useful command>
Write-Host "Linea fake 1 - termina il comando utile precedente"
Write-Host "Linea fake 2 - se resta in attesa, premere Enter qui"
```

For two or more useful commands, add one harmless fake line after the useful commands:

```powershell
<useful command 1>
<useful command 2>
Write-Host "Linea fake - se resta in attesa, premere Enter qui"
```

For long or critical workflows, prefer writing a `.ps1` file and executing it:

```powershell
$ScriptPath = Join-Path $env:TEMP "task.ps1"
@'
<commands here>
'@ | Set-Content -LiteralPath $ScriptPath -Encoding UTF8
pwsh -NoProfile -ExecutionPolicy Bypass -File $ScriptPath
```

The fake line is intentionally harmless. Its purpose is paste termination: if the final newline is lost, the useful command has already been terminated by the following line. If the terminal remains waiting, it should wait on a fake line, not on the useful command.
