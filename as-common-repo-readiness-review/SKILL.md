---
name: as-common-repo-readiness-review
description: "Usa questa skill per fare una revisione tecnica iniziale read-only di una repository prima di uno step Codex: branch, stato Git, struttura, test, documenti, rischi e readiness. Non usarla per riconciliare istruzioni, AGENTS.md o conflitti di contesto agente."
---

# Scopo

Usa questa skill per fare una revisione iniziale read-only di una repository prima di iniziare uno step Codex.

# Quando usarla

Usala quando Alberto chiede di verificare se una repository è pronta per uno step, oppure quando bisogna controllare branch, stato Git, documentazione, test e rischi prima di modificare file.

# Quando non usarla

Non usarla per:
- riconciliare istruzioni di sistema, developer, AGENTS.md, prompt e skill;
- decidere quale skill usare quando il problema principale e' un conflitto di contesto;
- preparare handoff o mappe delle fonti istruzione.

# Usa invece

- `as-common-agent-context-governor` quando il rischio riguarda istruzioni contraddittorie, gerarchie di contesto, AGENTS.md o skill conflict.

# Procedura

1. Non modificare file.
2. Controllare branch corrente.
3. Controllare `git status --short`.
4. Leggere i documenti operativi rilevanti se presenti.
5. Identificare test e verification gate disponibili.
6. Evidenziare rischi, blocchi e ambiguità.
7. Chiudere con readiness sintetica: pronto, pronto con attenzioni, oppure bloccato.

# Output atteso

- Stato repository.
- Branch corrente.
- File/documenti chiave trovati.
- Test/verifiche disponibili.
- Rischi o blocchi.
- Prossimo step consigliato.
