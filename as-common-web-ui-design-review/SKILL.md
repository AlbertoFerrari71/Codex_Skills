---
name: as-common-web-ui-design-review
description: Skill comune per review di UI web, UX visuale e design consistency su progetti web/dashboard/landing, con output prioritizzato e azioni pratiche, senza dipendere da Impeccable o da tool esterni. Usala per screenshot, pagine web, dashboard locali, web app e frontend review; non usarla per project instructions, repo readiness generica, prompt Codex, backend-only, generazione immagini o installazione di tool esterni.
---

# Scopo

Aiutare Alberto e Codex a fare review visuali e UX di interfacce web, dashboard,
landing page, schermate applicative e frontend locali.

La skill produce raccomandazioni pratiche, prioritarie e verificabili su:

- gerarchia visiva;
- layout, griglia e spaziature;
- tipografia;
- colore, contrasto e accessibility di base;
- responsive desktop/mobile;
- microcopy;
- stati vuoti, errore e loading;
- usabilita' dashboard;
- coerenza con `PRODUCT.md`, `DESIGN.md` o documenti equivalenti;
- anti-AI-slop;
- readiness visuale prima di release.

La skill consiglia e struttura la review. Non riscrive automaticamente il
frontend.

# Quando usarla

Usala quando Alberto chiede, con contesto UI sufficiente, di:

- fare review della UI di una dashboard;
- valutare screenshot di una web app;
- controllare se un'interfaccia sembra fatta dall'AI;
- fare audit visuale UX di una pagina;
- migliorare layout, gerarchia e microcopy di una schermata;
- fare review frontend prima della release;
- controllare accessibilita' base, responsive e contrasto;
- analizzare una landing page;
- fare visual QA della web UI;
- controllare la dashboard di AI Release Radar;
- controllare la UI di Mansionario_Vivo;
- controllare ASF Blueprint Studio lato UX;
- valutare una UI locale o futura UI ASF da screenshot, HTML/CSS o template.

# Quando non usarla

Non usarla per:

- richieste generiche di Project Instructions, AGENTS.md, Copilot instructions o
  quality gate agentici;
- creare prompt Codex lunghi o command pack;
- gestire commit, push, PR, merge o lifecycle di step numerati;
- fare solo repo readiness tecnica;
- scrivere business email;
- analisi backend/API senza superficie UI;
- test Python, FastAPI o pipeline tecniche non UI;
- disegno grafico professionale completo o brand identity critica;
- generare o modificare immagini;
- installare Impeccable o altri tool esterni;
- audit security;
- audit accessibilita' certificato WCAG;
- performance profiling completo.

# Input accettati

Lavora con uno o piu' di questi input:

- screenshot singolo o multiplo;
- descrizione della schermata;
- link locale o percorso progetto, se fornito;
- HTML, CSS, template o componenti frontend;
- `PRODUCT.md`, `DESIGN.md`, README o documenti equivalenti;
- obiettivo utente e job-to-be-done;
- vincoli brand o tono prodotto;
- target device e viewport;
- livello di severita' desiderato;
- confronto prima/dopo.

Se manca lo screenshot, non inventare dettagli visuali. Se manca browser o dev
server, fai review statica su file e descrizione. Se manca contesto utente,
dichiara assunzioni e limita la severita'.

# Procedura

1. Capire obiettivo utente, contesto prodotto, target device e superficie UI.
2. Separare problemi bloccanti da miglioramenti estetici.
3. Valutare gerarchia, layout, spaziatura, tipografia, colore, contrasto,
   responsive, microcopy, stati vuoti, stati errore e stati loading.
4. Individuare pattern anti-AI-slop e incoerenze di componenti.
5. Proporre interventi minimi, pratici e verificabili.
6. Se serve codice, suggerire uno step separato e controllato con gate di
   sicurezza, test e diff review.

# Formato output

Per review non banali restituisci:

1. Sintesi esecutiva.
2. Tabella issue P0/P1/P2/P3 con area, evidenza, impatto, suggerimento, effort,
   rischio regressione e verifica consigliata.
3. Quick wins.
4. Rischi UX residui.
5. Raccomandazioni pratiche e verificabili.
6. Eventuale prompt Codex per modifiche UI solo se Alberto lo chiede.
7. Gate di sicurezza prima di scrivere codice.

Priorita':

- P0: blocca uso, comprensione o accessibilita' essenziale.
- P1: problema serio che riduce conversione, efficienza o fiducia.
- P2: miglioramento importante ma non bloccante.
- P3: polish estetico, microcopy o rifinitura.

# Regole importanti

- Distingui fatti verificati, ipotesi, euristiche e raccomandazioni.
- Non promettere review visuale accurata senza screenshot, browser o evidenza
  visiva sufficiente.
- Non installare Impeccable.
- Non trattare Impeccable come dipendenza obbligatoria.
- Non avviare browser, live mode o scrittura live automatica.
- Non scrivere codice senza autorizzazione esplicita.
- Non sostituire designer o brand specialist per identita' visiva critica.
- Non fare audit accessibilita' certificato WCAG.
- Non fare security audit.
- Non fare performance profiling completo.
- Non toccare Git.
- Mantieni la review stretta su UI web, dashboard, landing e frontend.

# Riferimenti

- `references/review-checklist.md`
- `references/priority-rubric.md`
- `references/input-modes.md`
- `references/anti-ai-slop-patterns.md`
