---
name: as-common-codex-step-manager
description: Use this skill when Alberto is managing a numbered Codex/ASF step, including scope, phases, acceptance criteria, report format, completion status, and next recommended step. Do not use it only to draft a one-shot Codex prompt, write persistent runbook documentation, or summarize a chat restart.
---

# Scopo

Gestire step operativi Codex/Git nei progetti software di Alberto in modo ordinato, verificabile e riprendibile.

# Quando usarla

Usala quando Alberto scrive frasi come:
- "vai con STEP ..."
- "procedi con ..."
- "gestisci lo STEP ..."
- "continuiamo dal prossimo step"
- "chiudi/mergea/verifica lo step"
- "fai il prossimo step del progetto"
- "verifica acceptance criteria e report finale"

# Quando non usarla

Non usarla per:
- domande teoriche semplici;
- email commerciali;
- ricerche industriali non legate a una repository;
- modifiche rapide senza workflow Git;
- scrivere solo un prompt Codex temporaneo;
- creare README, AGENTS.md, runbook o documentazione persistente;
- fare un riepilogo di ripartenza per una nuova chat.

# Usa invece

- `as-common-codex-command-pack` quando serve solo un prompt operativo da incollare in Codex.
- `as-common-docs-runbook-builder` quando il risultato deve restare come documentazione di repository.
- `as-common-project-riepilogo-operativo` quando Alberto vuole chiudere una chat lunga e ripartire.

# Metodo operativo

1. Ricostruisci il contesto minimo del progetto: repository, branch principale, step corrente, step precedente, vincoli, test disponibili.
2. Prima di modificare file, fai una verifica iniziale:
   - branch corrente;
   - `git status --short`;
   - ultimi commit rilevanti con `git --no-pager log`;
   - presenza di istruzioni in `AGENTS.md`, README, docs o file di progetto.
3. Se il branch corrente non corrisponde al branch atteso, fermati e segnala il blocco. Non correggere il branch in autonomia salvo richiesta esplicita.
4. Per richieste complesse usa lo schema FASE 1 / FASE 2:
   - FASE 1: riepilogo, assunzioni numerate da 100, domande A/B/C/D con default A, criticità/ottimizzazioni.
   - FASE 2: prompt operativo o modifiche solo quando il flusso del progetto lo prevede o Alberto dà conferma.
5. Mantieni le modifiche piccole, verificabili e coerenti con lo step.
6. Non fare commit, push, PR o merge se non richiesto esplicitamente o se lo step non lo include chiaramente.
7. Alla fine produci sempre un report con:
   - step eseguito;
   - stato sintetico;
   - file creati/modificati;
   - test/verifiche eseguiti;
   - eventuali blocchi o rischi;
   - prossimo step consigliato.
8. Nei report Codex di Alberto includi, quando pertinente, anche:
   - step eseguito e tempo impiegato;
   - step successivo consigliato.

# Formato report finale consigliato

```text
A. Step eseguito
B. Stato
C. File creati/modificati
D. Sintesi modifiche
E. Test eseguiti
F. Verifiche Git
G. Vincoli rispettati
H. Problemi aperti / rischi
I. Prossimo step consigliato
J. Step eseguito e tempo impiegato
```

# Regole importanti

- Preferisci semplicità, leggibilità e manutenzione rispetto a soluzioni troppo sofisticate.
- Non nascondere incertezze: segnala se manca contesto.
- Se un warning Git LF/CRLF compare ma `git diff --check`, test e verify gate passano, trattalo come attenzione, non come fallimento automatico.
- Usa le skill Git/PowerShell dedicate quando il lavoro richiede blocchi di comandi Windows.
