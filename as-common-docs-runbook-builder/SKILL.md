---
name: as-common-docs-runbook-builder
description: Use this skill when Alberto asks to create or update persistent repository documentation, runbooks, AGENTS.md, README sections, workflow guides, or operational manuals. Do not use it for temporary Codex handoff prompts, numbered step lifecycle management, or chat restart summaries.
---

# Scopo

Creare documentazione operativa chiara, asciutta e utile a riprendere un progetto senza rileggere tutta la chat.

# Quando usarla

Usala per:
- README di progetto;
- runbook operativo;
- AGENTS.md;
- ROADMAP.md;
- DECISIONI.md;
- STATO_ATTUALE.md;
- prompt operativi persistenti come template documentati;
- checklist di rilascio/test;
- documentazione di onboarding.

# Quando NON usarla

Non usarla per:
- prompt temporanei da incollare in Codex per una singola esecuzione;
- gestione completa di uno step numerato;
- riepiloghi di chat o prompt di ripartenza;
- review tecnica read-only dello stato di una repository.

# Usa invece

- `as-common-codex-command-pack` per prompt temporanei o command packet Codex.
- `as-common-codex-step-manager` per lifecycle di step numerati.
- `as-common-project-riepilogo-operativo` per riepiloghi di ripartenza nuova chat.
- `as-common-repo-readiness-review` per review iniziale read-only di una repository.

# Principi

1. Documenta quello che serve davvero per lavorare.
2. Separa:
   - stato attuale;
   - decisioni prese;
   - procedure;
   - rischi;
   - comandi;
   - troubleshooting.
3. Evita romanzi: meglio sezioni brevi, aggiornabili.
4. Non duplicare informazioni già presenti: collega o sintetizza.
5. Inserisci comandi PowerShell secondo la skill `as-common-powershell-git-safe-flow`.
6. Evidenzia sempre percorso file/repo, branch, test e prossimo step.

# Struttura consigliata README

```markdown
# Nome progetto

## Obiettivo

## Stato attuale

## Struttura cartelle

## Setup rapido

## Comandi principali

## Test e verifica

## Workflow operativo

## Decisioni rilevanti

## Problemi noti

## Prossimi step
```

# Struttura consigliata AGENTS.md

```markdown
# Regole progetto per Codex

## Obiettivo progetto

## Vincoli non negoziabili

## Comandi test/verifica

## Convenzioni codice

## Workflow Git

## Cose da non fare
```

# Regole

- Non inventare comandi non verificati.
- Se un comando è ipotizzato, marcarlo come da verificare.
- Per progetti lunghi, aggiungi sempre una sezione "Come ripartire".
