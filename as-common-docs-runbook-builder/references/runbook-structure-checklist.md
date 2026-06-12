# Runbook Structure Checklist

Un runbook persistente deve essere eseguibile anche da chi non ha letto la chat.

## Campi essenziali

- Scopo.
- Ambito e quando usarlo.
- Prerequisiti.
- Input necessari.
- Passi operativi numerati.
- Comandi con shell o ambiente indicato.
- Verifiche attese.
- Condizioni di stop.
- Rollback, se disponibile.
- Troubleshooting.
- Ownership o responsabile.
- Quando aggiornarlo.

## Controlli

- I comandi sono verificati o marcati come da verificare?
- I path sono espliciti?
- Il runbook distingue azione manuale e automazione?
- Ci sono gate prima di operazioni irreversibili?
- Il documento evita duplicazioni inutili con README o AGENTS?
