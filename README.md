# Codex_Skills

Repository centrale delle skill Codex di Alberto Ferrari.

Questa repository contiene:

- skill comuni
- template skill
- documentazione
- validator
- linee guida operative

Le skill sono utilizzate direttamente da Codex tramite:

C:\Users\alberto.ferrari\.agents\skills

## Release workflow

Per creare nuove skill, modificare skill esistenti e pubblicare aggiornamenti verificati, usare `docs/release-workflow/100_SKILL_RELEASE_WORKFLOW_PACK.md`.

## Verifica rapida

Da root repository:

```powershell
python validators\repo_health_check.py
```

Il comando esegue i controlli locali di base senza dipendenze esterne: validatore catalogo, unit test, smoke trial, release workflow check e `git --no-pager diff --check`.

Per rigenerare gli artefatti tracciati:

```powershell
python validators\check_agent_skills.py --root . --write-index --write-score
```

