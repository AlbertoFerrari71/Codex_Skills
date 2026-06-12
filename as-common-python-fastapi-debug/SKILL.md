---
name: as-common-python-fastapi-debug
description: "Usa questa skill per debug locale Python/FastAPI/pytest di Alberto: endpoint, status code, trace, fixture, SQLAlchemy, Uvicorn, Jinja, template rendering, venv e fix minimi verificati. Non usarla per UI visual review, project instructions, prompt Codex, OpenCV, VBA o Git publish flow."
---

# Scopo

Usa questa skill per progetti Python, FastAPI, pytest, SQLAlchemy, Uvicorn, Jinja e debug incrementale nei progetti di Alberto.

# Quando usarla

Usala per:
- bug Python/FastAPI;
- test pytest e fixture;
- SQLAlchemy, sessioni e query locali;
- Uvicorn, virtualenv e configurazione ambiente;
- endpoint, route e status code;
- template rendering Jinja;
- error trace reali;
- log e debug locale;
- fix piccolo con gate prima del commit.

# Quando NON usarla

Non usarla per:
- UI visual review o screenshot frontend: usa `as-common-web-ui-design-review`;
- project instructions, AGENTS.md o quality gate durevoli: usa `as-common-project-instructions-builder`;
- prompt Codex operativo: usa `as-common-codex-command-pack`;
- pipeline immagini OpenCV: usa `as-common-opencv-image-pipeline`;
- VBA/Excel/Access: usa `as-common-vba-excel-access-alberto`;
- Git publish flow, PR e merge: usa `as-common-codex-step-manager` o skill Git dedicate.

# Procedura

1. Preferire modifiche piccole e verificabili.
2. Controllare struttura progetto e file coinvolti.
3. Non introdurre nuove dipendenze senza motivo.
4. Usare test esistenti prima di crearne di nuovi.
5. Separare errore osservato, causa probabile e fix proposto.
6. Dopo ogni modifica proporre comandi di verifica semplici.
7. Mantenere codice leggibile e minimale.
8. Distinguere trace reale da ipotesi quando mancano log completi.
9. Separare ambiente locale, server e deploy.

# Output atteso

- Diagnosi breve.
- Errore osservato e causa probabile.
- Passi minimi.
- File da leggere o modificare.
- Test mirati.
- Comandi.
- Rollback o stop se la patch non regge.
- Log da leggere.
- Fix piccolo.
- Gate prima di commit.
- Rischi residui.
- Prossimo passo.

# References

- `references/fastapi-debug-flow.md`
- `references/pytest-minimal-repro-checklist.md`

# Regole

- Non inventare lo stack: dedurlo dai file o dichiarare l'ipotesi.
- Non trasformare un bug locale in refactor architetturale.
- Non confondere fallimento template/Jinja con errore API senza prova.
