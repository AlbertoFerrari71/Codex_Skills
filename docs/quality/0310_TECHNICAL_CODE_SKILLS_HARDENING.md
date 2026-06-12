# 0310) Technical Code Skills Hardening

Data: 2026-06-12

Skill:

- `as-common-opencv-image-pipeline`
- `as-common-python-fastapi-debug`

## Problemi Trovati

| Skill | Problema |
|---|---|
| as-common-opencv-image-pipeline | Buon trigger tecnico ma anti-trigger assenti; output e stile C++ Alberto non abbastanza contrattuali. |
| as-common-python-fastapi-debug | Buona base ma senza separazione esplicita da UI, OpenCV, VBA e Git publish flow. |

## Modifiche Fatte

| Skill | Modifiche |
|---|---|
| as-common-opencv-image-pipeline | Aggiunti trigger QR, omografia, binarizzazione, istogrammi, segmentazione, debug immagini intermedie e confronto output. Aggiunto DiamSign come esempio non vincolo. |
| as-common-python-fastapi-debug | Aggiunti trigger FastAPI, pytest, SQLAlchemy, Uvicorn, Jinja, endpoint, status code, fixture, trace e debug locale. |

## Trigger Positivi

- OpenCV C++/Python, QR, omografia, soglie, istogrammi, maschere e overlay.
- Debug visuale con immagini intermedie e metriche.
- FastAPI endpoint, status code, pytest, fixture, SQLAlchemy, Uvicorn e Jinja.
- Patch minima con test mirato e gate prima del commit.

## Anti-Trigger

| Skill | Anti-trigger principali |
|---|---|
| as-common-opencv-image-pipeline | Generazione immagine creativa, UI review, email, FastAPI backend, prompt Codex, analisi brevettuale, VBA. |
| as-common-python-fastapi-debug | UI visual review, project instructions, prompt Codex, OpenCV, VBA, Git publish flow. |

## Rischi

- Non confondere image processing con review visuale UI.
- Non trasformare bug FastAPI in refactor architetturale.
- Non inventare stack, immagini, ambiente o trace.
- Non usare OCR salvo necessita esplicita.

## Reference Aggiunte

| Skill | Reference |
|---|---|
| as-common-opencv-image-pipeline | `references/image-pipeline-debug-checklist.md`, `references/opencv-cpp-style-alberto.md` |
| as-common-python-fastapi-debug | `references/fastapi-debug-flow.md`, `references/pytest-minimal-repro-checklist.md` |

## Test Aggiunti

| Skill | Test |
|---|---|
| as-common-opencv-image-pipeline | `tests/test_skill_contract.py` |
| as-common-python-fastapi-debug | `tests/test_skill_contract.py` |

## Esempi Real-Use

- QR non letto dopo warp: salvare warp, maschera, soglie, overlay e metriche.
- Segmentazione glitter in C++ OpenCV rispettando stile Alberto.
- FastAPI 422 in pytest: payload, fixture, endpoint e fix minimo.
- Jinja 500: distinguere route, template e ambiente locale/server.
