# 0280) Mature Skills Hardening Audit

Data: 2026-06-12

Step: 0280-0330) Codex Skills - Mature Skills Hardening, Trigger Boundaries and Real-Use Quality Pack

HEAD locale iniziale: `8228551a57ae06f8f4c5586cd5e8baa750ff1f55`

Conteggio skill: 22

## Scope

Audit complessivo delle skill `as-common-*` con hardening profondo limitato a:

- `as-common-deep-research-industriale`
- `as-common-technical-patent-draft`
- `as-common-business-email-draft`
- `as-common-opencv-image-pipeline`
- `as-common-python-fastapi-debug`
- `as-common-docs-runbook-builder`

Nessuna nuova skill e' necessaria: i gap rilevati sono confini, reference,
trigger eval e test contrattuali, non mancanze di dominio.

## Gate Iniziale

| Controllo | Esito |
|---|---|
| Branch iniziale | `main` |
| Working tree iniziale | clean |
| `HEAD` | `8228551a57ae06f8f4c5586cd5e8baa750ff1f55` |
| `origin/main` dopo fetch | `8228551a57ae06f8f4c5586cd5e8baa750ff1f55` |
| Ahead/behind | nessuno |
| `git diff --check` | PASS |
| `git diff --cached --check` | PASS |
| Validator read-only | PASS, 22 skill, 0 errori, 0 warning |

## Catalog Table

| Skill | Scopo sintetico | Maturita percepita | Trigger quality | Reference quality | Test quality | Overlap risk | Action consigliata |
|---|---|---|---|---|---|---|---|
| as-common-agent-context-governor | Governance conflitti contesto/istruzioni | Alta | Alta | Alta | Indiretta | Medio con repo readiness | Mantenere |
| as-common-business-email-draft | Email commerciali/tecniche/delicate | Media | Media | Assente | Assente | Medio con docs e patent | Harden |
| as-common-codex-command-pack | Prompt/command packet Codex | Alta | Alta | Alta | Validator | Medio con step manager | Mantenere |
| as-common-codex-prompt-length-advisor | Valutazione lunghezza prompt Codex | Alta | Alta | Alta | Alta | Basso | Mantenere |
| as-common-codex-report-intake-decision-gate | Decisione GO/NO_GO su report Codex | Alta | Alta | Alta | Validator | Medio con verification gate | Mantenere |
| as-common-codex-step-manager | Lifecycle step numerati Codex/ASF | Alta | Assente | Indiretta | Medio con command pack | Mantenere |
| as-common-deep-research-industriale | Ricerche industriali con fonti | Bassa-media | Debole | Assente | Assente | Alto con patent/email | Harden prioritario |
| as-common-docs-runbook-builder | Documentazione operativa persistente | Media | Media | Assente | Assente | Alto con project instructions | Harden |
| as-common-model-effort-advisor | Scelta livello/effort modello | Alta | Alta | Assente | Trigger eval | Medio con prompt length | Mantenere |
| as-common-opencv-image-pipeline | Pipeline immagini OpenCV | Media | Media | Assente | Assente | Medio con FastAPI/UI/patent | Harden |
| as-common-powershell-git-safe-flow | Verifica comandi PowerShell/Git | Alta | Assente | Indiretta | Medio con pwsh command pack | Mantenere |
| as-common-project-instructions-builder | Project Instructions/AGENTS/quality gate | Alta | Alta | Alta | Alta | Medio con docs runbook | Mantenere |
| as-common-project-riepilogo-operativo | Riepilogo operativo di ripartenza | Alta | Assente | Trigger eval | Medio con docs runbook | Mantenere |
| as-common-pwsh-command-pack | Command pack PowerShell completo | Alta | Alta | Alta | Validator | Medio con git safe flow | Mantenere |
| as-common-python-fastapi-debug | Debug Python/FastAPI/pytest | Media | Media | Assente | Assente | Medio con OpenCV/UI/Git | Harden |
| as-common-repo-readiness-review | Review iniziale read-only repo | Alta | Assente | Trigger eval | Medio con context governor | Mantenere |
| as-common-skill-authoring | Creazione/miglioramento skill | Alta | Alta | Assente | Trigger eval | Basso | Mantenere |
| as-common-technical-patent-draft | Disclosure e bozze tecniche brevetti | Bassa-media | Debole | Assente | Assente | Alto con research/legal/email | Harden prioritario |
| as-common-vba-excel-access-alberto | VBA/Excel/Access Alberto | Alta | Alta | Alta | Indiretta | Basso | Mantenere |
| as-common-verification-gate-test-eval-pack | Gate, smoke, eval, golden sample | Alta | Alta | Alta | Validator | Medio con report intake | Mantenere |
| as-common-web-ui-design-review | Review UX/UI web | Media-alta | Alta | Alta | Alta | Medio con linguistic QA | Mantenere |
| as-common-web-ui-linguistic-visual-qa | QA linguistica/visuale web | Alta | Media | Trigger eval | Medio con design review | Mantenere |

## Focus Candidate

| Skill | Gap principale | Priorita |
|---|---|---|
| as-common-deep-research-industriale | Anti-trigger assenti, fonti/uncertainty non abbastanza contrattuali | P0 |
| as-common-technical-patent-draft | Boundary legale e claim/FTO troppo sintetici | P0 |
| as-common-business-email-draft | Stile Alberto implicito, output varianti/rischi non contrattuale | P1 |
| as-common-docs-runbook-builder | Sovrapposizione con project instructions e riepilogo operativo | P1 |
| as-common-opencv-image-pipeline | Trigger tecnico utile ma poco delimitato da UI/FastAPI/patent | P2 |
| as-common-python-fastapi-debug | Trigger backend presenti ma senza anti-trigger e gate minimo | P2 |

## Rischi Generali Catalogo

- Le skill mature senza reference sono valide ma meno ripetibili.
- Trigger generici come email, debug, documento o ricerca possono causare routing sbagliato.
- Le skill documentali si sovrappongono se non separano runbook, project instructions, step manager e handoff chat.
- Le skill tecniche devono distinguere codice/debug da documentazione, brevetti e UI review.

## Conclusione

PROCEED.

Il catalogo e' coerente e non presenta blocchi globali. Procedere con
hardening mirato delle sei skill candidate, trigger eval e smoke pack, senza
creare nuove skill.
