# Project Instructions Quality Gate

Valida ogni pacchetto di istruzioni con PASS, WARNING o FAIL.

| # | Check | Esito | Nota |
|---:|---|---|---|
| 1 | Identita progetto presente |  |  |
| 2 | Obiettivo operativo presente |  |  |
| 3 | Ruolo di ChatGPT chiaro |  |  |
| 4 | Ruolo di Codex chiaro, se pertinente |  |  |
| 5 | Regole Git presenti, se pertinenti |  |  |
| 6 | Regole PowerShell presenti, se pertinenti |  |  |
| 7 | Regole Bridge presenti, se pertinenti |  |  |
| 8 | Vincoli di sicurezza presenti |  |  |
| 9 | Regole output/report presenti |  |  |
| 10 | Regole globali e progetto-specifiche separate |  |  |
| 11 | Nessuna contraddizione evidente |  |  |
| 12 | Nessuna automazione pericolosa implicita |  |  |
| 13 | Lunghezza controllata |  |  |
| 14 | Stile coerente con Alberto |  |  |
| 15 | Criteri di verifica presenti |  |  |
| 16 | Prossimo step o regola di ripartenza presente |  |  |
| 17 | Esempi o placeholder utili presenti |  |  |

## Stop policy

- FAIL su identita progetto, obiettivo, ruoli, sicurezza o automazioni pericolose blocca la pubblicazione delle istruzioni.
- WARNING su lunghezza, esempi o Copilot puo' essere accettato se motivato.
- Un output compatto troppo lungo va ridotto prima di essere incollato nelle Project Instructions ChatGPT.

## Evidenza minima

Ogni validazione deve indicare:

- fonti lette;
- output prodotti;
- punti WARNING o FAIL;
- decisioni lasciate ad Alberto;
- prossimo step consigliato.
