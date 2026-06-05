---
name: as-common-codex-command-pack
description: Use when preparing, saving, reviewing, or updating Codex prompts/task packets for Alberto. Creates numbered and LAST files in codex_command, copies LAST-Prompt_Codex.md to clipboard, and enforces safety, tests, and report contracts.
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
- available as LAST-Prompt_Codex.md;
- copied to clipboard when possible.

## Default folders

Dropbox Bridge root:

D:\FG-SAB Dropbox\Alberto Ferrari\ChatGPT_Bridge

For AI Software Factory:

D:\FG-SAB Dropbox\Alberto Ferrari\ChatGPT_Bridge\AI_Software_Factory\codex_command

For other projects prefer:

D:\FG-SAB Dropbox\Alberto Ferrari\ChatGPT_Bridge\<Project_Name>\codex_command

## Required output files

Create numbered files and LAST files:

- NNNN-Richiesta_Generazione_<slug>.txt
- NNNN-Prompt_Codex_<slug>.md
- NNNN-Checklist_Codex_<slug>.md
- NNNN-Report_Atteso_<slug>.md
- LAST-Richiesta_Generazione.txt
- LAST-Prompt_Codex.md
- LAST-Checklist_Codex.md
- LAST-Report_Atteso.md

Use the next available four-digit number and a short kebab-case slug.

After writing LAST-Prompt_Codex.md, copy its full content to clipboard with Set-Clipboard when available.

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
