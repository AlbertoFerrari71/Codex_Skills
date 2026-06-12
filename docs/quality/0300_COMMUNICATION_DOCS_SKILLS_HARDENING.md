# 0300) Communication And Docs Skills Hardening

Data: 2026-06-12

Skill:

- `as-common-business-email-draft`
- `as-common-docs-runbook-builder`

## Problemi Trovati

| Skill | Problema |
|---|---|
| as-common-business-email-draft | Stile Alberto presente ma non abbastanza contrattuale; mancavano output per oggetto, tono, varianti, rischi e punti da non scrivere. |
| as-common-docs-runbook-builder | Descrizione troppo vicina a project instructions/AGENTS; mancava distinzione netta da handoff chat, step manager ed email. |

## Modifiche Fatte

| Skill | Modifiche |
|---|---|
| as-common-business-email-draft | Aggiunti trigger HR, dipendente, fornitore, cliente, contestazione, sollecito, revisione prima invio e tono piu morbido/fermo. |
| as-common-docs-runbook-builder | Rifocalizzata su runbook, procedure ripetibili, manutenzione, deployment notes, troubleshooting, onboarding e guide persistenti. |

## Trigger Positivi

- Email delicata a dipendente, cliente o fornitore.
- Risposta a contestazione e sollecito.
- Comunicazioni HR e negoziali.
- Runbook operativo, checklist manutenzione, deployment notes.
- Troubleshooting e onboarding operativo.

## Anti-Trigger

| Skill | Anti-trigger principali |
|---|---|
| as-common-business-email-draft | Report tecnico lungo, prompt Codex, legal claim, UI review, runbook tecnico, copy marketing puro. |
| as-common-docs-runbook-builder | Project Instructions/AGENTS policy, prompt Codex singolo, step numerato, riepilogo nuova chat, email, UI review. |

## Sovrapposizioni Risolte

- Project Instructions e AGENTS.md policy restano a `as-common-project-instructions-builder`.
- Handoff nuova chat resta a `as-common-project-riepilogo-operativo`.
- Lifecycle branch/test/commit/PR resta a `as-common-codex-step-manager`.
- Email esterne o delicate restano a `as-common-business-email-draft`.

## Reference Aggiunte

| Skill | Reference |
|---|---|
| as-common-business-email-draft | `references/alberto-email-tone-rubric.md`, `references/delicate-email-risk-checklist.md` |
| as-common-docs-runbook-builder | `references/runbook-structure-checklist.md`, `references/runbook-vs-project-instructions.md` |

## Test Aggiunti

| Skill | Test |
|---|---|
| as-common-business-email-draft | `tests/test_skill_contract.py` |
| as-common-docs-runbook-builder | `tests/test_skill_contract.py` |

## Esempi Real-Use

- Email HR: logica, empatia, fermezza rispettosa e prossima azione chiara.
- Risposta a contestazione fornitore senza ammissioni non decise.
- Runbook deploy locale con prerequisiti, passi, verifiche e rollback.
- Guida onboarding operativa con ownership e aggiornamento futuro.
