---
name: as-common-deep-research-industriale
description: Usa questa skill quando Alberto deve impostare o scrivere una ricerca tecnica industriale con fonti su materiali, prodotti chimici/minerali, processi, norme, brevetti tecnici, fornitori, benchmark, mercato o stime tecnico-economiche. Non usarla per email, debug codice, prompt Codex, UI review o curiosita generiche senza ricerca.
---

# Scopo

Trasformare una domanda tecnica o industriale in una ricerca strutturata, rigorosa e utile per decisioni R&D, acquisto, laboratorio o business.

# Quando usarla

Usala per ricerche su:
- materiali e additivi;
- prodotti chimici, minerali, cementi, malte, calcestruzzi e coating;
- microdiamanti, glitter, superfici tecniche e trattamenti;
- norme tecniche, standard di prova e requisiti di settore;
- scouting fornitori, prodotti industriali, schede tecniche e comparazioni;
- processi produttivi, parametri di processo e tecnologie emergenti;
- freni, FEM, materiali ad alta temperatura;
- brevetti usati come fonte tecnica, senza trasformarli in parere legale;
- benchmark industriale e scouting competitivo;
- stime tecnico-economiche esplicitamente marcate come stime;
- prompt Deep Research quando serve delegare una ricerca web strutturata.

# Quando NON usarla

Non usarla per:
- semplice riassunto di testo gia fornito senza bisogno di ricerca;
- email commerciale, HR o negoziale: usa `as-common-business-email-draft`;
- debug codice, FastAPI o pytest: usa `as-common-python-fastapi-debug`;
- pipeline immagini OpenCV: usa `as-common-opencv-image-pipeline`;
- project instructions, AGENTS.md o quality gate di progetto: usa `as-common-project-instructions-builder`;
- review visuale UI/web: usa `as-common-web-ui-design-review`;
- prompt Codex operativo: usa `as-common-codex-command-pack`;
- curiosita generica senza decisione tecnica, fonti o output pratico.

# Usa invece

- `as-common-technical-patent-draft` quando Alberto deve preparare disclosure, bozze tecniche o materiale per il consulente brevettuale.
- `as-common-model-effort-advisor` quando la domanda e' solo quale livello/modello usare.
- `as-common-docs-runbook-builder` quando il risultato deve diventare procedura o runbook persistente.

# Metodo

1. Chiarisci obiettivo decisionale: cosa deve decidere Alberto dopo la ricerca.
2. Dividi il lavoro in livelli:
   - versione divulgativa;
   - approfondimento tecnico;
   - implicazioni pratiche per laboratorio/azienda.
3. Cerca o richiedi fonti aggiornate quando il tema e' aggiornabile, normativo, commerciale, prezzi, prodotti, fornitori, standard, persone o mercato.
4. Se Codex non ha web access, prepara un prompt Deep Research completo e segnala che le fonti vanno raccolte altrove.
5. Separa sempre:
   - fatti verificati;
   - fonti e citazioni;
   - stime;
   - ipotesi;
   - opinioni e raccomandazioni operative.
6. Valuta qualita e limiti delle fonti, distinguendo norme, datasheet, brevetti, articoli, pagine commerciali e inferenze.
7. Concludi con test pratici consigliati, rischi, dosaggi preliminari, criteri di successo/fallimento e decisione consigliata.

# Output tipo

```markdown
# Obiettivo della ricerca
# Sintesi esecutiva
# Quadro tecnico
# Tabella fonti
# Tabella dati e parametri
# Stato dell'arte e brevetti come fonti tecniche
# Applicazioni industriali
# Parametri/formulazioni da testare
# Incertezze e ipotesi
# Piano prove laboratorio
# Rischi e criticità
# Opportunità business/R&D
# Decisione consigliata
```

# References

- `references/research-output-rubric.md`
- `references/source-quality-and-uncertainty.md`

# Regole

- Non trasformare in marketing.
- Non dare dati numerici non verificati come certi.
- Quando mancano fonti, scrivere chiaramente cosa manca.
- Per tecnologie brevettabili, distinguere ispirazione tecnica da libertà di operare.
- Non presentare una pagina commerciale come prova tecnica senza indicarne il bias.
- Non sostituire norme o standard con memoria: verificare sempre versione, ente e data quando contano.
