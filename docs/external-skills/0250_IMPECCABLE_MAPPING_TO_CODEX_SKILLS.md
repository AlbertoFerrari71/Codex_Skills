# 0250 Impeccable Mapping To Codex Skills

Data: 2026-06-12

Step: 0250) Codex Skills - Impeccable Design Skill Evaluation and Safe Adoption Plan

## Mappa comandi Impeccable verso workflow Alberto

| Impeccable | Workflow Alberto possibile | Skill esistente coinvolta | Nota |
|---|---|---|---|
| `init` | Raccogliere contesto UI prodotto/design | `as-common-project-instructions-builder` solo per separazione istruzioni | Non sostituire AGENTS/Project Instructions; usare come design context. |
| `document` | Generare/aggiornare design context da UI esistente | futura `as-common-web-ui-design-review` | Da proporre, non fare automaticamente. |
| `shape` | Pianificare una nuova UI prima del codice | `as-common-codex-step-manager` | Utile in step implementativi futuri. |
| `craft` | Disegnare e costruire nuova feature UI | step manager + futura skill UI | Troppo invasivo per default; richiede gate e approvazioni. |
| `critique` | Review visuale/UX di una UI gia' costruita | futura `as-common-web-ui-design-review` | Candidato principale per wrapper. |
| `audit` | Audit UI tecnico: a11y/perf/responsive/theming | `as-common-verification-gate-test-eval-pack` + futura skill UI | Complementare ai test, non sostitutivo. |
| `polish` | Fix finale di UI prima di consegna | futura skill UI solo se fix autorizzato | Non eseguire in step review-only. |
| `harden` | Stati errore, i18n, overflow, edge cases UI | futura skill UI + verification gate | Utile per product UI/admin. |
| `onboard` | Empty states, first-run, activation | futura skill UI | Specifico per app/prodotti. |
| `adapt` | Responsive e device contexts | futura skill UI | Utile per dashboard/landing. |
| `clarify` | Microcopy/label/error message | futura skill UI o email/docs skill se non UI | Tenere limitato a copy in interfaccia. |
| `layout` | Spacing, rhythm, hierarchy | futura skill UI | Buon modulo review. |
| `typeset` | Typography | futura skill UI | Da usare come check, non dogma estetico. |
| `colorize` | Colore strategico | futura skill UI | Richiede identita' e accessibilita'. |
| `bolder`/`quieter` | Regolare intensita' visuale | futura skill UI | Solo dopo aver definito brand/product register. |
| `distill` | Ridurre complessita' UI | futura skill UI | Utile per dashboard dense. |
| `animate` | Motion design | futura skill UI | Richiede reduced motion e performance. |
| `delight` | Micro-interazioni/personality | futura skill UI | Basso priority rispetto a P0/P1. |
| `overdrive` | Effetti visuali avanzati | Nessuna skill attuale | Alto rischio, non default per Alberto. |
| `extract` | Estrarre token/componenti | futura skill UI o step implementativo | Richiede repo frontend maturo. |
| `live` | Browser visual iteration | futura skill UI solo come opzione esplicita | Alto rischio: scrive source via HMR workflow. |
| `pin/unpin` | Shortcut comandi | Nessun mapping consigliato | Evitare nel workflow Alberto salvo uso diretto Impeccable. |
| `detect` CLI | Detector anti-pattern read-only | verification gate opzionale | Miglior componente esterno da pilotare. |

## Sovrapposizioni con skill esistenti

| Skill | Cosa copre gia' | Gap rispetto a Impeccable |
|---|---|---|
| `as-common-project-instructions-builder` | Istruzioni durevoli ChatGPT/Codex/AGENTS/Copilot | Non fa UI critique, screenshot review o anti-pattern visuali. |
| `as-common-skill-authoring` | Creazione/naming/struttura skill | Non valuta UI, ma governa futura skill wrapper. |
| `as-common-repo-readiness-review` | Readiness tecnica repo prima dello step | Non giudica visual hierarchy, UX o design system. |
| `as-common-verification-gate-test-eval-pack` | Test, smoke, eval, stop policy | Non ha euristiche UI/anti-slop specifiche. |
| `as-common-codex-command-pack` | Prompt temporanei/handoff | Non e' una skill di review UI. |
| `as-common-codex-step-manager` | Step, report, vincoli Git | Governa esecuzione, non design review. |
| `as-common-agent-context-governor` | Conflitti istruzioni/AGENTS/skill | Utile se PRODUCT/DESIGN confliggono con istruzioni progetto. |
| `as-common-codex-prompt-length-advisor` | Lunghezza/integrita' prompt | Nessuna copertura UI. |

## Gap non coperti dal catalogo attuale

| Gap | Impatto | Copertura futura |
|---|---|---|
| Review UI visuale sistematica | Alto nei progetti web/dashboard | `as-common-web-ui-design-review`. |
| Anti-AI-slop e pattern estetici ricorrenti | Medio/alto per landing e UI generate | Checklist + detector opzionale. |
| Screenshot/browser review come evidenza | Alto per frontend | Browser opzionale con fallback. |
| Distinzione brand surface vs product UI | Alto per decisioni di layout/copy | Parte centrale della futura skill. |
| Microcopy UI | Medio | Sezione dedicata nella futura skill. |
| Visual QA responsive/accessibility | Alto | P0-P3 + test manuali/browser. |
| Uso sicuro di `PRODUCT.md`/`DESIGN.md` | Medio | Regola di separazione da project instructions. |

## Cosa copiare come idea

Non copiare sorgente, ma si possono riusare come concetti:

- separare strategia prodotto (`PRODUCT.md`) da sistema visuale (`DESIGN.md`);
- distinguere brand surface da product UI;
- usare critique e audit come due passaggi distinti;
- ordinare problemi per severita' P0-P3;
- usare personas e job-to-be-done per valutare UX;
- verificare anti-pattern ricorrenti in modo deterministico quando possibile;
- trattare screenshot/browser come evidenza, non come decorazione;
- dichiarare quando browser/live/detector non sono disponibili;
- non trasformare heuristic score in voto assoluto.

## Cosa evitare

| Cosa evitare | Motivo |
|---|---|
| Copiare la skill `impeccable` nel catalogo | Naming non conforme e scope troppo grande. |
| Portare 23 comandi in una nostra skill | Troppo ampia, alta collisione trigger. |
| Install/update automatici | Modificano provider folders e dipendono da rete/npm. |
| Live Mode come default | Scrive source e richiede browser/dev server. |
| Detector come unica verita' | False positive possibili, contesto brand conta. |
| Confondere `PRODUCT.md` con AGENTS.md | Governance e design context sono diversi. |
| Fix UI in uno step review-only | Viola separazione review/implementazione. |
| Bypassare test per estetica | La UI deve restare funzionante. |

## Trigger proposto per futura skill

Nome: `as-common-web-ui-design-review`

Description proposta:

```text
Usa questa skill quando Alberto chiede una review UI/UX di una pagina web,
dashboard, componente frontend, screenshot o app locale: visual QA,
anti-AI-slop, accessibilita', responsive, microcopy, design consistency e
report P0-P3. Non usarla per backend-only, project instructions, AGENTS.md,
repo readiness generica, prompt pack o gate/test non UI.
```

Anti-trigger:

- creare o aggiornare AGENTS.md;
- scrivere project instructions;
- fare repo readiness generica;
- generare prompt Codex;
- creare una skill;
- fare solo test backend;
- audit sicurezza/supply chain;
- editare UI senza autorizzazione.

## Esempio pratico in un progetto web ASF

Scenario: ASF Blueprint Studio ha una pagina dashboard con stati workflow e pannelli di comando.

Uso futuro:

1. Preflight branch/status.
2. Leggere README, route dashboard, CSS/tokens, componenti principali.
3. Se dev server disponibile, screenshot desktop/mobile.
4. Review P0-P3:
   - P0: azioni distruttive poco distinguibili;
   - P1: contrasto insufficiente negli stati warning;
   - P1: overflow su viewport mobile;
   - P2: gerarchia visiva troppo simile tra step attivo e completato;
   - P3: microcopy CTA non specifica.
5. Prossimo step: prompt implementativo separato, non fix automatico nella review.

## Esempio pratico in AI Release Radar

Scenario: dashboard locale o pagina report per segnali release.

Uso futuro:

1. Trattare la UI come product surface, non landing.
2. Valutare densita' informativa, filtri, tabelle, empty states, timestamp e priorita'.
3. Separare istruzioni agente da contesto UI: eventuale `PRODUCT.md` descrive utenti e workflow, non regole Codex.
4. Evitare palette/hero marketing se l'utente deve scansionare dati.
5. Output: P0/P1 su leggibilita', focus, ordinamento, stato "stale", responsive.

## Esempio pratico in Mansionario_Vivo

Scenario: admin tool con tabelle, form e calendario attivita'.

Uso futuro:

1. Product UI, target: operatori che devono inserire e controllare dati velocemente.
2. Review su:
   - form labels e error states;
   - accessibilita' tastiera;
   - mobile/tablet;
   - density;
   - action hierarchy;
   - microcopy italiana.
3. Evitare "delight" o effetti visuali se rallentano operativita'.
4. Prossimo step separato per fix mirati, con test e diff review.

## Esempio pratico in ASF Blueprint Studio

Scenario: interfaccia per progettare blueprint ASF e visualizzare step.

Uso futuro:

1. Identificare utenti: Alberto/agent operator, contesto ad alta attenzione.
2. Verificare che la UI sia leggibile in sessioni lunghe.
3. Priorita':
   - status e next action chiarissimi;
   - errori e stop policy visibili;
   - nessun card nesting inutile;
   - density professionale, non landing page.
4. Browser/live review solo su branch e con server noto.

## Separare project instructions da UI design review

| Oggetto | Deve vivere in | Non deve vivere in |
|---|---|---|
| Regole operative Codex | `AGENTS.md`, project instructions, docs governance | `PRODUCT.md`/`DESIGN.md` |
| Utenti, scopo prodotto, voce | `PRODUCT.md` o documento design context | AGENTS.md |
| Colori, typography, componenti | `DESIGN.md` o design docs | Project instructions compatte |
| Gate Git/test/report | AGENTS.md, release workflow, step prompt | DESIGN.md |
| Review UI P0-P3 | report della futura skill | Cataloghi skill generati |
| Detector findings | report o artifact del progetto target | Istruzioni permanenti globali |

Regola operativa: se un contenuto dice "come deve comportarsi l'agente", va in istruzioni progetto; se dice "per chi e' la UI e come deve apparire/funzionare", va nel design context.

## Raccomandazione finale

Creare uno step 0260 per una skill wrapper nostra. Impeccable resta benchmark e possibile tool esterno nei singoli progetti web, non dipendenza del catalogo `Codex_Skills`.
