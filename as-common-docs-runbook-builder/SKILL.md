---
name: as-common-docs-runbook-builder
description: Usa questa skill quando Alberto vuole creare o migliorare README, runbook, AGENTS.md, decision log, roadmap, prompt operativi o documentazione tecnica di progetto.
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
- prompt per Codex;
- checklist di rilascio/test;
- documentazione di onboarding.

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
