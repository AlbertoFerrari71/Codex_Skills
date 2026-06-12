# Web UI Linguistic Visual QA Adoption

## Quando usarla

Usare `as-common-web-ui-linguistic-visual-qa` quando una web app locale o una dashboard deve essere controllata per traduzioni, residui lingua baseline, enum raw, DOM visible text e difetti visuali legati a testi lunghi.

Usare `as-common-web-ui-design-review` quando il bisogno principale e' UX, gerarchia visiva, estetica, contrasto o anti-AI-slop senza focus i18n/linguistico.

## Preparare input

Raccogliere:

- repo path e branch/PR;
- comando server locale e base URL;
- lingue e baseline;
- pagine minime;
- endpoint tecnici da escludere dai difetti UI;
- allowlist prodotto/termini;
- cartella Bridge evidenze;
- test/validator;
- divieti su pulsanti operativi.

## Leggere il report

Leggere prima stato finale, metodo browser/fallback e copertura. Un report senza screenshot, visible text o fallback equivalente non basta per dichiarare browser QA.

Poi controllare:

- `Visual_QA_Matrix.md` per copertura pagine/lingue/viewport;
- `DOM_Suspects.json` per difetti e falsi positivi;
- `Review_Notes.md` per limiti e decisione;
- screenshot e file `visible_text_*` come evidenza primaria.

## Decidere merge/no merge

Raccomandare merge umano solo se:

- pagine e lingue richieste sono coperte;
- browser o fallback equivalente e' dichiarato;
- difetti reali P0/P1 sono assenti o corretti;
- test/gate richiesti sono PASS;
- repo target non e' contaminato;
- warning e falsi positivi sono classificati.

Usare `PARTIAL_PR_NEEDS_FIX` o `BLOCKED_*` quando browser/fallback, test, Git state o scope non sono sufficienti.

## Browser non disponibile

Se l'in-app Browser non funziona:

1. dichiarare il fallimento;
2. provare Chrome headless, Playwright, Selenium o HTTP DOM extraction;
3. salvare comunque visible text e screenshot se possibile;
4. spiegare cosa resta non verificato;
5. non scrivere `PASS_READY_FOR_HUMAN_MERGE` senza evidenza equivalente.

## UI vs endpoint tecnico

Trattare come UI utente solo testo visibile in HTML o componenti renderizzati. Trattare come tecnico, salvo diversa richiesta:

- JSON API;
- log;
- path, URL, ID, file name;
- raw report scaricabili;
- payload diagnostici.

Un dato tecnico puo' essere mostrato nella UI, ma deve essere presentato chiaramente come dato tecnico e non come label localizzata.

## Falsi positivi

Classificare falsi positivi invece di cancellarli. Esempi frequenti:

- nome prodotto non tradotto;
- acronimi tecnici;
- ID o file name;
- endpoint o path;
- baseline EN quando la pagina e' volutamente in inglese;
- parole brevi trovate come substring, ad esempio `pass` dentro `passo` o parole tedesche;
- titoli o snippet originali mostrati come contenuto sorgente, se la UI li etichetta chiaramente.

## Micro-fix

Trasformare finding in micro-fix solo se autorizzato:

- mapping enum/stati in un formatter centralizzato;
- cataloghi i18n invece di hardcoding nei template;
- label brevi e coerenti;
- fallback localizzati;
- CSS minimo per overflow di testi lunghi.

Evitare redesign, find/replace cieco e test pixel-perfect fragili.

## Evitare contaminazione repo target

In modalita read-only:

- non creare branch, commit o PR nel repo target;
- non scrivere evidenze dentro il repo target;
- usare Bridge o temp esterna;
- controllare `git status` prima e dopo;
- fermare solo server avviati dallo step.

## Lezione dai pilot 1410/1420

Dopo i pilot AI Release Radar e ASF Blueprint Studio, trattare come regola pratica:

- usare confini parola per termini brevi;
- conservare uno snippet per ogni sospetto;
- non classificare app English-baseline come non localizzate se non esistono target language;
- separare contenuto originale/dinamico, report raw e sezioni collassate dalle label della UI.