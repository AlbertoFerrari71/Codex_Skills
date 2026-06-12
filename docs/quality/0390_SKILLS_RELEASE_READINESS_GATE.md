# 0390 Skills Release Readiness Gate

Data step: 2026-06-12

## Decisione

PASS_WITH_WARNINGS per la fase locale pre-PR.

La merge readiness finale dipende dai gate runtime PR checks e final main clean, che sono registrati nel report Bridge finale perche avvengono dopo il commit di questo documento.

## Gate table

| Gate | Esito | Note |
|---|---|---|
| Naming gate | PASS | 22 cartelle `as-common-*`, tutte lowercase kebab-case, nessun underscore/spazio/accento. |
| Duplicate gate | PASS | Nessun duplicato nel campo `name`; cartella e campo `name` coincidono. |
| Trigger overlap gate | PASS_WITH_WARNINGS | 124 casi trigger eval e 22 skill coperte; resta euristico. |
| Catalog freshness gate | PASS | `check_agent_skills.py --write-index --write-score` e `repo_health_check.py` passano. |
| Installed sync gate | PASS_WITH_WARNINGS | 0 blocking issues; warning solo per cache `__pycache__` ignorate. |
| Test gate | PASS | `python -m pytest`: 78 passed; validator unittest: 35 test. |
| Smoke gate | PASS_WITH_WARNINGS | `smoke_trial_cases.py` PASS; smoke real-use 0330 documentale, non repository-target automation. |
| Repo health gate | PASS_WITH_WARNINGS | PASS con cache ignorate e mixed-EOL storici. |
| Git diff check gate | PASS | `git --no-pager diff --check` e `git --no-pager diff --cached --check` PASS nella fase locale. |
| PR checks gate | SKIPPED | Gate runtime: non esiste PR al momento del commit documentale. Se checks non sono verificabili, il merge deve essere bloccato. |
| Final main clean gate | SKIPPED | Gate runtime post-merge: deve essere verificato nel report Bridge finale. |

## Validator obbligatori

| Comando | Esito | Note |
|---|---|---|
| `python validators\check_agent_skills.py --root . --write-index --write-score` | PASS | 22 skill, 0 errori, 0 warning. |
| `python validators\check_agent_skills.py --root . --fail-on-warning` | PASS | Modalita severa PASS. |
| `python -m unittest discover -s validators -p "test_*.py"` | PASS | 35 test. |
| `python -m pytest` | PASS | 78 passed. |
| `python validators\installed_skills_sync_check.py --root .` | PASS_WITH_WARNINGS | Cache ignorate, 0 blocking issues. |
| `python validators\release_workflow_check.py` | PASS | Required paths checked: 18; strategic skills checked: 3. |
| `python validators\smoke_trial_cases.py` | PASS | `SMOKE RESULT: PASS`. |
| `python validators\repo_health_check.py` | PASS_WITH_WARNINGS | Mixed-EOL storici e cache ignorate. |
| `python quick_validate.py as-common-codex-prompt-length-advisor` | SKIPPED | `quick_validate.py` assente; non creato. |

## Test specifici skill

| Comando | Esito | Note |
|---|---|---|
| `python -m pytest as-common-codex-prompt-length-advisor\tests` | PASS | 13 passed. |
| `python -m pytest as-common-model-effort-advisor\tests` | SKIPPED | Cartella test assente. |
| `python -m pytest as-common-web-ui-design-review\tests` | PASS | 6 passed. |
| `python -m pytest as-common-web-ui-linguistic-visual-qa\tests` | SKIPPED | Cartella test assente. |
| `python -m pytest as-common-deep-research-industriale\tests` | PASS | 4 passed. |
| `python -m pytest as-common-technical-patent-draft\tests` | PASS | 4 passed. |
| `python -m pytest as-common-business-email-draft\tests` | PASS | 4 passed. |
| `python -m pytest as-common-docs-runbook-builder\tests` | PASS | 4 passed. |
| `python -m pytest as-common-opencv-image-pipeline\tests` | PASS | 4 passed. |
| `python -m pytest as-common-python-fastapi-debug\tests` | PASS | 4 passed. |

## Regole publish

- Nessun gate FAIL e' presente nella fase locale.
- I gate SKIPPED sono solo runtime/post-PR e devono essere chiusi nel report Bridge.
- Se i PR checks falliscono o non sono verificabili, non fare merge.
- Se il final main clean gate fallisce, segnalare blocco nel report Bridge e non dichiarare PASS_MERGED.
