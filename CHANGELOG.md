# CHANGELOG

## 0340-0400) Final Skills Closure, ASF Trial And Adoption Pack

Chiusura finale del ciclo skill dopo 0280-0330, senza creare nuove skill e senza refactor ampi.

- aggiunti audit finale release, sync/catalog integrity, adoption matrix, ASF end-to-end trial, known issues e readiness gate;
- confermato catalogo a 22 skill con 0 errori e 0 warning nel validator catalogo;
- confermati 124 casi trigger eval con copertura di tutte le 22 skill;
- documentata adozione logica sui progetti attivi di Alberto senza audit tecnico dei repository esterni;
- mantenuti visibili warning non bloccanti: cache `__pycache__`, mixed-EOL storici, assenza `quick_validate.py`, smoke documentali;
- nessuna skill modificata e nessuna normalizzazione line endings.

## 0280-0330) Mature Skills Hardening, Trigger Boundaries And Real-Use Quality Pack

Rafforzamento mirato di sei skill mature del catalogo senza creare nuove skill.

- hardenate `as-common-deep-research-industriale`,
  `as-common-technical-patent-draft`, `as-common-business-email-draft`,
  `as-common-docs-runbook-builder`, `as-common-opencv-image-pipeline` e
  `as-common-python-fastapi-debug`;
- aggiunti trigger, anti-trigger, output contract, reference leggere e test
  contrattuali per le sei skill candidate;
- esteso `validators/trigger_eval_cases.json` con 44 casi positivi, negativi e
  borderline per ridurre overlap con project instructions, command pack, step
  manager, prompt length, model effort, UI review, OpenCV, FastAPI, VBA,
  research e patent draft;
- creati audit e report qualità 0280-0330 in `docs/quality/` e smoke pack
  documentale in `docs/smoke-trials/`;
- aggiunto `pytest.ini` minimale per consentire `python -m pytest` con piu
  file `tests/test_skill_contract.py` in cartelle skill kebab-case;
- nessuna installazione esterna, nessuna nuova skill, nessuna normalizzazione
  EOL intenzionale.

## 270) Web UI Design Review Smoke Trial And Catalog Consistency Check

Verifica reale della skill `as-common-web-ui-design-review` e dello stato del
catalogo skill dopo gli step successivi alla pubblicazione 0260.

- confermata coerenza locale, `origin/main`, GitHub API e raw GitHub con 22
  skill totali;
- chiarito che l'atteso 21 skill del report 0260 e' uno snapshot storico
  superato dai commit successivi `1370-1450` e `1460`;
- aggiunto smoke trial read-only su `AI_Release_Radar` usando template, CSS e
  documenti UI, senza browser/server e senza modifiche al repo target;
- aggiunta review trigger/overlap per distinguere design review da project
  instructions, repo readiness, command pack, step manager, prompt length,
  OpenCV, Python/FastAPI e linguistic visual QA;
- nessuna installazione Impeccable, nessuna modifica a skill operative,
  cataloghi o repository target.

## 1460) Web UI Linguistic Visual QA Adoption Matrix

Piano di adozione della skill `as-common-web-ui-linguistic-visual-qa` sui progetti web/dashboard attivi.

- aggiunta matrice di priorita per AI Release Radar, ASF Blueprint Studio, Mansionario Vivo, Family Photo Organizer, AI Software Factory e candidato ambiguo AI Software Factory 2;
- aggiunto piano operativo con ordine pilot, safety read-only, gestione progetti sensibili e regole anti-contaminazione;
- nessuna modifica ai repo target e nessun server target avviato;
- nessuna modifica a skill, `SKILLS_INDEX.md`, `SKILL_SCORE.md` o trigger eval.

## 1370-1450) Web UI Linguistic Visual QA Skill Pack

Creazione della skill comune `as-common-web-ui-linguistic-visual-qa` per QA linguistica e visuale di web app/dashboard locali.

- aggiunta skill instruction-only per i18n, residui lingua baseline, enum raw, DOM text extraction, browser walkthrough, fallback headless/HTTP, screenshot matrix e merge readiness;
- aggiunti prompt template, checklist pratica, case study AI Release Radar 1360, fixture HTML statica e runbook di adozione;
- estesi i casi trigger-eval positivi e negativi per distinguere QA linguistica/visuale da design review, prompt Codex, email, Excel, brevetti e OpenCV;
- pianificati pilot read-only su AI Release Radar e secondo pilot/fixture con evidenze Bridge;
- nessuna dipendenza esterna o runtime LLM aggiunta.

## 260) Web UI Design Review Skill Pilot

Pubblicazione dei documenti 0250 su Impeccable e creazione della skill comune `as-common-web-ui-design-review`.

- aggiunta skill instruction-only per review UI web, dashboard, landing e visual QA;
- aggiunti reference su checklist, rubric P0/P1/P2/P3, input modes e anti-AI-slop;
- aggiunto test di contratto della skill senza dipendenze esterne;
- estesi i casi trigger-eval per distinguere review UI da project instructions, prompt length, repo readiness, command pack e step manager;
- confermato che Impeccable resta benchmark/tool esterno opzionale: non installato, non vendorizzato, senza dipendenza Node/npm/browser obbligatoria.

## 250) Impeccable Design Skill Evaluation

Valutazione documentale della skill esterna Impeccable e piano di adozione sicura per workflow web/UI.

- aggiunta valutazione in `docs/external-skills/0250_IMPECCABLE_DESIGN_SKILL_EVALUATION.md`;
- aggiunto piano di adozione in `docs/external-skills/0250_IMPECCABLE_SAFE_ADOPTION_PLAN.md`;
- aggiunto mapping verso skill Codex esistenti in `docs/external-skills/0250_IMPECCABLE_MAPPING_TO_CODEX_SKILLS.md`;
- confermata raccomandazione: non installare Impeccable in `Codex_Skills`, valutare futura skill wrapper `as-common-web-ui-design-review`;
- nessuna skill operativa creata o modificata; cataloghi skill non rigenerati.

## 220) Codex Prompt Length Advisor Skill

Nuova skill comune per valutare lunghezza, integrita', rumore e rischio di
crescita contesto dei prompt Codex.

- aggiunta skill `as-common-codex-prompt-length-advisor`;
- aggiunto script CLI standard-library per output testuale e JSON;
- aggiunte reference su soglie, integrita' prompt e crescita contesto runtime;
- aggiunti test unitari per soglie, stdin, JSON, integrity, runtime risk e publish safety;
- aggiunti casi trigger-eval mirati per evitare collisioni con command pack, step manager, model effort e verification gate;
- rigenerati `SKILLS_INDEX.md` e `SKILL_SCORE.md`.

## 190) Model Effort Advisor Skill

Nuova skill comune per scegliere il livello ChatGPT adeguato a compiti ordinari, tecnici e ASF/Codex.

- aggiunta skill `as-common-model-effort-advisor`;
- definita matrice Alberto/ASF per Istantanea, Media, Alta, Extra Elevata, Pro Standard e Pro Estesa;
- aggiunte regole di onesta' sul livello corrente non verificabile e sul mancato cambio automatico del modello;
- aggiunti casi trigger-eval mirati per evitare collisioni con prompt Codex, report intake e skill authoring;
- rigenerati `SKILLS_INDEX.md` e `SKILL_SCORE.md`.

## 180) Trigger eval and project instructions adoption review

Verifica di adozione della skill `as-common-project-instructions-builder` e
rafforzamento dei casi trigger-eval per ridurre collisioni con skill affini.

- aggiunto documento `docs/project-instructions/0180_PROJECT_INSTRUCTIONS_ADOPTION_REVIEW.md`;
- esteso `validators/trigger_eval_cases.json` con casi positivi, negativi e borderline;
- confermato che la UI ChatGPT resta fatto dichiarato da Alberto, non verificabile localmente;
- mantenuti invariati skill, `AGENTS.md` e smoke trial per evitare rumore.

## 170) Install and publish project instructions builder

Review e pubblicazione della skill `as-common-project-instructions-builder`.

- aggiunta sezione compatta in `AGENTS.md` per il project instructions builder workflow;
- registrata nel documento applicativo la decisione di non creare Copilot instructions;
- confermata pubblicazione solo dopo review semantica, gate locali, PR e merge.

## 160) Project Instructions Builder

Nuova skill comune per creare istruzioni di progetto ChatGPT/Codex mantenibili.

- aggiunta skill `as-common-project-instructions-builder`;
- aggiunti template per Project Instructions, documento esteso, `AGENTS.md` e Copilot;
- aggiunta checklist quality gate per istruzioni di progetto;
- creata prima applicazione reale per `Codex_Skills` in `docs/project-instructions/`;
- aggiunti casi trigger-eval per distinguere istruzioni progetto da prompt temporanei, runbook e riepiloghi.

## 0905) PowerShell, Bridge and Codex Skill Hardening

Rafforzamento operativo dalle lezioni emerse durante la pubblicazione ASF STEP 0900.

- preferenza al file Bridge progressivo prima di `LAST-*`, con controllo coerenza;
- diagnostiche Git dirette per gate critici e output/exit code salvati;
- divieto operativo di here-string Markdown lunghe nei blocchi da incollare;
- stop su `git diff --cached --check` prima di Phase B/pubblicazione;
- procedura EOF blank-line mirata solo sui file segnalati, con backup e ristaging selettivo;
- aggiunto test di regressione sui concetti 0905.

## 150) Installed Skills Sync Checker

Controllo read-only dello stato installato delle skill rispetto a Git e ai cataloghi generati.

- aggiunto `validators/installed_skills_sync_check.py`;
- controllate skill attive, `SKILL.md`, frontmatter `name:`, Git tracking e cataloghi;
- gestiti `_archive/backup-skills/` e file locali a rischio con policy esplicita;
- integrato lo sync checker nel repository health check;
- aggiunti test unitari dedicati;
- documentato il comando principale e i limiti read-only.

## 140) Skill Trigger & Content Cleanup Pack

Pulizia mirata dei confini di triggering tra skill vicine.

- chiariti description, anti-trigger e cross-reference delle skill in overlap;
- separati prompt Codex, lifecycle step e documentazione persistente;
- separati riepilogo di ripartenza e runbook persistente;
- aggiunte micro-regole per distinguere PowerShell command pack e Git safe flow;
- separati gate/test design da intake di report finale Codex;
- separati repo readiness tecnica e governance del contesto agente;
- documentata policy lingua/trigger delle description.

## 130) Scoring v2 & Trigger Eval Foundation

Fondazione dello scoring v2 e della base trigger-eval deterministica.

- separati `StructureScore` e `OperationalQualityScore`;
- aggiornato `SKILL_SCORE.md` con i due punteggi e raccomandazioni;
- rimossi punti cosmetici per cartelle `references/` ed `examples/` vuote;
- aggiunta base trigger-eval deterministica con casi positivi/negativi;
- aggiunti test unitari per scoring v2 e trigger-eval;
- documentati comandi, limiti euristici e fuori scope.

## 120) Validator Hardening & Automation Gate

Rafforzamento dei gate locali e remoti del catalogo skill.

- esteso scan valori sensibili a docs, templates, file root e GitHub workflow;
- aggiunto controllo catalog freshness per `SKILLS_INDEX.md` e `SKILL_SCORE.md`;
- aggiunto link-check minimale per riferimenti `references/` ed `examples/`;
- rafforzato `validators/repo_health_check.py` come runner unico;
- aggiunta GitHub Action `Validate Codex Skills`;
- aggiornati test e documentazione validator.

## 100) Skill Release Workflow Pack

Creazione del workflow stabile per rilasciare nuove skill o modificare skill esistenti.

- release workflow documentato;
- checklist release;
- authoring/modification flow;
- AI Software Factory handoff;
- release decision gate;
- template release prompt;
- release checker opzionale;
- cataloghi rigenerati.

## 090) Skill Smoke Trial Pack

Creazione del pacchetto di smoke trial per skill strategiche e command pack.

- smoke trial delle tre skill strategiche;
- edge cases strani;
- PowerShell command pack trial;
- report intake trial;
- validator smoke cases;
- cataloghi rigenerati.

## 085) PowerShell Command Pack Hardening Rules

Rafforzamento dello standard per command pack PowerShell/Git non banali.

- integrated 20 hardening rules;
- documented direct main push policy D3-C;
- added robust Git parsing and diff cached checks;
- added real `.ps1` payload requirement;
- added DOCX non-blocking and temp path rule;
- added clipboard-on-failure rule;
- regenerated catalog and score.

## 080) PowerShell Paste Termination Hotfix

Correzione della guida sulla terminazione dei blocchi PowerShell copiati/incollati.

- corrected PowerShell paste termination guidance;
- removed reliance on final `Write-Host ";";`;
- documented one useful command plus two fake lines rule;
- documented two or more useful commands plus one fake line rule;
- recommended `.ps1` execution for long or critical flows;
- regenerated catalog and score.

## 070) Codex Report Intake Decision Gate Skill

Creazione della terza skill strategica per verificare report finali Codex prima di decisioni GO/NO-GO.

- aggiunta skill `as-common-codex-report-intake-decision-gate`;
- creati file `references/` per intake report, diff review, decision matrix, evidence check, prompt correttivi e readiness commit/push;
- creati file `examples/` con prompt dimostrativi, sample intake e prompt correttivo NO-GO;
- aggiornata roadmap con 070 completato e prossimi step 080/090;
- rigenerati `SKILLS_INDEX.md` e `SKILL_SCORE.md`.

## 060) Verification Gate Test Eval Pack Skill

Creazione della seconda skill strategica per progettare e applicare verification gate.

- aggiunta skill `as-common-verification-gate-test-eval-pack`;
- creati file `references/` per gate, test matrix, eval, golden sample, stop policy e report finale;
- creati file `examples/` con prompt dimostrativi e sample verification gate;
- aggiornata roadmap con 060 completato e prossimo step 070;
- rigenerati `SKILLS_INDEX.md` e `SKILL_SCORE.md`.

## 050) Agent Context Governor Skill

Creazione della prima skill strategica nuova per governare il contesto operativo degli step Codex.

- aggiunta skill `as-common-agent-context-governor`;
- creati file `references/` per governance contesto, source map, AGENTS.md, conflitti e handoff;
- creati file `examples/` con prompt dimostrativi e sample review;
- aggiornata roadmap con 050 completato e prossimi step 060/070;
- rigenerati `SKILLS_INDEX.md` e `SKILL_SCORE.md`.

## 040) Skill Quality Cleanup

Pulizia e uniformazione dopo la fondazione del catalogo skill.

- archiviati i backup `.bak.md` tracciati in `_archive/backup-skills/`;
- aggiunta documentazione `_archive/README.md`;
- aggiornata `.gitignore` per evitare futuri backup temporanei;
- aggiunta review warning in `docs/skill-warning-review.md`;
- migliorate `as-common-codex-command-pack` e `as-common-vba-excel-access-alberto` con `references/` ed `examples/`;
- sostituiti esempi sensibili con placeholder o termini equivalenti;
- aggiornato il validator per ignorare esplicitamente `_archive/`;
- rigenerati `SKILLS_INDEX.md` e `SKILL_SCORE.md`.

## 030) Skill Catalog & Validator Foundation

Creazione della base di catalogazione e validazione delle skill Codex.

- aggiunto validator principale `validators/check_agent_skills.py`;
- aggiunti test standard library `validators/test_check_agent_skills.py`;
- aggiunta generazione automatica di `SKILLS_INDEX.md`;
- aggiunta generazione automatica di `SKILL_SCORE.md`;
- aggiornata documentazione qualità e authoring skill;
- mantenuta la rilevazione dei file backup senza cancellarli.

## 010

Creazione Governance Pack iniziale.

- README
- AGENTS
- docs
- templates
- validators
- gitignore
- gitattributes
