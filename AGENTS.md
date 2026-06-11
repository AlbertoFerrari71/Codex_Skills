# AGENTS.md

## Scopo

Questa repository contiene il catalogo ufficiale delle skill Codex.

## Naming

Tutte le skill devono:

- essere minuscole
- usare kebab-case
- non usare underscore
- non usare spazi
- non usare accenti

Esempio:

as-common-codex-command-pack

## Struttura minima

nome-skill/

    SKILL.md

## Struttura consigliata

nome-skill/

    SKILL.md
    references/
    examples/
    scripts/

## Sicurezza

Non salvare:

- password
- token
- api key
- certificati
- file .env

## Workflow

1. creare skill
2. validare skill
3. aggiornare indice
4. commit
5. push

## Project instructions builder workflow

Usare `as-common-project-instructions-builder` quando il lavoro riguarda istruzioni durevoli di progetto per ChatGPT, Codex, `AGENTS.md`, Copilot o quality gate.

La prima applicazione reale per questa repository vive in:

docs/project-instructions/0160_CODEX_SKILLS_PROJECT_INSTRUCTIONS.md

I file `docs/project-instructions/*` sono documenti applicativi di supporto: non sostituiscono `AGENTS.md`, README, validator o workflow di release.

Non pubblicare automaticamente modifiche a skill, indici o istruzioni progetto salvo istruzione esplicita di Alberto e gate locali PASS.

