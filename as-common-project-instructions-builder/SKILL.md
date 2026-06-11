---
name: as-common-project-instructions-builder
description: Use this skill when Alberto needs to create, audit, or refresh durable project instructions for ChatGPT Projects, Codex AGENTS.md, repository-wide agent rules, Copilot instructions, instruction templates, or quality gates. Do not use it for one-shot Codex prompts, numbered step lifecycle management, generic runbooks, or chat restart summaries.
---

# Scopo

Creare istruzioni di progetto compatte, coerenti e mantenibili per ChatGPT Projects, Codex e altri coding agent.

La skill serve quando Alberto avvia, consolida o ripulisce un progetto e vuole trasformare README, AGENTS.md, roadmap, decisioni, workflow, report e vincoli operativi in istruzioni efficaci.

# Quando usarla

Usala per:

- generare Project Instructions ChatGPT pronte da incollare;
- creare un documento esteso di supporto alle istruzioni;
- proporre o aggiornare un `AGENTS.md`;
- proporre `.github/copilot-instructions.md` quando utile;
- separare regole globali, regole progetto-specifiche e memoria storica;
- creare checklist e quality gate per validare le istruzioni;
- preparare un prompt Codex opzionale per installare i file generati.

# Quando non usarla

Non usarla per:

- preparare un prompt Codex temporaneo per un singolo step: usa `as-common-codex-command-pack`;
- gestire tutto il lifecycle di uno step numerato: usa `as-common-codex-step-manager`;
- scrivere un README o runbook generico senza focus sulle istruzioni agentiche: usa `as-common-docs-runbook-builder`;
- fare solo una readiness review tecnica read-only: usa `as-common-repo-readiness-review`;
- riconciliare conflitti puntuali tra fonti istruzione senza produrre istruzioni nuove: usa `as-common-agent-context-governor`;
- creare un riepilogo di ripartenza chat: usa `as-common-project-riepilogo-operativo`.

# Input richiesti

Raccogli o chiedi:

1. Nome progetto e repository.
2. Scopo operativo del progetto.
3. Ruolo atteso di ChatGPT.
4. Ruolo atteso di Codex o altri coding agent.
5. File fonte disponibili: `AGENTS.md`, README, changelog, roadmap, decisioni, workflow, runbook, report, prompt precedenti.
6. Vincoli non negoziabili: sicurezza, Git, PowerShell, Bridge, dati sensibili, dipendenze, deploy.
7. Output richiesti: compatto ChatGPT, documento esteso, AGENTS.md, Copilot, checklist, prompt Codex.

# Input opzionali

Usa se disponibili:

- branch principale e branch operativi tipici;
- comandi test/verifica;
- workflow di pubblicazione;
- esempi di report finale accettato;
- policy su commit, push, PR, merge e deploy;
- regole su file progressivi, Bridge, `LAST-*` e `latest-*`;
- lingua e tono preferiti;
- errori ricorrenti da evitare.

# Procedura

1. Identifica le fonti istruzione.
   - Mappa file versionati, prompt, report Bridge, memoria, chat e policy globali.
   - Considera autorevoli i file versionati correnti piu' dei riassunti di chat.
   - Non copiare segreti, token, password, chiavi, file `.env` o dati privati non necessari.
2. Classifica ogni contenuto.
   - Regole globali di Alberto.
   - Regole progetto-specifiche.
   - Istruzioni operative per ChatGPT.
   - Istruzioni operative per Codex.
   - Memoria storica.
   - Checklist o gate.
   - Rumore da escludere.
3. Riduci e risolvi.
   - Mantieni solo regole non ovvie e utili in esecuzione.
   - Elimina duplicazioni e istruzioni obsolete.
   - Evidenzia contraddizioni invece di nasconderle.
   - Se una regola e' rischiosa, richiedi autorizzazione esplicita o trasformala in divieto.
4. Genera output multi-livello.
   - Versione compatta ChatGPT Project Instructions.
   - Documento esteso di supporto.
   - `AGENTS.md` consigliato o patch consigliata.
   - `.github/copilot-instructions.md` opzionale.
   - Checklist di validazione.
   - Prompt Codex opzionale per applicare i file.
5. Applica il quality gate.
   - Usa `checklists/project-instructions-quality-gate.md`.
   - Segna PASS, WARNING o FAIL per ogni punto.
   - Non dichiarare pronte istruzioni non validate.
6. Concludi con proposta operativa.
   - File da creare/modificare.
   - Rischi residui.
   - Prossimo step consigliato.

# Separazione contenuti

| Tipo | Va nelle istruzioni? | Regola |
|---|---|---|
| Regole globali di Alberto | Solo se servono nel progetto | Non duplicare preferenze generiche se gia' stabili altrove. |
| Regole progetto-specifiche | Si | Devono essere concrete, verificabili e aggiornabili. |
| Istruzioni ChatGPT | Si | Spiegano come essere utile nel progetto. |
| Istruzioni Codex | Si, in `AGENTS.md` o sezione dedicata | Devono indicare poteri, limiti, test e report. |
| Memoria storica | No, salvo sintesi operativa | Spostare dettagli lunghi in docs o decision log. |
| Checklist/gate | Si, ma fuori dal testo compatto se lunga | Usare file separato o sezione dedicata. |
| Log, tentativi, report runtime | No | Restano Bridge o artefatti di step, non istruzioni permanenti. |
| Piano futuro | Solo prossimo step stabile | Non confondere roadmap e istruzioni operative. |

# Regole operative Alberto da preservare

Quando pertinenti, includi:

- lingua italiana salvo richiesta diversa;
- tono diretto, trasparente, senza preamboli inutili;
- FASE 1 / FASE 2 quando servono decisioni;
- domande chiuse A/B/C/D con default A quando il contesto lo consente;
- ChatGPT pianifica e revisiona, Codex esegue localmente, Alberto decide i passaggi strategici;
- nessun commit, push, PR, merge, deploy, reset, clean, rebase, force push o checkout distruttivo senza istruzione esplicita;
- `git --no-pager` per output lunghi;
- warning LF/CRLF non bloccanti se test e `git diff --check` passano;
- PowerShell semplice, script `.ps1` nel Bridge per flussi robusti, niente mega-blocchi fragili;
- Bridge con file progressivi deterministici; `LAST-*` e `latest-*` solo se il progetto li autorizza esplicitamente;
- report con stato, branch, file, test, warning, rischi, prossimo step e tempo se misurabile;
- semplicita', manutenzione e niente sovrastrutture inutili.

# Output atteso

Produci solo gli output richiesti. Se Alberto chiede il pacchetto completo, usa questo ordine:

1. `Project Instructions ChatGPT - versione compatta`
2. `Documento esteso`
3. `AGENTS.md consigliato`
4. `copilot-instructions.md opzionale`
5. `Checklist quality gate`
6. `Prompt Codex opzionale`

Per i prompt Codex opzionali:

- indicare file esatti da creare o modificare;
- vietare commit, push, PR, merge e deploy salvo richiesta esplicita;
- chiedere preflight Git e `git diff --check`;
- richiedere report finale con verifiche eseguite e non eseguite;
- non includere segreti o contenuti privati non necessari.

# Criteri di qualita'

Le istruzioni finali sono buone solo se:

- identificano il progetto e il suo obiettivo;
- spiegano il ruolo concreto di ChatGPT;
- spiegano il ruolo concreto di Codex se pertinente;
- separano regole globali e regole progetto-specifiche;
- sono concise e self-contained;
- non promettono automazioni non autorizzate;
- includono vincoli Git, sicurezza e dati sensibili quando pertinenti;
- indicano test, gate o verifica minima;
- hanno un prossimo step o regola di ripartenza;
- non contengono contraddizioni evidenti;
- non usano memoria storica come istruzione permanente;
- sono aggiornabili senza riscrivere tutto.

# Risorse

- `references/project-instructions-source-map.md` per classificare le fonti e decidere cosa includere.
- `templates/chatgpt-project-instructions-template.md` per la versione compatta ChatGPT.
- `templates/project-instructions-extended-template.md` per il documento esteso.
- `templates/agents-md-template.md` per `AGENTS.md`.
- `templates/copilot-instructions-template.md` per Copilot.
- `checklists/project-instructions-quality-gate.md` per la validazione finale.
- `examples/demo-prompts.md` per esempi di attivazione e anti-attivazione.
