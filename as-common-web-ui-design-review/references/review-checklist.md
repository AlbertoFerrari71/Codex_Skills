# Review Checklist

Usa questa checklist come guida pratica. Non deve produrre un report lungo per
forza: seleziona le voci rilevanti per la superficie UI osservata.

## Contesto

- Scopo pagina: la schermata comunica subito cosa si puo' fare e perche'.
- Obiettivo utente: il task primario e' evidente.
- Primo colpo d'occhio: stato, priorita' e prossima azione sono leggibili in
  pochi secondi.
- Coerenza prodotto: la UI rispetta `PRODUCT.md`, `DESIGN.md`, README o
  documenti equivalenti, se presenti.

## Struttura Visuale

- Gerarchia visiva: titoli, metriche, azioni e contenuti hanno peso coerente.
- Densita' informativa: la pagina e' scansionabile senza nascondere dati utili.
- Layout e griglia: colonne, allineamenti e gruppi sono regolari.
- Spaziature: padding, gap e margini sono intenzionali e non casuali.
- Tipografia: dimensioni, peso e lunghezza righe aiutano lettura e confronto.
- Colore/contrasto: stati, testo e CTA sono leggibili e non dipendono solo dal
  colore.

## Interazione

- Call to action: azioni primarie e secondarie sono distinguibili.
- Navigazione: l'utente capisce dove si trova e come tornare o proseguire.
- Stati vuoti: spiegano cosa manca e offrono un'azione utile.
- Stati errore: dicono cosa e' successo, cosa rischia l'utente e come risolvere.
- Stati loading: preservano layout e aspettativa, senza blocchi silenziosi.
- Feedback: click, salvataggi, filtri e azioni distruttive hanno conferma o
  stato visibile.

## Qualita' UI

- Responsive: desktop, tablet e mobile non rompono gerarchia, overflow o azioni.
- Accessibility base: focus, contrasto, label, ordine logico e testo alternativo
  sono ragionevoli per una review non certificata.
- Microcopy: label, CTA, empty state ed errori usano parole specifiche e utili.
- Consistenza componenti: componenti simili si comportano e appaiono in modo
  simile.
- Anti-AI-slop: pattern decorativi, gradienti, card, badge e icone hanno una
  funzione chiara.

## Dashboard

- Priorita': metriche, allarmi e next action sono ordinati per importanza.
- Tabelle e liste: colonne, filtri, ordinamento e stati sono scansionabili.
- Timestamp e freshness: dati vecchi, mancanti o incerti sono evidenti.
- Densita': la UI supporta uso ripetuto senza stile marketing eccessivo.

## Landing

- Offerta: valore, target e azione primaria sono chiari nel primo viewport.
- Prova: immagini, esempi o stati reali mostrano prodotto o risultato.
- CTA: il testo dice cosa succede dopo.
- Sezioni: ogni blocco aggiunge informazione, non solo decorazione.

## Local Web App

- Ambiente: URL locale, viewport e stato dati sono dichiarati.
- Workflow: la schermata supporta il task reale, non solo una demo vuota.
- Sicurezza operativa: azioni irreversibili, import/export e path locali sono
  chiari.

## Release Readiness

- P0/P1 risolti o accettati consapevolmente.
- Stati vuoti, errore e loading verificati.
- Mobile/desktop verificati almeno sui viewport target.
- Microcopy critico e messaggi errore riletti.
- Nessun pattern anti-AI-slop dominante rimasto senza motivo.
