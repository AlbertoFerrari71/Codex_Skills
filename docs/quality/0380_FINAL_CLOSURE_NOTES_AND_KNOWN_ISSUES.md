# 0380 Final Closure Notes And Known Issues

Data step: 2026-06-12

## Attivita skill considerate chiuse

- Catalogo base `as-common-*` consolidato a 22 skill.
- Validator catalogo, score, trigger eval, smoke trial e release workflow disponibili.
- Skill mature principali rafforzate nello step 0280-0330.
- Trigger boundaries documentati per le collisioni piu probabili.
- Test contrattuali presenti per le skill mature hardenizzate e per skill tecniche recenti.
- Project instructions builder, prompt length advisor, web UI design review e web UI linguistic visual QA risultano presenti e catalogate.

## Attivita rimandate volutamente

- Nessuna nuova skill creata in questo step.
- Nessun refactor ampio delle skill esistenti.
- Nessuna normalizzazione line endings.
- Nessuna conversione dei smoke pack documentali in automazione obbligatoria.
- Nessuna verifica tecnica dei repository esterni: la matrice 0360 e' logica, non un audit dei repo target.

## Warning LF/CRLF storici

`repo_health_check.py` continua a segnalare mixed-EOL storici su:

- `.gitattributes`
- `docs/asf_external_pilot/0870_CONTROLLED_WRITE_PILOT.md`
- `docs/naming-conventions.md`
- `docs/skill-authoring-guide.md`
- `docs/skill-quality-checklist.md`

Questi warning non sono bloccanti finche:

- `git --no-pager diff --check` passa;
- i validator passano;
- i test passano;
- lo step non introduce nuovi whitespace error;
- non viene fatta normalizzazione EOL fuori scope.

## `quick_validate.py`

`quick_validate.py` non e' presente nel repository. Il comando richiesto:

```powershell
python quick_validate.py as-common-codex-prompt-length-advisor
```

e' quindi SKIPPED. Non e' stato creato uno script fittizio per soddisfare il prompt.

## Trigger eval euristico

`validators/trigger_eval_cases.json` contiene 124 casi e copre tutte le 22 skill con negative boundaries. Questo e' un buon presidio regressivo, ma resta euristico.

Limite noto: puo' emergere un falso trigger in prompt reali che combinano governance, dominio tecnico, UI e report finale nello stesso messaggio.

## Smoke pack documentale vs smoke reale

`validators/smoke_trial_cases.py` passa. Il pack 0330 resta pero documentale per i casi real-use delle skill mature: dimostra ragionamento e boundaries, non esecuzione automatica su repository applicativi reali.

Questo e' accettabile per una chiusura catalogo. I prossimi smoke reali devono nascere da uso concreto dei progetti, non da test sintetici aggiunti solo per aumentare copertura apparente.

## Cosa non fare nei prossimi step

- Non aprire un nuovo mega-ciclo di hardening senza evidenza reale.
- Non creare skill duplicate per domini gia coperti.
- Non modificare skill solo per alzare uno score euristico.
- Non normalizzare EOL insieme a modifiche funzionali.
- Non trattare cache `__pycache__` ignorate come blocco se i validator le classificano come warning.
- Non usare skill di progetto esterno per audit tecnico dei repository senza leggere prima quel repo.

## Quando riaprire il ciclo skill

Riaprire solo se si verifica almeno una di queste condizioni:

- falso trigger ricorrente in uso reale;
- task importante non coperto da skill esistenti;
- collisione concreta tra due skill con output sbagliato;
- validator locale insufficiente a intercettare regressioni note;
- nuovo workflow ASF o Bridge che richiede standardizzazione.

## Stato finale consigliato

PASS_WITH_WARNINGS. Il catalogo e' utilizzabile e pubblicabile, ma i warning residui vanno mantenuti visibili.
