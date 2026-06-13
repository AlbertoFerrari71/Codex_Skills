---
name: as-common-codex-command-pack
description: Use this skill when Alberto asks to prepare one executable Codex prompt or command packet for implementation, debugging, review, or repository work. Use it for temporary handoff prompts to Codex. Do not use it for numbered step governance, durable docs, or restart summaries.
---

# as-common-codex-command-pack

## Purpose

Use this skill whenever Alberto asks to prepare, save, revise, archive, or standardize a Codex prompt, task packet, implementation prompt, step prompt, or Codex handoff.

Every Codex prompt must be:
- self-contained;
- safe;
- traceable;
- reproducible;
- stored in codex_command;
- available as a numbered step-specific prompt file;
- copied to clipboard only when explicitly requested, using file-content piping.

## Use This Skill When

- Alberto needs one executable prompt or command packet to paste into Codex.
- The output is a temporary handoff prompt for implementation, debugging, review, verification, or repository work.
- The prompt must be saved in the Bridge with numbered files; create `LAST-*` mirrors only when Alberto explicitly asks for them.

## Do Not Use This Skill When

- Alberto is managing the full lifecycle of a numbered step.
- The requested output is persistent README, AGENTS.md, runbook, or workflow documentation.
- The goal is to close a long chat and prepare a restart summary.

## Use Instead

- `as-common-codex-step-manager` for numbered step scope, phases, status, final report, and next step.
- `as-common-docs-runbook-builder` for persistent repository documentation.
- `as-common-project-riepilogo-operativo` for chat restart summaries.

## Default folders

Dropbox Bridge root:

D:\FG-SAB Dropbox\Alberto Ferrari\ChatGPT_Bridge

For AI Software Factory:

D:\FG-SAB Dropbox\Alberto Ferrari\ChatGPT_Bridge\AI_Software_Factory\codex_command

For other projects prefer:

D:\FG-SAB Dropbox\Alberto Ferrari\ChatGPT_Bridge\<Project_Name>\codex_command

## Required output files

Create numbered files:

- NNNN-Richiesta_Generazione_<slug>.txt
- NNNN-Prompt_Codex_<slug>.md
- NNNN-Checklist_Codex_<slug>.md
- NNNN-Report_Atteso_<slug>.md

Create these `LAST-*` mirrors only when Alberto explicitly requests them:

- LAST-Richiesta_Generazione.txt
- LAST-Prompt_Codex.md
- LAST-Checklist_Codex.md
- LAST-Report_Atteso.md

Use the next available four-digit number and a short kebab-case slug.

If `LAST-Prompt_Codex.md` was explicitly requested, copy its full content to clipboard only when explicitly requested too. Use `Get-Content -Path $LastPromptPath -Raw | Set-Clipboard`; never use `Set-Clipboard -Path`.

## Bridge retrieval and LAST policy

Numbered prompt/report files are the preferred source for recovery. `LAST-*` files are convenience fallbacks and can be stale.

When Alberto references an output/log/report under:

```text
D:\FG-SAB Dropbox\Alberto Ferrari\ChatGPT_Bridge
```

before asking him to paste content, try to retrieve the file through the Dropbox/Bridge connector if available:

1. Look first for the specific numbered/progressive file named by the step, for example `0910A-Output_Diagnostica_Diretta_Git_Cached_Diff.txt`.
2. Use `LAST-Output_Compatto.md`, `LAST-Output_Completo.txt`, or `LAST-Prompt_Codex.md` only if the progressive file is not available.
3. If `LAST` exists but step, filename, timestamp, or server_modified is incoherent with the current step, declare it stale and do not use it as evidence.
4. If Bridge access or Dropbox indexing is unavailable, ask only for the minimum excerpt needed, such as `## Cached diff check`, `## Cached diff names`, `## Git status short`, or the exact progressive path.

## Codex prompt contract

Every Codex prompt must include:

1. Project name.
2. GitHub repository.
3. Local folder.
4. Required branch.
5. Step number and title.
6. Objective.
7. Current context/state.
8. Files/areas to modify.
9. Files/areas not to modify.
10. Safety constraints.
11. Required tests and verification commands.
12. Documentation updates to consider.
13. Git constraints.
14. Final report format.

## Default safety constraints

Unless Alberto explicitly says otherwise, every Codex prompt must state:

- Do not commit.
- Do not push.
- Do not create PRs.
- Do not merge.
- Do not deploy.
- Do not use destructive commands.
- Do not delete files or folders.
- Do not run git reset, git clean, or force push.
- Do not modify credentials or sensitive values.

## Reference files

Use these support files for non-trivial prompt packs:

- `references/codex-command-pack-standard.md` for the standard structure and guardrails.
- `examples/demo-prompts.md` for compact examples of acceptable task packets.
- Stop and report if the working tree is dirty before making changes.
- Prefer small, reversible, testable changes.
- No new dependencies unless clearly justified.
- If the prompt includes operational PowerShell blocks for Alberto to paste, require `Clear-Host` as the first line and `# terminatore copia-incolla` followed by one real blank final line.

## Required checks

Ask Codex to run relevant checks, usually:

- git branch --show-current
- git status --short
- git --no-pager log --oneline --max-count=5
- project tests, if available
- verification gate, if available
- git diff --check
- git status --short at the end

## Final Codex report format

Require this exact structure:

A. Step eseguito
B. Stato: completato / bloccato / parziale / fallito
C. Branch corrente
D. File creati
E. File modificati
F. Sintesi modifiche
G. Test eseguiti e risultato
H. Verifiche Git
I. Rischi/anomalie/attenzioni
J. Prossimo step consigliato
K. Riga finale:
- Step eseguito: NNN
- Tempo impiegato: se disponibile
- Step successivo consigliato: NNN

If blocked, Codex must explain why it stopped, what it verified, which files were not modified, and what is needed to unblock.
