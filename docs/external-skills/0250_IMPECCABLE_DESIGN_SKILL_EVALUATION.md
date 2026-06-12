# 0250 Impeccable Design Skill Evaluation

Data: 2026-06-12

Step: 0250) Codex Skills - Impeccable Design Skill Evaluation and Safe Adoption Plan

## Sintesi esecutiva

Impeccable e' una skill/toolchain esterna per migliorare interfacce frontend con un unico comando agente (`impeccable`), 23 sub-comandi, file di contesto progetto (`PRODUCT.md`, `DESIGN.md`), Live Mode browser e un detector deterministico da CLI. La valutazione conferma utilita' concreta per audit visuale, anti-AI-slop, accessibilita', responsive e design consistency nei progetti web.

La raccomandazione e' **Opzione A**: non installare Impeccable direttamente nel repository `Codex_Skills`; creare eventualmente in uno step futuro una skill wrapper leggera, conforme ad `as-common-*`, che incorpori solo il workflow utile per Alberto e tratti Impeccable come benchmark/tool esterno opzionale.

Motivo: la skill ufficiale si chiama `impeccable`, installa cartelle harness come `.agents/skills/impeccable`, usa Node/npm, include update check, puo' scrivere `PRODUCT.md`, `DESIGN.md`, `.impeccable/*` e varianti UI nei progetti target. Tutto questo e' utile nei progetti web, ma non e' adatto a essere importato come skill comune personale dentro questo catalogo senza isolamento e gate.

## Fonti analizzate

| Fonte | Accessibile | Versione/commit | Note |
|---|---:|---|---|
| https://github.com/pbakaus/impeccable | si | HEAD `92d6141cdf61f9943dfc8e2e46870e54e46d8641` | Repository ufficiale analizzato anche con clone shallow fuori repo. |
| https://impeccable.style/ | si | sito consultato 2026-06-12 | Home/docs marketing e descrizione funzionale. |
| https://impeccable.style/docs/ | si | sito consultato 2026-06-12 | Command reference generale. |
| https://impeccable.style/docs/critique/ | si | sito consultato 2026-06-12 | Flusso critique: review LLM + detector. |
| https://impeccable.style/docs/audit/ | si | sito consultato 2026-06-12 | Audit tecnico: a11y, performance, theming, responsive, anti-pattern. |
| https://impeccable.style/docs/live/ | si | sito consultato 2026-06-12 | Live Mode alpha, HMR e scrittura in source. |
| https://impeccable.style/privacy/ | si | last updated 2026-04-06 | Policy privacy del sito/skill/extension. |
| https://impeccable.style/changelog/ | si | letto 2026-06-12 | Update check, changelog CLI/skill/extension. |
| `git ls-remote https://github.com/pbakaus/impeccable HEAD` | si | `92d6141...` | Verifica read-only HEAD. |
| Clone esterno `D:\FG-SAB Dropbox\Alberto Ferrari\ChatGPT_Bridge\Codex_Skills\external_research\0250-impeccable` | si | `92d6141...` | Fuori repository `Codex_Skills`; non aggiunto a Git. |
| `npm view impeccable version license engines --json` | si | `2.3.2`, `Apache-2.0`, `node >=18` | Metadato registry. |
| `package.json` clonato | si | `2.3.2`, `Apache-2.0`, `node >=24` | Diverge da `npm view` sugli engines. |
| `README.md` | si | commit `92d6141...` | Include install, commands, Codex CLI paths. |
| `AGENTS.md` | si | commit `92d6141...` | Build/test/release policy e struttura. |
| `docs/HARNESSES.md` | si | last verified 2026-04-28 | Capabilities per harness, incluso Codex. |
| `HARNESSES.md` root | no | n/a | Non presente in root; documento equivalente trovato in `docs/`. |
| `skill/SKILL.src.md` | si | commit `92d6141...` | Fonte skill. |
| `.agents/skills/impeccable/SKILL.md` | si | commit `92d6141...` | Build distribuito per Codex. |
| `cli/bin/commands/skills.mjs` | si | commit `92d6141...` | Install, update, link, check. |
| `cli/engine/registry/antipatterns.mjs` | si | 41 regole | Registry detector. |
| `skill/scripts/context.mjs` | si | commit `92d6141...` | PRODUCT/DESIGN loader e update check. |

## Cosa fa Impeccable

Fatti verificati:

- Installa una skill agente chiamata `impeccable`.
- Espone il comando agente `/impeccable <command> <target>` o, in Codex, la skill invocabile come `$impeccable`.
- Consolida 23 comandi sotto una skill unica: `craft`, `shape`, `init`, `document`, `extract`, `critique`, `audit`, `polish`, `bolder`, `quieter`, `distill`, `harden`, `onboard`, `animate`, `colorize`, `typeset`, `layout`, `delight`, `overdrive`, `clarify`, `adapt`, `optimize`, `live`.
- Usa `PRODUCT.md` per contesto strategico e `DESIGN.md` per sistema visuale.
- Include un detector CLI deterministico con 41 regole.
- Include Live Mode per iterare elementi UI in browser e scrivere varianti nel source.
- Include build per piu' harness: `.agents`, `.claude`, `.cursor`, `.gemini`, `.github`, `.kiro`, `.opencode`, `.pi`, `.qoder`, `.trae`, `.trae-cn`, `.rovodev`.
- Per Codex distribuisce `.agents/skills/impeccable/` e subagent annidati sotto `<skill>/agents/`.

Ipotesi ragionevole:

- Il valore principale per Alberto non e' installare l'intera skill nel catalogo personale, ma importare un metodo di review UI: contesto progetto, audit visuale, detector, screenshot/live review quando disponibile, priorita' P0-P3.

## Struttura tecnica

| Area | Contenuto verificato | Impatto per Alberto |
|---|---|---|
| `skill/` | `SKILL.src.md`, `reference/`, `scripts/`, `agents/` | Fonte autoritativa della skill; troppo ampia per copia diretta. |
| `.agents/skills/impeccable/` | Build Codex con `SKILL.md`, reference, scripts, detector, agents | Installabile in Codex ma non conforme al naming `as-common-*`. |
| `cli/` | CLI `impeccable`, `skills install/update/link/check`, detector | Utile come tool esterno per progetti web; richiede Node/npm. |
| `extension/` | Browser extension detector | Utile ma fuori scope Codex_Skills. |
| `site/` | Documentazione Astro e changelog/privacy | Fonte pubblica utile per audit. |
| `tests/` | Test CLI, detector, live e skill behavior | Buon segnale manutentivo; non eseguiti in questo step. |
| Root harness folders | `.agents`, `.claude`, `.cursor`, ecc. | Sono artifact distribuiti e tracciati nel repo esterno. |

## Comandi e trigger rilevanti

| Comando | Scopo | Utilita' potenziale |
|---|---|---|
| `/impeccable init` | Crea contesto progetto e propone `PRODUCT.md`/`DESIGN.md` | Utile come idea, ma da tenere separato dalle nostre project instructions. |
| `/impeccable document` | Genera `DESIGN.md` da codice esistente | Utile per progetti web con design system minimo. |
| `/impeccable critique` | Review UX/design con score, personas e detector | Molto vicino alla futura skill wrapper consigliata. |
| `/impeccable audit` | Audit tecnico UI: a11y, performance, theming, responsive, anti-pattern | Complementare a verification gate; non sostituisce test tecnici. |
| `/impeccable polish` | Pass finale di refinement | Potenzialmente invasivo se usato senza gate. |
| `/impeccable harden` | Errori, i18n, overflow, edge cases | Utile ma da separare da QA tecnico generale. |
| `/impeccable live` | Browser variant mode con accettazione in source | Alto valore ma alto rischio operativo; pilot solo in repo web controllato. |
| `npx impeccable detect <target>` | Detector deterministic anti-patterns | Il componente piu' riusabile come gate opzionale. |
| `npx impeccable skills install/update/link/check` | Installazione e gestione skill | Da non eseguire nel catalogo `Codex_Skills`. |

## File generati o modificabili da Impeccable

| File/cartella | Quando | Rischio |
|---|---|---|
| `.agents/skills/impeccable/` | Install Codex project-local o user-wide | Viola naming `as-common-*` se installato nel catalogo personale. |
| `PRODUCT.md` | `/impeccable init` | Puo' sovrapporsi a project instructions, README o docs governance. |
| `DESIGN.md` | `/impeccable init` o `/impeccable document` | Utile, ma va trattato come design context, non istruzione Codex globale. |
| `.impeccable/live/config.json` | Setup Live Mode | Modifica progetto; richiede review. |
| `.impeccable/live/sessions/` | Live Mode | Stato locale operativo; da ignorare o gestire nel repo target. |
| `.impeccable/critique/<timestamp>__<slug>.md` | `/impeccable critique` | Snapshot utile, ma puo' creare rumore versionato se non governato. |
| File UI sorgenti | `polish`, `craft`, `live`, ecc. | Modifiche dirette a codice di prodotto; richiedono diff review e test. |

## Detector e validator

Fatti verificati:

- `node cli/bin/cli.js detect --help` ha funzionato nella copia esterna con Node locale `v24.13.0`.
- Il modulo `cli/engine/registry/antipatterns.mjs` esporta 41 regole.
- Il detector supporta file/directory, HTML statico, testo non HTML, URL via Puppeteer, JSON output e flag provider `--gpt`/`--gemini`.
- La documentazione pubblica indica uso in CI con exit code interpretabile.

Limiti:

- In questo step non e' stato eseguito `npx impeccable detect` su un progetto reale.
- Non sono state installate dipendenze e non sono stati avviati browser, dev server o Puppeteer.
- `README.npm.md` cita ancora `jsdom` e `--fast`, mentre il sorgente/changelog indicano che `--fast` e' deprecated/ignorato e il detector statico non usa piu' jsdom. Questo e' un segnale di documentazione parzialmente non allineata.

## Requisiti tecnici

| Requisito | Evidenza | Valutazione |
|---|---|---|
| Node/npm | `npm view` e `package.json` | Dipendenza reale. Non adatta a repo non Node senza pilot. |
| Node engine | `npm view`: `>=18`; `package.json`: `>=24`; README.npm: `24+` | Divergenza da chiarire prima di standardizzare. |
| Optional Puppeteer | CLI URL scan e Live/browser workflows | Alto rischio in sandbox o ambienti senza browser. |
| Build esterno | Bun, Astro, Playwright, provider SDK in devDependencies | Non serve per usare il pacchetto, ma aumenta complessita' se si fa fork. |
| Codex support | `.agents/skills/impeccable/`, `docs/HARNESSES.md`, `openai.yaml` | Supporto presente, ma naming e governance non compatibili con import diretto. |

## Licenza

Fatti verificati:

- `LICENSE` e `package.json` indicano `Apache-2.0`.
- Il copyright nel file LICENSE e' `Copyright 2025 Paul Bakaus`.

Valutazione:

- Apache-2.0 consente uso, modifica e redistribuzione con condizioni di attribuzione/licenza.
- In questo step non e' stato copiato codice sorgente di Impeccable nel repository `Codex_Skills`.
- Un futuro fork/vendor richiederebbe conservare licenza, avvisi e tracciamento modifiche. Non e' consigliato come primo passo.

## Privacy, telemetria e update check

Fatti verificati:

- La privacy policy dichiara che le skill testuali girano localmente, non raccolgono dati e non fanno analytics.
- Il sito usa Google Analytics; i download dal sito registrano evento bundle/timestamp senza dati personali dichiarati.
- La Chrome DevTools extension dichiara detection locale e preferenze salvate in Chrome sync.
- `skill/scripts/context.mjs` fa un update check best-effort verso `https://impeccable.style/api/version`, throttle giornaliero, cache in home utente, timeout 1200 ms.
- L'update check si puo' disattivare con `IMPECCABLE_NO_UPDATE_CHECK=1`.
- Il prompt generato dall'update check chiede all'agente di domandare prima di eseguire `npx impeccable skills update`.

Rischio:

- Anche se non invia contenuti progetto, il network check automatico e la cache in home sono comportamenti da dichiarare e disattivare in workflow supervisionati.
- Per progetti riservati o offline, default consigliato: `IMPECCABLE_NO_UPDATE_CHECK=1` e version pinning.

## Compatibilita' con Codex

Compatibile come tool esterno:

- Il build Codex usa `.agents/skills/impeccable/`.
- I subagent Codex sono annidati in `<skill>/agents/`.
- `docs/HARNESSES.md` indica Codex CLI come supportato e chiarisce che Codex usa `.agents/skills/` come directory nativa.

Non compatibile con import diretto in `Codex_Skills`:

- Il nome skill e' `impeccable`, non `as-common-*`.
- La description e' ampia e rischia collisioni con molte richieste frontend, QA e UX.
- La skill e' operativa e puo' scrivere file nei progetti target.
- Il suo workflow di init genera `PRODUCT.md`/`DESIGN.md`, potenzialmente sovrapposti alle nostre istruzioni di progetto.
- Install/update possono modificare cartelle skill provider e rinominare vecchi prefissi.

## Compatibilita' con convenzione `as-common-*`

| Criterio Codex_Skills | Impeccable ufficiale | Esito |
|---|---|---|
| Nome cartella con prefisso `as-common-` | `impeccable` | FAIL per import diretto. |
| Kebab-case/lowercase | si | PASS parziale. |
| Cartella = campo `name` | si | PASS nel proprio modello. |
| Scope piccolo e ripetibile | no, copre molti workflow UI | WARNING. |
| No install global non autorizzato | install supporta user-wide | WARNING. |
| No update automatico senza gate | update check chiede conferma | WARNING gestibile. |
| Nessuna skill operativa creata in questo step | rispettato | PASS. |

## Possibili usi nei progetti di Alberto

| Progetto/tipo | Uso potenziale | Note |
|---|---|---|
| Mansionario_Vivo | Audit UI admin, form, tabelle, responsive, microcopy, stati vuoti/errori | Usare come review/pilot su branch, non auto-polish su main. |
| AI Release Radar | Design review per dashboard/report web e project docs UI | Separare product UI da governance docs; utile per dashboard locali. |
| ASF Blueprint Studio | Audit e critique di interfacce workflow, dashboard, editor visuali | Alto valore, ma serve gate su screenshot e UX reale. |
| Family_Photo_Organizer_ASF | UI tool locale per archivi foto, stati di conferma e sicurezza | Priorita' sicurezza dati; evitare Live Mode invasivo senza backup. |
| Dashboard locali | Detector e audit per layout, contrasto, overflow, responsive | Buon candidato pilot. |
| Landing/presentazioni web | Critique brand/product e anti-template | Utile, ma richiede identita' visiva e immagini reali quando necessario. |

## Sovrapposizioni con skill esistenti

| Skill esistente | Sovrapposizione | Valutazione |
|---|---|---|
| `as-common-project-instructions-builder` | `PRODUCT.md`/`DESIGN.md` possono sembrare istruzioni progetto | Separare: project instructions = regole agente; PRODUCT/DESIGN = contesto UI. |
| `as-common-skill-authoring` | Naming, scope e futura skill wrapper | Usare per disegnare futura skill `as-common-*`. |
| `as-common-repo-readiness-review` | Preflight branch/status/test prima di UI step | Complementare, non duplicare. |
| `as-common-verification-gate-test-eval-pack` | Audit/gate e PASS/FAIL | Complementare: Impeccable copre design/UI, verification copre test/gate. |
| `as-common-codex-command-pack` | Prompt operativi e report | Non usare per review UI live; solo per handoff prompt. |
| `as-common-codex-step-manager` | Lifecycle step, report Bridge | Governa lo step, non fa design review. |
| `as-common-agent-context-governor` | Conflitti tra skill/AGENTS/project instructions | Utile se PRODUCT/DESIGN entra in collisione con AGENTS. |
| `as-common-codex-prompt-length-advisor` | Nessuna sovrapposizione operativa | Non toccata; utile solo se futuro prompt UI diventa troppo lungo. |

## Benefici

| Beneficio | Evidenza | Peso |
|---|---|---|
| Riduce output UI generico | Detector e regole anti-pattern mirate | Alto per progetti web. |
| Spinge contesto prodotto/design | `PRODUCT.md` e `DESIGN.md` | Alto se separato dalle istruzioni agente. |
| Offre audit pratico | `audit` e `critique` con severita'/score | Alto come review. |
| Codex supportato | Build `.agents` e subagent annidati | Medio, utile ma non basta per import diretto. |
| Detector deterministico | 41 regole, JSON, CLI | Alto come gate opzionale. |
| Licenza permissiva | Apache-2.0 | Medio, permette ispirazione/wrapper. |

## Rischi

| Rischio | Severita' | Mitigazione |
|---|---:|---|
| Installazione non conforme a `as-common-*` | alta | Non installare in `Codex_Skills`; eventuale wrapper nostro. |
| Modifica automatica skill installate | alta | Vietare `skills install/update` nel catalogo; pilot in repo target isolato. |
| Dipendenza Node/npm | media | Pilot solo in progetti Node/web; version pin; prerequisito Node esplicito. |
| Engines divergenti `>=18` vs `>=24` | media | Prima del pilot fissare runtime minimo e comando test. |
| Riuso/licenza | media | Non copiare sorgente; citare Apache-2.0; fork solo con nota licenza. |
| Manutenzione esterna | media | Treat as optional tool; non dipendere per gate obbligatori core. |
| Collisione con skill esistenti | media | Trigger wrapper stretto su web UI review, non governance generale. |
| Prompt troppo ampio | media | Wrapper instruction-only, niente catalogo completo di 23 comandi. |
| Design bello ma UX non reale | alta | Review deve partire da utenti, task, stati, dati reali e screenshot. |
| Privacy/update check | media | Disabilitare update check o chiedere consenso; no contenuti progetto a servizi esterni. |
| Assenza browser/live mode | media | Fallback su source review e screenshot statici; non bloccare se browser manca. |
| Workflow ASF supervisionato | alta | Sempre branch/status/test/diff gate; no auto-accept live edits. |
| Skill troppo generica | alta | Nome e description futuri devono essere stretti: review UI web, non "design everything". |
| UI curata ma poco funzionale | alta | PASS solo se task completion, a11y, responsive e microcopy sono verificati. |
| Confusione project instructions/UI QA | alta | `PRODUCT.md`/`DESIGN.md` restano design context, non AGENTS.md. |

## Decisione raccomandata

Decisione: **Opzione A - creare in futuro una nostra skill wrapper/ispirata, non installare Impeccable in `Codex_Skills`**.

Nome consigliato per lo step futuro: `as-common-web-ui-design-review`.

Motivazione:

- Il gap reale del catalogo Alberto e' una skill di review UI web, non un import integrale di una toolchain esterna.
- Impeccable offre idee forti: contesto `PRODUCT.md`/`DESIGN.md`, critique/audit separati, detector, severita', personas, anti-pattern, live review.
- L'install diretto creerebbe una skill `impeccable`, non conforme al prefisso obbligatorio, e potrebbe modificare skill/provider folders.
- Un wrapper nostro puo' restare instruction-only all'inizio, usare screenshot/browser quando disponibili, citare Impeccable come benchmark e lasciare il CLI come tool esterno opzionale per i singoli progetti web.

## Limiti della valutazione

- Non sono stati eseguiti install, update, link, build, test Impeccable, Puppeteer o Live Mode.
- Non e' stato eseguito detector su un progetto reale di Alberto.
- La valutazione della qualita' manutentiva si basa su repository/docs/sorgente, non su issue triage completo.
- La privacy policy e' stata letta come fonte dichiarativa; non e' stato fatto network tracing.
- Non e' stata fatta consulenza legale: la licenza Apache-2.0 e' stata registrata come fatto tecnico.
