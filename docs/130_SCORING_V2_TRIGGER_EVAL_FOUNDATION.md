# 130 - Scoring v2 & Trigger Eval Foundation

## Obiettivo

Lo step 130 separa lo score strutturale dalla qualita operativa e introduce una
base trigger-eval deterministica per controllare collisioni di routing tra skill.

## StructureScore

`StructureScore` misura igiene, installabilita e riproducibilita. Le voci
valgono 10 punti ciascuna:

- nome cartella valido e con prefisso atteso;
- `SKILL.md` presente e leggibile;
- frontmatter valido;
- `name:` coerente con la cartella;
- `description:` presente e con lunghezza accettabile;
- sezione operativa minima riconoscibile;
- assenza di backup/temp file nella skill attiva;
- `references/` ed `examples/` reali se dichiarati o assenti se non richiesti;
- link-check `references/`/`examples/` senza file mancanti;
- nessun warning o errore validator.

Cartelle `references/` o `examples/` vuote non danno punti cosmetici.

## OperationalQualityScore

`OperationalQualityScore` misura in modo euristico la chiarezza operativa:

- trigger chiaro nella description;
- description specifica e non generica;
- frasi o sezioni "quando usarla";
- frasi o sezioni "quando non usarla" / "non usare";
- output contract riconoscibile;
- examples o references con file reali;
- cross-reference come "usa invece";
- vincoli reali Alberto/Codex/PowerShell/Git;
- bassa collisione testuale semplice con description di skill vicine.

Questo score non usa AI, API, embedding o classificatori semantici. E' un
segnale conservativo per orientare cleanup futuri, non una valutazione assoluta.

## Cataloghi

Rigenerare indice e score:

```powershell
python validators\check_agent_skills.py --root . --write-index --write-score
```

Eseguire il validator severo:

```powershell
python validators\check_agent_skills.py --root . --fail-on-warning
```

## Trigger eval

I casi trigger-eval sono in:

- `validators/trigger_eval_cases.json`
- `validators/test_trigger_eval.py`

Il runner e' incluso nel discovery standard:

```powershell
python -m unittest discover -s validators -p test_*.py
```

Esecuzione singola:

```powershell
python -m unittest validators.test_trigger_eval
```

Il test controlla formato JSON, ID univoci, input non vuoti, tags presenti,
skill attese esistenti, negative skill esistenti e assenza di conflitto tra
expected e negative.

## Fuori scope

Restano fuori scope:

- orchestrazione reale di modelli AI;
- chiamate API OpenAI/Claude;
- embedding;
- classificatore semantico avanzato;
- sync checker tra repository e skill installate;
- policy definitiva `LAST-*`;
- cleanup massivo delle description.

## Prossimo step

Se i gate locali passano, il prossimo step consigliato e':

`130-B) Review and Commit Scoring v2 and Trigger Eval Foundation`
