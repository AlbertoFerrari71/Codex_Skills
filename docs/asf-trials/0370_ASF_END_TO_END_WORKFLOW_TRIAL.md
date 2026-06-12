# 0370 ASF End-To-End Workflow Trial

Data step: 2026-06-12

Repository: `C:\Users\alberto.ferrari\.agents\skills`

Branch step: `step-0340-0400-final-closure-asf-trial-adoption-pack`

## Scopo

Dimostrare che `Codex_Skills` puo' essere gestito con metodo ASF supervisionato: prompt preservato, gate iniziali, branch dedicato, modifiche allow-list, validator locali, PR, checks e merge solo se i gate passano.

Questo documento registra le evidenze disponibili prima del commit della branch. Le evidenze runtime successive alla creazione della PR, inclusi PR number, checks remoti, merge hash e verifica finale su `main`, sono registrate nel report Bridge `0340-0400-Report_Codex.md`, perche non sono conoscibili prima della pubblicazione della branch.

## Prompt Bridge

| Controllo | Esito | Evidenza |
|---|---|---|
| Prompt salvato nel Bridge | PASS | `D:\FG-SAB Dropbox\Alberto Ferrari\ChatGPT_Bridge\Codex_Skills\codex_command\0340-0400-Prompt_Codex.md` |
| Clipboard | PASS | Non usata. |
| File `LAST-*` | PASS | Non creati. |
| File `latest-*` | PASS | Non creati. |
| Marker finale | PASS | `END_OF_PROMPT_0340_0400` presente come ultima riga non vuota. |
| Sezione `REGOLE FINALI` | PASS | Presente. |

## Preflight

| Comando | Esito | Evidenza |
|---|---|---|
| `git status --short` | PASS | Output vuoto. |
| `git --no-pager branch --show-current` | PASS | `main`. |
| `git fetch origin` | PASS | Exit code 0. |
| `git --no-pager rev-parse HEAD` | PASS | `845f476220f6a4dfc25dda953d7fbfb6078c9ce8`. |
| `git --no-pager rev-parse origin/main` | PASS | `845f476220f6a4dfc25dda953d7fbfb6078c9ce8`. |
| `git --no-pager diff --check` | PASS | Exit code 0. |
| `git --no-pager diff --cached --check` | PASS | Exit code 0. |

## Branch

| Passo | Esito | Evidenza |
|---|---|---|
| Branch iniziale | PASS | `main`. |
| Branch lavoro | PASS | `step-0340-0400-final-closure-asf-trial-adoption-pack`. |
| Creazione branch | PASS | `git switch -c step-0340-0400-final-closure-asf-trial-adoption-pack`. |

## Modifiche allow-list

File previsti dallo step:

- `CHANGELOG.md`
- `docs/roadmap.md`
- `SKILLS_INDEX.md`, solo se il validator produce diff reale
- `SKILL_SCORE.md`, solo se il validator produce diff reale
- `docs/quality/0340_FINAL_SKILLS_RELEASE_AUDIT.md`
- `docs/quality/0350_INSTALLED_SKILLS_SYNC_AND_CATALOG_INTEGRITY.md`
- `docs/adoption/0360_ACTIVE_PROJECTS_SKILL_ADOPTION_MATRIX.md`
- `docs/asf-trials/0370_ASF_END_TO_END_WORKFLOW_TRIAL.md`
- `docs/quality/0380_FINAL_CLOSURE_NOTES_AND_KNOWN_ISSUES.md`
- `docs/quality/0390_SKILLS_RELEASE_READINESS_GATE.md`

Nessuna skill `SKILL.md` e' stata modificata in questo trial perche non sono emersi blocchi funzionali.

## Test e validator locali

| Comando | Esito | Note |
|---|---|---|
| `python validators\check_agent_skills.py --root . --write-index --write-score` | PASS | 22 skill, 0 errori, 0 warning. |
| `python validators\check_agent_skills.py --root . --fail-on-warning` | PASS | 22 skill, 0 errori, 0 warning. |
| `python -m unittest discover -s validators -p "test_*.py"` | PASS | 35 test. |
| `python -m pytest` | PASS | 78 passed. |
| `python validators\installed_skills_sync_check.py --root .` | PASS_WITH_WARNINGS | 9 cache ignorate, 0 blocking issues. |
| `python validators\release_workflow_check.py` | PASS | Required paths checked: 18, strategic skills checked: 3. |
| `python validators\smoke_trial_cases.py` | PASS | `SMOKE RESULT: PASS`. |
| `python validators\repo_health_check.py` | PASS_WITH_WARNINGS | Cache ignorate e mixed-EOL storici. |
| `python quick_validate.py as-common-codex-prompt-length-advisor` | SKIPPED | `quick_validate.py` non presente. |

## Publish runtime checklist

| Fase | Stato in questo documento | Regola runtime |
|---|---|---|
| Diff check pre-staging | PASS | Deve restare PASS prima del commit. |
| Cached diff check pre-staging | PASS | Deve restare PASS dopo staging allow-list. |
| Commit | PENDING_RUNTIME | Solo file dello step. |
| Push branch | PENDING_RUNTIME | Solo branch dedicata. |
| PR | PENDING_RUNTIME | Titolo `0340-0400 final skills closure and ASF trial`. |
| PR checks | PENDING_RUNTIME | Se non verificabili, non merge. |
| Merge | PENDING_RUNTIME | Solo se checks PASS. |
| Final main verification | PENDING_RUNTIME | Main clean e `HEAD == origin/main`. |
| Report Bridge | PENDING_RUNTIME | `0340-0400-Report_Codex.md`. |

## Conclusione trial

Il trial e' pronto per la fase publish se i gate finali locali restano PASS e lo staging contiene solo file allow-list. Le parti non conoscibili prima della PR sono deliberately runtime-gated e devono essere chiuse nel report Bridge finale.
