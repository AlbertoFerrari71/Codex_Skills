# 0350 Installed Skills Sync And Catalog Integrity

Data step: 2026-06-12

## Sintesi

Il controllo install/sync passa con warning non bloccanti. La repository e' gia' la cartella installata `C:\Users\alberto.ferrari\.agents\skills`; non e' stata fatta copia o installazione esterna.

## Risultato `installed_skills_sync_check.py`

Comando:

```powershell
python validators\installed_skills_sync_check.py --root .
```

Esito:

| Voce | Valore |
|---|---:|
| Skills found | 22 |
| Skills in `SKILLS_INDEX.md` | 22 |
| Skills in `SKILL_SCORE.md` | 22 |
| Blocking issues | 0 |
| Warnings | 9 |
| Info | 2 |
| Risultato | PASS_WITH_WARNINGS |

Warning:

- `ignored_cache_in_active_skill` per cache `__pycache__` generate dai test nelle skill con test Python.

Info:

- root dentro `.agents/skills`;
- `_archive/backup-skills` ignorata come area backup inattiva.

## Differenze tra repository e skill installate

Non ci sono differenze di installazione da riconciliare: la root repository locale coincide con la root delle skill installate usata da Codex.

## File non tracciati

Al momento della validazione locale prima della scrittura documentale, `git status --short` era vuoto. Dopo la scrittura dello step, gli unici file non ancora tracciati previsti sono i documenti 0340-0390 e gli aggiornamenti ammessi prima dello staging allow-list.

## Cache ignorate

Le cache `__pycache__` sono prodotte dai test e sono ignorate da Git. Il validator le rende visibili come warning, non come blocchi.

Regola applicata nello step:

- non cancellare cache in modo indiscriminato;
- non normalizzare line endings;
- documentare il warning se i validator restano PASS.

## Stato `SKILLS_INDEX.md`

`SKILLS_INDEX.md` risulta coerente con 22 skill:

- 22 skill totali;
- 0 skill con errors;
- 0 skill con warnings;
- nessun file backup rilevato.

`python validators\check_agent_skills.py --root . --write-index --write-score` e' stato eseguito e ha confermato PASS.

## Stato `SKILL_SCORE.md`

`SKILL_SCORE.md` risulta coerente con il catalogo:

- 22 skill;
- tutte con `StructureScore` 100;
- 20 skill grade A;
- 2 skill grade B: `as-common-technical-patent-draft`, `as-common-web-ui-design-review`.

Le due B non sono blocchi release: derivano da score operativo euristico, non da errori o warning validator.

## Coerenza con validator

| Comando | Esito | Note |
|---|---|---|
| `python validators\check_agent_skills.py --root . --write-index --write-score` | PASS | Cataloghi scritti/confermati, 22 skill, 0 errori, 0 warning. |
| `python validators\check_agent_skills.py --root . --fail-on-warning` | PASS | Modalita severa senza warning. |
| `python validators\installed_skills_sync_check.py --root .` | PASS_WITH_WARNINGS | Solo cache ignorate. |
| `python validators\repo_health_check.py` | PASS_WITH_WARNINGS | Sync warning e mixed-EOL storici non bloccanti. |

## Azioni correttive

Azioni fatte:

- eseguiti validator disponibili;
- confermata coerenza cataloghi;
- documentate cache ignorate e mixed-EOL storici.

Azioni non fatte:

- nessuna cancellazione cache indiscriminata;
- nessuna normalizzazione EOL;
- nessun nuovo validator creato;
- nessuna modifica a skill per ragioni cosmetiche.

## Decisione

PASS_WITH_WARNINGS. La release puo' procedere se anche i gate Git, PR checks e final main clean passano.
