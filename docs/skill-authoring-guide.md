# Skill Authoring Guide

Linee guida per creare nuove skill.

1. creare cartella
2. creare SKILL.md
3. aggiungere references
4. aggiungere examples
5. validare

## Validazione skill

Eseguire il validator dalla root repository:

```powershell
python validators/check_agent_skills.py
python validators/check_agent_skills.py --write-index --write-score
python validators/test_check_agent_skills.py
```

Il comando base controlla naming, frontmatter, campi obbligatori, body operativo, cartelle consigliate, file backup/temp e possibili segnali di segreti.

Usare `--write-index --write-score` quando serve aggiornare:

- `SKILLS_INDEX.md`
- `SKILL_SCORE.md`

Se una modifica produce backup temporanei, archiviarli fuori dalle skill operative oppure rimuoverli dopo verifica. I backup storici temporanei vivono in `_archive/backup-skills/`.

