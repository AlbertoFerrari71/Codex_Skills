# 0340 Final Skills Release Audit

Data step: 2026-06-12

Branch step: `step-0340-0400-final-closure-asf-trial-adoption-pack`

## Decisione finale

RELEASE_READY_WITH_WARNINGS

Motivo: il catalogo skill e' coerente, i validator disponibili passano e non sono emersi duplicati o violazioni naming. Restano warning non bloccanti gia' noti: cache `__pycache__` ignorate dopo i test, mixed-EOL storici e assenza di `quick_validate.py`.

## Conteggio skill

| Voce | Valore |
|---|---:|
| Skill totali | 22 |
| Skill `as-common-*` | 22 |
| Skill con errori validator | 0 |
| Skill con warning validator | 0 |
| Skill con `StructureScore` 100 | 22 |

## Elenco skill `as-common-*`

- `as-common-agent-context-governor`
- `as-common-business-email-draft`
- `as-common-codex-command-pack`
- `as-common-codex-prompt-length-advisor`
- `as-common-codex-report-intake-decision-gate`
- `as-common-codex-step-manager`
- `as-common-deep-research-industriale`
- `as-common-docs-runbook-builder`
- `as-common-model-effort-advisor`
- `as-common-opencv-image-pipeline`
- `as-common-powershell-git-safe-flow`
- `as-common-project-instructions-builder`
- `as-common-project-riepilogo-operativo`
- `as-common-pwsh-command-pack`
- `as-common-python-fastapi-debug`
- `as-common-repo-readiness-review`
- `as-common-skill-authoring`
- `as-common-technical-patent-draft`
- `as-common-vba-excel-access-alberto`
- `as-common-verification-gate-test-eval-pack`
- `as-common-web-ui-design-review`
- `as-common-web-ui-linguistic-visual-qa`

## Naming e duplicati

| Controllo | Esito | Evidenza |
|---|---|---|
| Prefisso `as-common-` | PASS | Tutte le 22 cartelle attive usano il prefisso. |
| Minuscole e kebab-case | PASS | Nessuna cartella contiene underscore, spazi o accenti. |
| Campo `name` uguale alla cartella | PASS | Nessun mismatch rilevato. |
| Duplicati campo `name` | PASS | Nessun duplicato rilevato. |
| `SKILL.md` presente | PASS | Tutte le cartelle skill attive hanno `SKILL.md`. |

## Stato cataloghi

| Catalogo | Stato | Evidenza |
|---|---|---|
| `SKILLS_INDEX.md` | PASS | 22 skill, 0 errors, 0 warnings. |
| `SKILL_SCORE.md` | PASS | 22 skill, tutte con `StructureScore` 100. |
| Catalog freshness | PASS | `repo_health_check.py` passa il check catalog freshness. |

## Stato score

| Score | Stato | Note |
|---|---|---|
| `StructureScore` | PASS | 22/22 skill a 100. |
| `OperationalQualityScore` | PASS_WITH_WARNINGS | Due skill restano grade B: `as-common-technical-patent-draft` e `as-common-web-ui-design-review`. Non e' bloccante: nessun warning validator e boundaries documentati. |
| Recommendation | PASS | Nessuna skill richiede blocco release. |

## Stato trigger eval

| Voce | Stato |
|---|---:|
| Casi trigger eval totali | 124 |
| Skill coperte da casi trigger eval | 22 |
| Casi con negative boundaries | 124 |

Il trigger eval resta euristico: e' utile per collisioni note e regressioni di routing, ma non dimostra assenza assoluta di falsi positivi in uso reale.

## Stato smoke pack

| Area | Stato | Note |
|---|---|---|
| `validators/smoke_trial_cases.py` | PASS | Smoke validator eseguito con risultato `SMOKE RESULT: PASS`. |
| Smoke pack 0330 | PASS_WITH_WARNINGS | Pack documentale di real-use, non prova automatizzata su repository target. |
| Test skill specifici | PASS_WITH_SKIPS | Le cartelle test presenti passano; due skill richieste non hanno cartella `tests` e sono SKIPPED. |

## Stato install sync

`python validators\installed_skills_sync_check.py --root .` risulta PASS WITH NON-BLOCKING WARNINGS.

Warning rilevati:

- cache `__pycache__` ignorate dentro skill attive dopo l'esecuzione dei test;
- `_archive/backup-skills` ignorata come area backup inattiva;
- repo confermata dentro `.agents/skills`.

Nessuna azione correttiva distruttiva e' stata fatta: le cache non sono state cancellate indiscriminatamente.

## Warning noti

- Mixed-EOL storici su `.gitattributes`, `docs/asf_external_pilot/0870_CONTROLLED_WRITE_PILOT.md`, `docs/naming-conventions.md`, `docs/skill-authoring-guide.md`, `docs/skill-quality-checklist.md`.
- `quick_validate.py` non e' presente nel repository.
- Alcuni smoke restano documentali e non sostituiscono trial reali su repository applicativi.
- Il trigger eval resta una matrice di casi, non un router semantico completo.

## Rischi residui

- Falsi trigger possono emergere solo nell'uso reale cross-progetto.
- Le skill di confine, specialmente patent/research e UI design/UI linguistic QA, richiedono attenzione operativa nei prompt ambigui.
- Le cache Python possono ricomparire dopo i test; il sync checker le classifica come warning non bloccante.

## Conclusione

Il repository e' release-ready con warning noti e non bloccanti. Non serve aprire un nuovo ciclo grosso di hardening skill senza evidenza reale di falsi trigger o mancanze operative.
