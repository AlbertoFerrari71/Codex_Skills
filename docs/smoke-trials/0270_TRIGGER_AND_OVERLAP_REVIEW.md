# 0270) Trigger And Overlap Review

Data: 2026-06-12

Skill verificata: `as-common-web-ui-design-review`

## Positive Triggers Tested Mentally

| Trigger | Esito |
|---|---|
| "Fai review della dashboard AI Release Radar da screenshot" | positivo, skill appropriata |
| "Valuta questa web app locale da HTML/CSS senza browser" | positivo, con limite esplicito |
| "Controlla se questa landing sembra fatta dall'AI" | positivo, anti-AI-slop applicabile |
| "Audit visuale UX prima della release" | positivo se esiste evidenza UI |
| "Controlla gerarchia, spaziature, contrasto e microcopy" | positivo |
| "Review statica di template Jinja e CSS" | positivo, senza promettere accuratezza visuale |

## Negative Triggers

| Trigger | Skill corretta o azione | Esito |
|---|---|---|
| "Scrivi AGENTS.md o project instructions" | `as-common-project-instructions-builder` | web UI design review non deve attivarsi |
| "Fai repo readiness, branch, status, test e rischi tecnici" | `as-common-repo-readiness-review` | web UI design review non deve attivarsi |
| "Prepara un prompt Codex operativo" | `as-common-codex-command-pack` | web UI design review non deve attivarsi |
| "Gestisci uno step numerato con commit/push/PR" | `as-common-codex-step-manager` | web UI design review non deve gestire lifecycle |
| "Valuta se un prompt e' troppo lungo" | `as-common-codex-prompt-length-advisor` | web UI design review non deve attivarsi |
| "Segmenta immagini, soglie, omografia, QR" | `as-common-opencv-image-pipeline` | web UI design review non deve attivarsi |
| "Debug FastAPI, pytest o endpoint backend" | `as-common-python-fastapi-debug` | web UI design review non deve attivarsi |
| "Trova residui EN/IT/DE nel DOM e raw enum visibili" | `as-common-web-ui-linguistic-visual-qa` | design review puo restare secondaria |

## Overlap Review

| Skill | Confine |
|---|---|
| `as-common-project-instructions-builder` | istruzioni durevoli di progetto, AGENTS, Copilot, quality gate; non layout o UX visuale |
| `as-common-repo-readiness-review` | stato repo, branch, test, documenti e rischi tecnici; non giudizio UI |
| `as-common-codex-command-pack` | prompt operativo eseguibile; non audit UI |
| `as-common-codex-step-manager` | lifecycle step, gate, commit, PR e report; non review frontend |
| `as-common-codex-prompt-length-advisor` | lunghezza/integrita prompt e rischio contesto; non gerarchia o visual design |
| `as-common-opencv-image-pipeline` | pipeline immagini e computer vision; non UX di web app |
| `as-common-python-fastapi-debug` | backend Python/FastAPI/pytest; non layout e microcopy |
| `as-common-web-ui-linguistic-visual-qa` | i18n, residui lingua, DOM visible text, screenshot matrix e QA linguistica; puo affiancare ma non sostituire design review |

## Trigger Risk Notes

- Il termine "visual QA" compare nella skill design review e puo sovrapporsi
  alla skill `as-common-web-ui-linguistic-visual-qa` aggiunta dopo 0260.
- I casi in `validators/trigger_eval_cases.json` includono gia esempi positivi
  e negativi per separare design review da prompt length, command pack,
  project instructions, repo readiness, Python/FastAPI e linguistic visual QA.
- Non e' emerso un falso positivo concreto che richieda modifica immediata a
  `SKILL.md` o ai trigger eval.

## Possible Restriction

Nessuna restrizione necessaria in questo step. Se in futuro "visual QA" crea
ambiguita, restringere il trigger design review a layout, gerarchia, UX visuale,
component consistency, accessibility base e anti-AI-slop, lasciando i18n/DOM
text alla skill linguistica.

## Possible Addition

Nessuna aggiunta obbligatoria. Una futura micro-estensione utile potrebbe
menzionare esplicitamente che screenshot matrix multilingua e residui lingua
sono responsabilita primaria di `as-common-web-ui-linguistic-visual-qa`.

## Recommendation

Raccomandazione: nessuna modifica necessaria.

Motivo: i trigger esistenti sono abbastanza chiari per lo smoke trial 0270, e
la separazione con le skill operative e linguistiche e' verificabile senza
toccare skill, reference o validator.
