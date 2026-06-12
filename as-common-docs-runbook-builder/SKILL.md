---
name: as-common-docs-runbook-builder
description: Use this skill when Alberto asks to create or update persistent repository documentation such as runbooks, repeatable procedures, maintenance checklists, deployment notes, troubleshooting, onboarding, README sections, or user/technical guides. Do not use it for Project Instructions or AGENTS policy, one-shot Codex prompts, numbered step lifecycle, email, UI review, or chat restart summaries.
---

# Scopo

Creare documentazione operativa chiara, asciutta e utile a eseguire, mantenere o riprendere un progetto senza rileggere tutta la chat.

# Quando usarla

Usala per:
- README di progetto;
- runbook operativo;
- procedura ripetibile;
- checklist di manutenzione;
- deployment notes;
- troubleshooting;
- onboarding operativo;
- guida utente o tecnica persistente;
- ROADMAP.md, DECISIONI.md o STATO_ATTUALE.md quando sono documentazione operativa;
- checklist di rilascio/test;
- documentazione di onboarding.

# Quando NON usarla

Non usarla per:
- istruzioni progetto ChatGPT, Codex AGENTS.md o policy agente: usa `as-common-project-instructions-builder`;
- prompt temporanei da incollare in Codex per una singola esecuzione;
- gestione completa di uno step numerato;
- riepiloghi di chat o prompt di ripartenza;
- review tecnica read-only dello stato di una repository;
- email a clienti/fornitori/collaboratori;
- review visuale UI/web.

# Usa invece

- `as-common-codex-command-pack` per prompt temporanei o command packet Codex.
- `as-common-codex-step-manager` per lifecycle di step numerati.
- `as-common-project-riepilogo-operativo` per riepiloghi di ripartenza nuova chat.
- `as-common-repo-readiness-review` per review iniziale read-only di una repository.
- `as-common-project-instructions-builder` per istruzioni progetto, AGENTS.md e quality gate durevoli per ChatGPT/Codex.
- `as-common-business-email-draft` per comunicazioni esterne o delicate.

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
6. Evidenzia sempre percorso file/repo, prerequisiti, comandi, verifiche, rollback/stop e ownership.

# Struttura consigliata runbook

```markdown
# Titolo runbook

## Scopo

## Prerequisiti

## Quando usarlo

## Passi operativi

## Comandi

## Verifiche

## Rollback / stop

## Troubleshooting

## Ownership

## Aggiornamento futuro
```

# Struttura consigliata README operativo

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

# References

- `references/runbook-structure-checklist.md`
- `references/runbook-vs-project-instructions.md`

# Regole

- Non inventare comandi non verificati.
- Se un comando è ipotizzato, marcarlo come da verificare.
- Per progetti lunghi, aggiungi sempre una sezione "Come ripartire".
- Non trasformare un runbook in policy agente o istruzioni ChatGPT.
- Non includere rollback se non esiste: scrivere "rollback non definito" e indicare cosa verificare.
