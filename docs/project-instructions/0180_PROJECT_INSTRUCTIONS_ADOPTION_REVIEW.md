# 0180) Project Instructions Adoption Review

## Scopo

Verificare l'adozione reale della skill `as-common-project-instructions-builder`
nel repository `Codex_Skills` e rafforzare i casi trigger-eval per evitare
collisioni con skill vicine.

## Fatto dichiarato da Alberto

Alberto ha dichiarato di aver incollato nella UI ChatGPT il testo delle Project
Instructions prodotte dopo lo step 0170. Questa adozione non e' verificabile
localmente da Codex e va trattata come dichiarazione di Alberto, non come fatto
validato nel repository.

## Cosa e' verificabile localmente

- `AGENTS.md` contiene una sezione breve dedicata al workflow
  `as-common-project-instructions-builder`.
- `docs/project-instructions/0160_CODEX_SKILLS_PROJECT_INSTRUCTIONS.md`
  conserva la versione compatta, il documento esteso e la checklist applicata.
- La skill `as-common-project-instructions-builder` include trigger, anti-trigger,
  template, checklist e source map coerenti con il documento 0160.
- README, CHANGELOG, `SKILLS_INDEX.md` e validator riconoscono la skill e i gate
  di trigger-eval.

## Skill confrontate

- `as-common-project-instructions-builder`
- `as-common-project-riepilogo-operativo`
- `as-common-codex-command-pack`
- `as-common-codex-step-manager`
- `as-common-codex-report-intake-decision-gate`
- `as-common-agent-context-governor`
- `as-common-repo-readiness-review`
- `as-common-docs-runbook-builder`
- `as-common-skill-authoring`
- `as-common-verification-gate-test-eval-pack`

## Collisioni potenziali

- Istruzioni durevoli di progetto vs riepilogo di ripartenza chat.
- Project Instructions e `AGENTS.md` vs prompt Codex temporaneo.
- Audit istruzioni progetto vs governance puntuale del contesto agente.
- `AGENTS.md` come istruzione agentica vs documentazione/runbook generico.
- Quality gate delle istruzioni vs verification gate di uno step Codex.
- Trasformare una procedura in skill per istruzioni progetto vs authoring
  generico di una nuova skill.

## Casi trigger-eval aggiunti

`validators/trigger_eval_cases.json` e' stato esteso senza cambiare formato:
lista di oggetti con `id`, `input`, `expected_skill`, `negative_skills` e `tags`.

Aggiunti 6 casi positivi per `as-common-project-instructions-builder`:

- istruzioni perfette per un progetto;
- Project Instructions ChatGPT per una repo;
- `AGENTS.md` consigliato con regole Codex e gate locali;
- audit delle istruzioni progetto;
- procedura trasformata in skill trasversale per creare istruzioni progetto;
- nuovo progetto con istruzioni personalizzate per ChatGPT e Codex.

Aggiunti 8 casi negativi che devono instradare altrove:

- riepilogo operativo e prompt di ripartenza;
- prompt Codex temporaneo per uno step;
- report intake GO/NO_GO;
- authoring generico di skill;
- readiness review read-only;
- runbook tecnico stabile;
- pulizia/governance del contesto agente;
- test gate, smoke, eval e stop policy.

Aggiunti 5 casi borderline:

- skill per handoff dei progetti;
- update di `AGENTS.md` con regole agentiche e quality gate;
- istruzioni Codex per uno step specifico;
- review delle istruzioni progetto seguita da prompt Codex per installarle;
- riepilogo operativo con istruzioni per una nuova chat.

## Decisioni prese

- Nessuna modifica al contenuto della skill: i trigger e gli anti-trigger sono
  gia' coerenti e sufficientemente espliciti.
- Nessuna modifica ad `AGENTS.md`: la sezione aggiunta nello step 0170 e'
  compatta e non sostituisce README, validator o workflow di release.
- Nessuna modifica a `validators/smoke_trial_cases.py`: quello smoke trial
  valida il comportamento del validator su repository temporanee; la copertura
  trigger-eval vive in `validators/trigger_eval_cases.json` e
  `validators/test_trigger_eval.py`.
- Nessun campo nuovo nel JSON trigger-eval: motivazioni e secondary skill sono
  documentate qui per non cambiare lo schema consolidato.

## Rischi residui

- Il trigger `AGENTS.md` resta intenzionalmente borderline: se Alberto chiede
  un `AGENTS.md` agentico o Project Instructions, usare
  `as-common-project-instructions-builder`; se chiede documentazione operativa
  generica, usare `as-common-docs-runbook-builder`.
- Le Project Instructions nella UI ChatGPT non sono verificabili localmente.
- Il trigger-eval e' deterministico e strutturale: non misura routing AI reale,
  embedding o classificazione semantica.

## Prossimo step consigliato

`0190) Codex Skills - Trigger Eval Semantic Trial`

Eseguire una prova manuale o assistita su prompt reali brevi per verificare che
le skill selezionate dai nuovi casi coincidano con il comportamento atteso in
chat, senza introdurre un classificatore automatico prematuro.
