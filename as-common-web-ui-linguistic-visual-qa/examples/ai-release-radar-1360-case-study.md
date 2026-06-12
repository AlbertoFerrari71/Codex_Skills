# AI Release Radar 1360 Case Study

## Contesto astratto

AI Release Radar e' stato usato come caso reale per estrarre una procedura generale di QA linguistica e visuale. Il problema iniziale era una UI italiana con residui inglesi visibili, mentre il requisito era lasciare invariato solo il nome prodotto `AI Release Radar`.

Il controllo e' stato poi esteso a FR, DE, ES e baseline EN, includendo dashboard, Action Center, dettagli run e distinzione tra UI HTML ed endpoint tecnici.

## Problemi osservati

- Residui inglesi in label localizzate.
- Enum e codici tecnici raw mostrati nella UI invece di label utente.
- Fallback e microcopy non uniformi tra lingue.
- Alcuni testi lunghi in FR/DE con rischio visuale su badge, card o azioni.
- Necessita di distinguere dati tecnici ammessi da difetti reali.

## Metodo utile estratto

- Usare browser reale quando disponibile.
- Se l'in-app Browser non funziona, dichiarare fallback Chrome headless e DOM extraction invece di fingere QA browser.
- Salvare screenshot e visible text in Bridge.
- Cercare termini sospetti nel DOM visibile, non negli endpoint JSON tecnici.
- Classificare ogni sospetto come difetto reale, falso positivo, dato tecnico o lingua baseline.
- Correggere micro-fix tramite mapping o formatter centralizzati.

## Micro-fix esemplificativi

Lezioni astratte emerse da fix reali:

- tradurre label operative come backlog e auto-action quando sono UI utente;
- correggere varianti linguistiche errate come `Revue` o `Auto-Aktion` quando non aderenti al catalogo;
- mantenere `AI Release Radar` come nome prodotto non tradotto;
- non tradurre path, ID, URL, nomi file o dati grezzi chiaramente tecnici.

## Evidenze e gate

Il caso ha usato screenshot/evidenze Bridge, DOM extraction, controllo visuale desktop/mobile e test finali. La PR di riferimento e' stata la #33, con merge finale umano.

## Cosa non va hard-coded

Questa skill non deve incorporare route, testi o workflow specifici di AI Release Radar. Il caso serve solo a giustificare pattern riusabili:

- separare UI da endpoint tecnico;
- usare allowlist esplicita;
- pretendere evidenze visuali o fallback equivalente;
- preferire micro-fix controllati;
- raccomandare merge solo dopo review umana.