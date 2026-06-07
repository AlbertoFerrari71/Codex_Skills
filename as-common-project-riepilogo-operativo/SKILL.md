---
name: as-common-project-riepilogo-operativo
description: Usa questa skill quando Alberto chiede un riepilogo operativo di continuità per chiudere una chat lunga e ripartire in una nuova chat dello stesso progetto. Non usarla per README, runbook o documentazione persistente di repository.
---

# Scopo

Creare un riepilogo operativo compatto ma completo per chiudere una chat lunga e ripartire in una nuova chat dello stesso progetto.

# Quando usarla

Usala quando Alberto scrive:
- "fai riepilogo"
- "prepara riassunto"
- "riassunto"
- "fai un prompt di ripartenza"
- "chiudiamo questa chat"
- "ripartiamo in una nuova chat"

# Quando NON usarla

Non usarla per:
- creare o aggiornare README, AGENTS.md, runbook o documentazione stabile;
- gestire il ciclo completo di uno step Codex numerato;
- preparare solo un prompt temporaneo per Codex.

# Usa invece

- `as-common-docs-runbook-builder` quando il risultato deve restare come documentazione persistente nel repository.
- `as-common-codex-step-manager` quando Alberto sta governando uno step numerato.
- `as-common-codex-command-pack` quando serve solo un prompt operativo da incollare in Codex.

# Metodo

1. Identifica il progetto.
2. Conserva solo informazioni utili per ripartire.
3. Elimina rumore operativo, tentativi falliti non più rilevanti e dettagli non necessari.
4. Non inventare dati mancanti.
5. Se manca un dato, scrivi: `non chiarito nella chat`.
6. Separa fatti certi, ipotesi e decisioni.
7. Prepara un prompt finale copiabile nella nuova chat.
8. Il titolo consigliato della nuova chat deve usare numerazione progressiva passo 10 quando il contesto lo consente, nel formato:
   ```text
   XXX) titolo breve e chiaro
   ```

# Formato output obbligatorio

```markdown
# Titolo consigliato nuova chat

# Contesto del progetto

# Stato attuale

# Decisioni prese

# File, cartelle e repository coinvolti

# Problemi risolti

# Problemi aperti / rischi

# Prossimo step consigliato

# Prompt di ripartenza pronto da copiare
```

# Regole

- Non aggiungere spiegazioni generiche.
- Non fare cronologia completa della chat.
- Non includere tentativi falliti salvo che servano a evitare di ripetere errori.
- Mantieni nomi di branch, commit, path e step esattamente come emersi.
- Se il progetto usa ChatGPT + Codex, conserva sempre l’ultimo step eseguito e il prossimo step operativo.
