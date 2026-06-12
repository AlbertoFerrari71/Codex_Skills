# 0270) Web UI Design Review Smoke Trial

Data: 2026-06-12

Skill verificata: `as-common-web-ui-design-review`

## Project Selection

| Campo | Valore |
|---|---|
| Progetto scelto | `AI_Release_Radar` |
| Path | `C:\Users\alberto.ferrari\source\repos\AI_Release_Radar` |
| Motivo scelta | primo progetto accessibile nell'ordine richiesto con dashboard web reale, template Jinja2, CSS e documenti UI gia presenti |
| Modalita input | static source + docs |
| Screenshot | evidenza visuale non disponibile |
| Browser/server | non avviato |
| Modifiche al repo target | nessuna |

Target verificati in sola lettura:

- `AI_Release_Radar`: presente, contiene `radar_web/templates/*.html`,
  `radar_web/static/style.css` e documenti UI.
- `ASF_Blueprint_Studio`: presente, contiene molti template web.
- `Mansionario_Vivo`: presente, contiene template e CSS.

La scelta resta `AI_Release_Radar` per determinismo: e' il primo target valido.

## Materiale Analizzato

File sorgente:

- `radar_web/templates/index.html`
- `radar_web/templates/actions.html`
- `radar_web/templates/run_detail.html`
- `radar_web/static/style.css`

Documenti:

- `docs/architecture/0760_WEB_DASHBOARD_ARCHITECTURE.md`
- `docs/runbooks/0930_OPERATOR_SCREENSHOT_PACK.md`
- `docs/reviews/1310_ACTION_CENTER_MULTILINGUAL_UX_REVIEW.md`
- `docs/reviews/1320_UI_READABILITY_LAYOUT_POLISH.md`

## Assumptions

- La dashboard e' uno strumento locale operativo per leggere run Bridge,
  scheduler, gate, HAG, action inbox e prompt suggestions.
- Il task primario e' aiutare Alberto a capire stato, rischi e prossime azioni
  senza confondere suggerimenti con auto-azioni.
- La review e' statica: valuta struttura, gerarchia dichiarata, copy, stati e
  rischi di interazione deducibili dal source.

## Limits

- evidenza visuale non disponibile.
- Nessun browser e nessun server locale avviato.
- Nessuna verifica reale di contrasto, viewport, focus, hover, loading o layout
  renderizzato.
- Le osservazioni su responsive e peso visivo sono ipotesi UX derivate da
  HTML/CSS, non giudizi visuali definitivi.

## Executive Summary

La skill produce un output utile per questo caso: forza la separazione tra
fatti verificati, limiti e ipotesi; richiede priorita P0/P1/P2/P3; impedisce di
inventare dettagli visuali senza screenshot. Il risultato non e' generico:
emergono rischi specifici su warning, decisioni operatore, path tecnici, stati
vuoti e verifica mobile.

Non sono emersi P0 da source statico. I rischi principali sono P1/P2 e
richiedono screenshot o smoke browser in uno step separato prima di decidere
fix frontend.

## Issues

| Priorita | Area | Evidenza | Impatto | Suggerimento | Effort S/M/L | Rischio regressione | Verifica consigliata |
|---|---|---|---|---|---|---|---|
| P0 | Uso essenziale | Nessun blocco certo rilevato da `index.html`, `actions.html`, `run_detail.html` e `style.css`. | Non ci sono prove statiche di task primario impossibile. | Nessun fix P0 senza screenshot/browser. | S | Basso | Confermare con screenshot home, actions, run detail desktop/mobile. |
| P1 | Warning operativi | In `index.html` le sezioni `status.warnings` e `status.data_completeness_warnings` compaiono dopo metriche, pannelli e tabella run recenti. | Un warning runtime o dati incompleti puo essere visto tardi rispetto a metriche che sembrano rassicuranti. | Quando esistono warning, mostrare un sommario warning vicino al primo viewport, sopra o subito sotto `status-grid`. | S | Basso | Screenshot con warning simulato e controllo primo viewport. |
| P1 | Decisioni Action Center | In `actions.html` ogni card espone molti bottoni di decisione (`approve_prompt`, `defer`, `ignore`, `backlog`, `request_review`) piu `generate_prompt_pack`; la JS invia POST e ricarica dopo 450 ms. | In una dashboard supervisionata, azioni con conseguenze diverse possono essere percepite come equivalenti o cliccate due volte. | Raggruppare decisioni per rischio, rendere chiara l'azione raccomandata, disabilitare i bottoni durante il POST e mostrare conferma leggibile prima del reload. | M | Medio | Smoke con click controllato, verifica stato disabled/result panel e screenshot card. |
| P2 | Path tecnici | Header, detail header e metriche mostrano path lunghi con classi `path` e `path-value`; il CSS mitiga overflow con `overflow-wrap:anywhere`. | I path sono utili ma possono dominare la scansione, soprattutto su mobile o in lingue lunghe. | Tenere il path completo disponibile ma secondario: summary/collapse, label piu corta o copy affordance in step separato. | S | Basso | Screenshot desktop/mobile con path Bridge reale lungo. |
| P2 | Empty state | La tabella run recenti usa `NO_DATA` come empty state; alcune liste detail mostrano solo `NO_DATA`. | L'operatore vede che manca il dato, ma non sempre capisce la causa o la prossima azione. | Per gli empty state critici aggiungere una frase specifica: cosa manca, dove arriva il dato, quale controllo fare. | S | Basso | Smoke con repo Bridge vuoto o fixture senza run. |
| P2 | Loading/error actions | `index.html` gestisce `daily-sim` con disabled/running label; `actions.html` mostra JSON result ma non disabilita i bottoni durante le decisioni. | Esperienza incoerente fra due flussi operativi e rischio di doppio click su decisioni. | Allineare il pattern di loading/disabled tra trigger manuale e action decisions. | S | Medio | Test manuale o browser smoke con doppio click controllato. |
| P2 | Responsive reale | CSS ha breakpoints a 980 px e 620 px; `action-grid` usa `minmax(360px, 1fr)` e i bottoni supportano wrap. Documenti 1310/1320 dichiarano smoke HTML/API ma non PNG visuale. | Il source mostra mitigazioni, ma non prova che card dense, badge e bottoni restino scansionabili su mobile. | Eseguire screenshot pack dedicato seguendo `docs/runbooks/0930_OPERATOR_SCREENSHOT_PACK.md`. | S | Basso | Screenshot home/actions/detail a desktop e mobile. |
| P3 | Microcopy tecnico | Etichette e valori sono localizzati via `t()`, ma molti stati restano concettualmente tecnici: gate, scheduler readiness, source coverage, prompt suggestions. | Utile per Alberto, ma nuovi operatori potrebbero richiedere piu contesto. | Aggiungere tooltip o note brevi solo sui termini piu ambigui, evitando testo didascalico diffuso. | M | Basso | Review con un operatore non autore del sistema. |

## Quick Wins

- Portare un warning summary in alto quando `status.warnings` o
  `data_completeness_warnings` non sono vuoti.
- Disabilitare i bottoni Action Center durante `postJson` e mostrare stato
  "saving" coerente con il trigger `daily-sim`.
- Rendere i path lunghi meno dominanti nel primo viewport, mantenendo il valore
  completo disponibile.
- Arricchire gli empty state critici con prossima azione o fonte attesa.
- Usare lo screenshot pack esistente prima di ogni fix CSS.

## UX Risks

- La dashboard supporta un workflow supervisionato: confondere suggerimento,
  decisione, trigger manuale e stato di gate sarebbe piu grave di un difetto
  estetico.
- Senza screenshot non si puo confermare gerarchia, contrasto apparente o
  densita reale.
- Le lingue lunghe sono gia considerate nei documenti 1310/1320, ma restano un
  rischio da verificare con screenshot.

## Practical Recommendations

1. Trattare questo smoke trial come input per un futuro step UI, non come
   autorizzazione a modificare frontend.
2. Prima di scrivere codice, produrre screenshot home/actions/detail con dati
   realistici e almeno un warning.
3. Se lo step successivo riguarda fix UI, limitare il primo intervento a warning
   placement, button loading state e empty state.
4. Tenere separata la review design dalla QA linguistica: per residui lingua,
   enum raw o DOM visible text usare la skill `as-common-web-ui-linguistic-visual-qa`.

## Non-Actions

- Nessuna modifica a `AI_Release_Radar`.
- Nessun branch, test, build, browser o server nel repo target.
- Nessuna installazione Impeccable.
- Nessun fix CSS o template proposto come codice in questo step.

## Non-Overlap Check

La skill e' rimasta dentro UI design review:

- non ha fatto repo readiness;
- non ha gestito lifecycle Git;
- non ha creato command pack;
- non ha analizzato lunghezza prompt;
- non ha debuggato FastAPI/backend;
- non ha fatto OpenCV o image processing;
- non ha fatto QA linguistica completa.

## Skill Quality Judgment

| Criterio | Giudizio |
|---|---|
| Utile/non utile | utile |
| Trigger appropriati | appropriati per dashboard, screenshot, HTML/CSS e review frontend |
| Output concreto/generico | concreto, perche obbliga evidenza, impatto, suggerimento e verifica |
| Miglioramenti necessari | nessun micro-fix immediato; monitorare overlap con la skill linguistica/visual QA |

Conclusione smoke trial: PASS.
