# SKILLS_INDEX

Catalogo automatico delle skill presenti nella repository.

Aggiornato: 2026-06-13 11:46:16

## Riepilogo

| Voce | Valore |
|---|---:|
| Skill totali | 22 |
| Skill con errors | 0 |
| Skill con warnings | 0 |

## Catalogo

| Skill | Name dichiarato | Description | References | Examples | Errors | Warnings |
|---|---|---|---:|---:|---:|---:|
| as-common-agent-context-governor | as-common-agent-context-governor | Use this skill when reviewing, creating, or reconciling project instructions, AGENTS.md files, Codex prompts, skill usage, repository rules, handoff summaries, or context conflicts before starting or closing an agentic coding step. Do not use it for a purely technical repository readiness review. | si | si | 0 | 0 |
| as-common-business-email-draft | as-common-business-email-draft | Usa questa skill quando Alberto vuole correggere, riscrivere o preparare email commerciali, tecniche, HR o delicate in italiano o inglese per clienti, fornitori, dipendenti e collaboratori, con tono logico, empatico, fermo e operativo. Non usarla per runbook, prompt Codex, UI review, legal claim o report tecnici lunghi. | si | no | 0 | 0 |
| as-common-codex-command-pack | as-common-codex-command-pack | Use this skill when Alberto asks to prepare one executable Codex prompt or command packet for implementation, debugging, review, or repository work. Use it for temporary handoff prompts to Codex. Do not use it for numbered step governance, durable docs, or restart summaries. | si | si | 0 | 0 |
| as-common-codex-prompt-length-advisor | as-common-codex-prompt-length-advisor | Usa questa skill quando Alberto deve valutare un prompt Codex troppo lungo, mega-prompt o prompt monolitico con rischio troncamento, END_OF_PROMPT, REGOLE FINALI, CONTROLLO INTEGRITÀ PROMPT, prompt packet, prompt da 20k/30k/45k/70k/100k caratteri, context used in Codex o crescita contesto durante il run. Non usarla per scrivere prompt generici, scegliere il modello o gestire uno step numerato end-to-end. | si | no | 0 | 0 |
| as-common-codex-report-intake-decision-gate | as-common-codex-report-intake-decision-gate | Use this skill when Alberto provides a completed Codex final report and needs it compared with the original prompt, Git status, diffs, tests, warnings, and evidence to decide GO, GO_WITH_WARNINGS, NO_GO, clarification needs, or corrective follow-up. Do not use it to design test gates before work starts. | si | si | 0 | 0 |
| as-common-codex-step-manager | as-common-codex-step-manager | Use this skill when Alberto is managing a numbered Codex/ASF step, including scope, phases, acceptance criteria, report format, completion status, and next recommended step. Do not use it only to draft a one-shot Codex prompt, write persistent runbook documentation, or summarize a chat restart. | no | no | 0 | 0 |
| as-common-deep-research-industriale | as-common-deep-research-industriale | Usa questa skill quando Alberto deve impostare o scrivere una ricerca tecnica industriale con fonti su materiali, prodotti chimici/minerali, processi, norme, brevetti tecnici, fornitori, benchmark, mercato o stime tecnico-economiche. Non usarla per email, debug codice, prompt Codex, UI review o curiosita generiche senza ricerca. | si | no | 0 | 0 |
| as-common-docs-runbook-builder | as-common-docs-runbook-builder | Use this skill when Alberto asks to create or update persistent repository documentation such as runbooks, repeatable procedures, maintenance checklists, deployment notes, troubleshooting, onboarding, README sections, or user/technical guides. Do not use it for Project Instructions or AGENTS policy, one-shot Codex prompts, numbered step lifecycle, email, UI review, or chat restart summaries. | si | no | 0 | 0 |
| as-common-model-effort-advisor | as-common-model-effort-advisor | Usa questa skill quando Alberto chiede quale livello ChatGPT usare o serve un model effort check per compiti Codex, ASF, coding, ricerca, review, decision gate, merge o skill trasversali. Non usarla per cambiare modello automaticamente o per interventi ordinari senza mismatch evidente. | no | no | 0 | 0 |
| as-common-opencv-image-pipeline | as-common-opencv-image-pipeline | Usa questa skill per pipeline immagini di Alberto con OpenCV Python/C++: QR code, omografia, binarizzazione, istogrammi, segmentazione, soglie, debug visuale, output intermedi e confronto immagini. DiamSign e' un esempio, non un vincolo. Non usarla per generazione immagine creativa, UI review, FastAPI, email, prompt Codex o analisi brevettuale. | si | no | 0 | 0 |
| as-common-powershell-git-safe-flow | as-common-powershell-git-safe-flow | Usa questa skill quando devi generare o verificare comandi PowerShell/Git sicuri, linee guida Git o blocchi brevi per Alberto su Windows. Non usarla per costruire command pack PowerShell completi con Bridge, report e artifact riutilizzabili. | no | no | 0 | 0 |
| as-common-project-instructions-builder | as-common-project-instructions-builder | Use this skill when Alberto needs to create, audit, or refresh durable project instructions for ChatGPT Projects, Codex AGENTS.md, repository-wide agent rules, Copilot instructions, instruction templates, or quality gates. Do not use it for one-shot Codex prompts, numbered step lifecycle management, generic runbooks, or chat restart summaries. | si | si | 0 | 0 |
| as-common-project-riepilogo-operativo | as-common-project-riepilogo-operativo | Usa questa skill quando Alberto chiede un riepilogo operativo di continuità per chiudere una chat lunga e ripartire in una nuova chat dello stesso progetto. Non usarla per README, runbook o documentazione persistente di repository. | no | no | 0 | 0 |
| as-common-pwsh-command-pack | as-common-pwsh-command-pack | Generate safe logged PowerShell command packs for Alberto with short safe bootstraps, generated .ps1 scripts, numbered outputs, optional LAST mirrors on explicit request, compact Markdown/DOCX reports, explicit file handoff, robust Git parsing, PR-first publication, and Git/Codex/ASF guardrails. | si | si | 0 | 0 |
| as-common-python-fastapi-debug | as-common-python-fastapi-debug | Usa questa skill per debug locale Python/FastAPI/pytest di Alberto: endpoint, status code, trace, fixture, SQLAlchemy, Uvicorn, Jinja, template rendering, venv e fix minimi verificati. Non usarla per UI visual review, project instructions, prompt Codex, OpenCV, VBA o Git publish flow. | si | no | 0 | 0 |
| as-common-repo-readiness-review | as-common-repo-readiness-review | Usa questa skill per fare una revisione tecnica iniziale read-only di una repository prima di uno step Codex: branch, stato Git, struttura, test, documenti, rischi e readiness. Non usarla per riconciliare istruzioni, AGENTS.md o conflitti di contesto agente. | no | no | 0 | 0 |
| as-common-skill-authoring | as-common-skill-authoring | Usa questa skill quando Alberto vuole creare, rinominare, migliorare o organizzare skill Codex secondo il naming as-common-* e as-<project-key>-*. | no | no | 0 | 0 |
| as-common-technical-patent-draft | as-common-technical-patent-draft | Usa questa skill per preparare disclosure inventive, bozze tecniche e documenti per consulente brevettuale su algoritmi, materiali, processi e sistemi R&D di Alberto. Non usarla per pareri legali definitivi, deposito brevetto, FTO, validita garantita, contraffazione, traduzioni pure o email. | si | no | 0 | 0 |
| as-common-vba-excel-access-alberto | as-common-vba-excel-access-alberto | Usa questa skill per codice VBA/Excel/Access di Alberto, inclusi UserForm generati via codice, eSolver read-only, ADODB/ODBC, performance, debug flag e fogli Excel. | si | si | 0 | 0 |
| as-common-verification-gate-test-eval-pack | as-common-verification-gate-test-eval-pack | Use this skill when designing or enforcing tests, smoke checks, health checks, evals, golden samples, verification gates, evidence requirements, or stop policies before or during a Codex-driven step. Do not use it to intake a completed Codex final report; use the report-intake decision gate instead. | si | si | 0 | 0 |
| as-common-web-ui-design-review | as-common-web-ui-design-review | Skill comune per review di UI web, UX visuale e design consistency su progetti web/dashboard/landing, con output prioritizzato e azioni pratiche, senza dipendere da Impeccable o da tool esterni. Usala per screenshot, pagine web, dashboard locali, web app e frontend review; non usarla per project instructions, repo readiness generica, prompt Codex, backend-only, generazione immagini o installazione di tool esterni. | si | no | 0 | 0 |
| as-common-web-ui-linguistic-visual-qa | as-common-web-ui-linguistic-visual-qa | Use this skill for multilingual web UI linguistic and visual QA on local web apps or dashboards: i18n checks, baseline-language residue, raw enum/status labels, DOM visible-text extraction, browser or headless fallback walkthroughs, screenshot matrix, mobile/desktop overflow, and merge-readiness review. Do not use it for generic translation, email, Excel/VBA, OpenCV, image generation, scheduler changes, or merge without review. | no | si | 0 | 0 |

## File backup rilevati

- Nessuno.

## Note

Il file è generato automaticamente da `validators/check_agent_skills.py`.
