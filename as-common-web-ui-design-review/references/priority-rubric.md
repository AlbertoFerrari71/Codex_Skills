# Priority Rubric

Classifica ogni issue in base a impatto sul task utente, rischio operativo e
facilita' di verifica.

## Priorita'

| Priorita' | Definizione | Esempi |
|---|---|---|
| P0 | Blocca uso, comprensione o accessibilita' essenziale. | CTA primaria invisibile, form non usabile da tastiera, testo critico illeggibile, mobile rotto su task principale. |
| P1 | Problema serio che riduce conversione, efficienza o fiducia. | Gerarchia confusa, contrasto insufficiente su warning, dashboard senza priorita', error state non azionabile. |
| P2 | Miglioramento importante ma non bloccante. | Spacing incoerente, microcopy generico, componenti simili ma non uguali, responsive migliorabile. |
| P3 | Polish estetico, microcopy o rifinitura. | Icona decorativa superflua, tono CTA migliorabile, piccola incoerenza di shadow o radius. |

## Campi Obbligatori Issue

Ogni issue deve includere:

- priorita';
- area;
- evidenza;
- impatto;
- suggerimento;
- effort stimato S/M/L;
- rischio regressione basso/medio/alto;
- verifica consigliata.

## Criteri Di Classificazione

- Usa P0 solo quando l'utente non puo' completare o capire il task primario, o
  quando l'accessibility base e' compromessa in modo essenziale.
- Usa P1 quando il task resta possibile ma la UI riduce fiducia, velocita' o
  accuratezza.
- Usa P2 per interventi importanti che migliorano chiarezza e qualita' senza
  bloccare.
- Usa P3 per polish che non deve ritardare una release se P0/P1 sono puliti.
- Non alzare priorita' solo per gusto estetico personale.
- Dichiara incertezza quando l'evidenza e' una descrizione testuale senza
  screenshot o browser.

## Esempio Formato

| Priorita' | Area | Evidenza | Impatto | Suggerimento | Effort | Rischio regressione | Verifica |
|---|---|---|---|---|---|---|---|
| P1 | Dashboard | Warning e stato OK hanno peso visivo simile. | L'utente puo' ignorare problemi critici. | Aumentare contrasto e ordinare alert sopra le metriche secondarie. | M | Medio | Screenshot desktop/mobile e test con dati warning. |
