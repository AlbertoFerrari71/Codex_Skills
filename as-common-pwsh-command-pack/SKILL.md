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
- Avoid `setx PATH`, unrequested destructive commands, secret leakage, and any attempt to bypass failed gates.
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

### Regola PowerShell per copia/incolla

Quando generi comandi PowerShell per Alberto:

- per comandi a riga singola, chiudi con una riga finale innocua eseguibile, preferibilmente:
  `Write-Host "";`
- assicurati che l’ultimo comando venga realmente eseguito dopo l’incolla, senza lasciare PowerShell in attesa di Enter;
- per blocchi multilinea, termina sempre il blocco con newline reale adeguato;
- evita di affidarti solo a `Write-Host ""` se manca l’invio finale;
- questa regola vale anche per prompt Codex, report operativi, step Git e istruzioni di progetto.