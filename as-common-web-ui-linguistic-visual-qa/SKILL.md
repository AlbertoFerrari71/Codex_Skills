---
name: as-common-web-ui-linguistic-visual-qa
description: Use this skill for multilingual web UI linguistic and visual QA on local web apps or dashboards: i18n checks, baseline-language residue, raw enum/status labels, DOM visible-text extraction, browser or headless fallback walkthroughs, screenshot matrix, mobile/desktop overflow, and merge-readiness review. Do not use it for generic translation, email, Excel/VBA, OpenCV, image generation, scheduler changes, or merge without review.
---

# Scopo

Eseguire QA linguistica e visuale di web app, dashboard e frontend locali con attenzione a:

- i18n e cataloghi lingua;
- residui della lingua baseline nelle lingue target;
- enum, stati e codici tecnici esposti come label utente;
- DOM extraction del testo visibile;
- browser walkthrough e fallback dichiarati;
- screenshot desktop/mobile;
- overflow, badge, card, pulsanti, header, nav e testi tagliati;
- report Bridge con evidenze;
- decisione di readiness per merge umano.

La skill struttura il controllo. Non sostituisce la skill `as-common-web-ui-design-review` per review UX/visual generale quando non ci sono rischi linguistici, i18n o DOM text QA.

# Quando usarla

Usala per richieste come:

- verifica dashboard web multilingua;
- QA visuale pagina web con screenshot;
- ci sono parole inglesi nella UI italiana;
- controlla traduzioni FR/DE/ES;
- controlla i18n e fallback lingua;
- naviga sito pagina per pagina;
- verifica testi tagliati, badge e card troppo stretti;
- browser walkthrough o screenshot matrix;
- controlla layout mobile/desktop;
- verifica enum tecnici esposti nella UI;
- review PR UI/web prima del merge;
- DOM text extraction e classificazione sospetti.

# Quando non usarla

Non usarla per:

- tradurre solo un testo generico;
- scrivere o correggere email;
- fare ricerca brevetti;
- analizzare Excel, Access o VBA;
- modificare codice C++/OpenCV;
- preparare business plan;
- generare o modificare immagini;
- modificare scheduler, servizi o processi esterni;
- inviare email;
- fare merge senza review;
- audit backend/API senza superficie UI.

# Input

Chiedi o deduci questi dati prima di partire:

- repo path e nome progetto;
- base branch, branch o PR target;
- modalita Git: solo report, micro-fix controllato o PR draft;
- comando server locale, host/porta preferita e porte fallback;
- base URL;
- lingue target e lingua baseline;
- pagine minime da controllare ed eventuale pagina dettaglio;
- endpoint tecnici/API da tenere separati dalla UI;
- allowlist termini, nomi prodotto e termini vietati/sospetti;
- viewport desktop/mobile;
- cartella Bridge evidenze;
- comandi test/validator;
- pulsanti o azioni da non premere.

Se un dato manca, usa una ipotesi esplicita solo se e' a basso rischio. Altrimenti chiedi un chiarimento o chiudi con `BLOCKED_AMBIGUOUS_SCOPE`.

# Procedura

## Fase 0 - Safety preflight

1. Verifica repo corretto, branch atteso e working tree.
2. Non usare reset, clean, rebase, force push o `--no-verify`.
3. Non attivare scheduler, email, deploy, tag, release o LLM a runtime.
4. Non premere pulsanti operativi nella web app durante il QA.
5. Non fare merge automatico. La decisione finale resta umana salvo policy esplicita diversa.
6. In modalita read-only, non modificare il repo target e salva evidenze solo nel Bridge o in una cartella temp dichiarata.

## Fase 1 - Analisi contesto

1. Leggi report precedenti, diff PR e istruzioni repo.
2. Leggi cataloghi i18n, template, componenti, CSS e formatter di stati/codici.
3. Identifica pagine principali, lingue, route, endpoint tecnici e dati grezzi.
4. Separa UI HTML navigabile da API JSON, log, report raw e file tecnici.

## Fase 2 - Avvio server locale

1. Avvia solo server locali necessari al QA read-only.
2. Usa la porta preferita o una fallback libera, documentando host e porta.
3. Non fermare processi non avviati dallo step.
4. Registra PID/comando quando possibile e ferma solo il server avviato dallo step.

## Fase 3 - Browser e fallback

1. Prova l'in-app Browser Codex quando disponibile.
2. Se il browser non funziona, non dichiarare browser QA fittizia.
3. Usa un fallback reale disponibile: Chrome headless, Playwright, Selenium o HTTP DOM extraction.
4. Salva screenshot e testo visibile per pagina/lingua.
5. Dichiara sempre metodo, limiti e copertura effettiva.

## Fase 4 - DOM linguistic scan

1. Estrai testo visibile per pagina e lingua.
2. Cerca residui della lingua baseline nelle lingue target.
3. Cerca enum raw, codici stato, placeholder non localizzati e fallback `n/a`.
4. Cerca parole sospette non allowlistate: error, pass, hold, warning, status, run, prompt, action, review, gate, scheduler e simili.
5. Usa match con confini parola e case appropriato per token brevi: non classificare `pass` dentro `passo` o `verpasste`, e conserva snippet/contesto.
6. Distingui testo originale/dinamico mostrato come dato sorgente, report raw collassati, endpoint JSON e label UI localizzata.
7. Classifica ogni sospetto come:
   - difetto reale;
   - residuo ammesso;
   - falso positivo;
   - endpoint tecnico;
   - dato tecnico grezzo;
   - lingua baseline;
   - testo originale/dinamico;
   - report raw o sezione collassata;
   - falso positivo substring.

## Fase 5 - Visual QA

1. Cattura screenshot desktop per pagina/lingua prioritaria.
2. Cattura almeno mobile IT dashboard e una pagina target critica in lingua lunga, se richiesto.
3. Verifica overflow, parole spezzate, badge stretti, card, bottoni, header, nav e testi uppercase lunghi.
4. Controlla valori tecnici lunghi, report raw e layout responsive.
5. Non introdurre test pixel-perfect salvo motivo forte e documentato.

## Fase 6 - Micro-fix controllati

1. Correggi solo difetti reali nel perimetro autorizzato.
2. Preferisci formatter centralizzati, mapping enum e cataloghi i18n.
3. Evita find/replace cieco e traduzioni disperse nei template.
4. Non fare redesign, refactor ampi o modifiche backend non necessarie.
5. Aggiungi test non fragili solo dove riducono rischio reale.

## Fase 7 - Test e gate

Esegui i gate disponibili e pertinenti:

- unit test;
- validator o smoke test;
- `git diff --check` e, se c'e staging, `git diff --cached --check`;
- help CLI/web o health check locali;
- PR status check se disponibile e autorizzato.

Se un gate fallisce, correggi solo nel perimetro autorizzato. Altrimenti chiudi con `BLOCKED_TEST_FAILURE` o `PARTIAL_PR_NEEDS_FIX`.

## Fase 8 - Report e decisione

Il report deve includere:

- stato finale;
- pagine e lingue verificate;
- metodo browser/fallback;
- screenshot, visible text e DOM suspects;
- termini corretti, residui ammessi e falsi positivi;
- problemi grafici;
- test/gate;
- conferma read-only o micro-fix;
- decisione merge/no merge;
- prossimo step.

# Stati finali

- `PASS_READY_FOR_HUMAN_MERGE`: QA completo, nessun fix richiesto, gate PASS, merge solo umano.
- `PASS_WITH_MICROFIX_READY_FOR_HUMAN_MERGE`: micro-fix autorizzati applicati e verificati, merge solo umano.
- `PASS_PR_DRAFT`: branch/PR draft creati e gate PASS, nessun merge.
- `PASS_LOCAL_ONLY`: evidenze locali/Bridge complete, nessuna pubblicazione richiesta.
- `PARTIAL_PR_NEEDS_FIX`: PR o lavoro parziale con finding ancora da correggere.
- `BLOCKED_GIT_STATE`: repo, branch o working tree non permettono procedere in sicurezza.
- `BLOCKED_BROWSER_QA`: browser e fallback equivalenti non disponibili, impossibile dichiarare QA visuale.
- `BLOCKED_TEST_FAILURE`: gate richiesto fallisce fuori dal perimetro correggibile.
- `BLOCKED_AMBIGUOUS_SCOPE`: input o permessi ambigui rendono rischiosa l'esecuzione.

# Allowlist generica

Ammessi come dati tecnici, non come label utente:

- nome software/prodotto;
- URL, path, ID tecnici, nomi file;
- endpoint API;
- `run_id` e chiavi sorgente se chiaramente dati tecnici;
- codici JSON raw solo in endpoint tecnici;
- nomi task/scheduler se mostrati come dato tecnico;
- titoli, snippet o ragioni originali in lingua sorgente quando la UI li etichetta chiaramente come contenuto originale;
- app English-baseline quando non esistono lingue target richieste.

Non ammessi nella UI localizzata, salvo eccezioni esplicite:

- enum grezzi;
- codici stato usati come label;
- residui lingua baseline;
- label tecniche non tradotte;
- placeholder non localizzati;
- fallback `n/a` non localizzato;
- testi hardcoded in template.

# Anti-pattern

Evita:

- dichiarare browser QA senza browser o fallback equivalente;
- confondere endpoint JSON con UI utente;
- tradurre path, ID, URL o nomi file;
- fare find/replace cieco;
- disperdere traduzioni nei template;
- mostrare enum raw nella UI;
- nascondere dati tecnici invece di presentarli bene;
- creare test pixel-perfect fragili;
- fare redesign non richiesto;
- premere pulsanti operativi durante QA;
- modificare scheduler o processi esterni;
- fare merge automatico;
- fare pulizia Git distruttiva;
- classificare substring brevi come difetti senza confini parola;
- contare testo raw/collassato come label UI visibile senza verificarne lo stato visuale.

# Output standard

Cartella Bridge:

```text
web_smoke/<step>_web_ui_linguistic_visual_qa_<timestamp>
```

File attesi:

- `Visual_QA_Matrix.md`
- `DOM_Suspects.json`
- `Review_Notes.md`
- `Server_Info.json`
- `Server_Stop_Info.json`
- `visible_text_<lang>_<page>.txt`
- `<lang>_<page>.png`
- `<lang>_<page>_mobile.png`
- `Report_Codex.md`

# Risorse incluse

- Prompt template: `templates/web-ui-linguistic-visual-qa-prompt.md`.
- Checklist operativa: `checklists/web-ui-linguistic-visual-qa-checklist.md`.
- Case study: `examples/ai-release-radar-1360-case-study.md`.
- Fixture statica: `examples/fixture-web-ui-qa-sample.html`.
- Adoption runbook: `docs/web-ui-linguistic-visual-qa-adoption.md`.