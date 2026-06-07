# Validators

Controlli locali per il catalogo Codex_Skills. Tutti i comandi usano solo la
standard library Python e non scrivono file, salvo quando indicato.

## Health check rapido

Da root repository:

```powershell
python validators\repo_health_check.py
```

Il comando esegue:

- validazione catalogo skill;
- unit test dei validator;
- smoke trial temporanei;
- controllo wiring del release workflow;
- `git --no-pager diff --check`.

## Comandi singoli

```powershell
python validators\check_agent_skills.py --root .
python -m unittest discover -s validators -p "test_*.py"
python validators\smoke_trial_cases.py
python validators\release_workflow_check.py
git --no-pager diff --check
```

## Aggiornare file generati

Aggiorna indice e score solo quando vuoi rigenerare gli artefatti tracciati:

```powershell
python validators\check_agent_skills.py --root . --write-index --write-score
```

Prima di rigenerare, rimuovere o archiviare eventuali backup locali se non
devono comparire in `SKILLS_INDEX.md`.

