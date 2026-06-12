# Input Modes

Adatta la review all'evidenza disponibile. Non inventare dettagli visuali quando
manca una fonte.

## Solo Screenshot

- Descrivi solo cio' che e' visibile.
- Valuta gerarchia, contrasto apparente, spacing, microcopy e composizione.
- Segnala limiti: niente hover, focus, loading, responsive o stato dinamico.
- Chiedi altri screenshot solo se un giudizio P0/P1 dipende da stato mancante.

## Piu' Screenshot

- Confronta desktop/mobile, prima/dopo o stati diversi.
- Cerca coerenza tra componenti e variazioni di layout.
- Valuta se gli stati vuoti, errore e loading sono trattati con la stessa cura.

## HTML/CSS/Templates

- Leggi struttura, classi, token, componenti e stati disponibili.
- Evidenzia rischi statici: overflow, gerarchia, contrasto dichiarato, focus,
  testi generici.
- Non promettere accuratezza visuale senza render o screenshot.

## Repo Web Locale

- Prima chiarisci se il lavoro e' review-only o fix autorizzato.
- Leggi README, route, componenti principali, CSS/tokens e documenti design.
- Usa browser o screenshot solo se disponibili, necessari e autorizzati dal
  contesto.
- Non avviare dev server o scrivere codice automaticamente.

## Descrizione Testuale

- Trasforma la descrizione in ipotesi esplicite.
- Dai raccomandazioni di struttura e checklist, non giudizi visuali definitivi.
- Indica quali screenshot o file servirebbero per confermare P0/P1.

## PRODUCT.md / DESIGN.md

- Trattali come contesto prodotto/design.
- Non confonderli con `AGENTS.md` o project instructions.
- Verifica coerenza tra utenti, tono, componenti e UI osservata.

## Prototipo Non Implementato

- Lavora su flusso, gerarchia, contenuti minimi e stati necessari.
- Produci una checklist per il futuro implementation step.
- Non generare codice salvo richiesta separata.

## Confronto Prima/Dopo

- Valuta se il dopo migliora task, chiarezza e accessibilita', non solo estetica.
- Cerca regressioni in densita', responsive, contrasto e microcopy.
- Mantieni issue vecchie e nuove separate.

## Mobile/Desktop

- Verifica priorita' e azioni nel primo viewport.
- Cerca overflow, testo troppo lungo, tap target deboli e navigazione nascosta.
- Per dashboard dense, distinguere mobile utile da mobile solo consultivo.

## Limiti Da Dichiarare

- Se non c'e' screenshot, non inventare dettagli visivi.
- Se non c'e' browser, fare review statica.
- Se manca contesto utente, esplicitare assunzioni.
- Se mancano stati vuoti/errore/loading, segnalarli come gap di evidenza.
