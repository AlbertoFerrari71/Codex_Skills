# 0320) Trigger Boundaries And Overlap Cleanup

Data: 2026-06-12

File aggiornato: `validators/trigger_eval_cases.json`

## Sintesi

Aggiunti 44 casi trigger-eval per le sei skill candidate:

- 18 casi positivi;
- 20 casi negativi;
- 6 casi borderline.

Ogni caso usa input realistici, non trigger generici come "ricerca", "email",
"debug", "documento" o "brevetto" senza contesto.

## Skill Toccate

| Skill | Positivi | Negativi | Borderline |
|---|---:|---:|---:|
| as-common-deep-research-industriale | 3 | 3 | 1 |
| as-common-technical-patent-draft | 3 | 3 | 1 |
| as-common-business-email-draft | 3 | 3 | 1 |
| as-common-docs-runbook-builder | 3 | 4 | 1 |
| as-common-opencv-image-pipeline | 3 | 3 | 1 |
| as-common-python-fastapi-debug | 3 | 4 | 1 |

## Casi Positivi Aggiunti

- Deep research: coating/materiali, scouting fornitori/norme, processi e benchmark tecnico-economici.
- Patent draft: invention disclosure, processo/coating per consulente, claim draft tecnico non legale.
- Business email: HR delicata, contestazione fornitore, revisione mail cliente.
- Docs runbook: deploy, troubleshooting/manutenzione, onboarding operativo.
- OpenCV: QR/omografia, C++ style Alberto, maschere/istogrammi.
- FastAPI: pytest fixture/status code, SQLAlchemy/Uvicorn, Jinja/template.

## Casi Negativi Aggiunti

- Deep research esclusa per email, project instructions e scelta livello modello.
- Patent draft esclusa per benchmark mercato, email e prompt Codex.
- Business email esclusa per ricerca tecnica, runbook e command packet Codex.
- Docs runbook esclusa per Project Instructions/AGENTS, riepilogo chat, step manager e prompt length.
- OpenCV esclusa per UI review, FastAPI e disclosure brevettuale.
- FastAPI esclusa per UI review, OpenCV, Git publish flow e VBA.

## Casi Borderline

- Brevetti come fonti tecniche: deep research, non patent draft.
- Prior art preliminare per differenze tecniche da portare al consulente: patent draft.
- Appunti tecnici trasformati in email al fornitore: business email.
- Procedura ripetibile in README operativo: docs runbook.
- QR non letto dopo warp con debug immagini: OpenCV.
- Pagina web con errore 500 da trace/template: FastAPI, non UI review.

## Overlap Ridotti

Copertura nuova o rinforzata verso:

- `as-common-project-instructions-builder`
- `as-common-project-riepilogo-operativo`
- `as-common-codex-command-pack`
- `as-common-codex-step-manager`
- `as-common-codex-prompt-length-advisor`
- `as-common-model-effort-advisor`
- `as-common-web-ui-design-review`
- `as-common-web-ui-linguistic-visual-qa`
- `as-common-opencv-image-pipeline`
- `as-common-python-fastapi-debug`
- `as-common-vba-excel-access-alberto`
- `as-common-technical-patent-draft`
- `as-common-deep-research-industriale`

## Overlap Residui

- Patent draft e deep research restano vicine quando i brevetti sono sia fonte tecnica sia materiale per disclosure.
- Docs runbook e project instructions restano vicine su README/AGENTS, ma il confine e' ora esplicito.
- FastAPI e UI review restano vicine quando un errore backend appare come pagina web rotta.

## Raccomandazione Finale

Mantenere i casi 0320 come regressione minima per routing delle skill mature.
Un futuro playbook 0340 dovrebbe spiegare all'operatore quando scegliere una
skill rispetto alle vicine.
