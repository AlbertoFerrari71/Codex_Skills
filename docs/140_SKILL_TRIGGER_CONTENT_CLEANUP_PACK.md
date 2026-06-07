# 140 - Skill Trigger & Content Cleanup Pack

## Obiettivo

Ridurre collisioni di routing tra skill vicine con modifiche piccole e
verificabili a description, anti-trigger e cross-reference.

## Skill toccate

Gruppo A - Prompt Codex, step, documentazione:

- `as-common-codex-command-pack`
- `as-common-codex-step-manager`
- `as-common-docs-runbook-builder`

Gruppo B - Riepilogo operativo vs documentazione persistente:

- `as-common-project-riepilogo-operativo`
- `as-common-docs-runbook-builder`

Gruppo C - PowerShell/Git:

- `as-common-pwsh-command-pack`
- `as-common-powershell-git-safe-flow`

Gruppo D - Gate progettato vs report ricevuto:

- `as-common-verification-gate-test-eval-pack`
- `as-common-codex-report-intake-decision-gate`

Gruppo E - Repo readiness vs context governor:

- `as-common-repo-readiness-review`
- `as-common-agent-context-governor`

## Confini chiariti

- `as-common-codex-command-pack`: prompt o command packet temporaneo da passare
  a Codex.
- `as-common-codex-step-manager`: lifecycle di uno step numerato, con scope,
  acceptance criteria, stato e report finale.
- `as-common-docs-runbook-builder`: documentazione persistente nel repository.
- `as-common-project-riepilogo-operativo`: riepilogo di continuita per nuova
  chat, non README/runbook.
- `as-common-pwsh-command-pack`: pacchetto PowerShell operativo completo con
  Bridge, script, log e report.
- `as-common-powershell-git-safe-flow`: regole e comandi Git/PowerShell sicuri,
  senza artifact completi.
- `as-common-verification-gate-test-eval-pack`: progettazione di gate, test,
  smoke, eval e stop policy.
- `as-common-codex-report-intake-decision-gate`: decisione su un report Codex
  gia ricevuto.
- `as-common-repo-readiness-review`: readiness tecnica read-only di una repo.
- `as-common-agent-context-governor`: gerarchie istruzioni, AGENTS.md, skill e
  conflitti di contesto.

## Policy description

- Usare inglese tecnico semplice per skill strategiche o Codex-facing.
- Usare italiano per skill personali o di dominio Alberto.
- Accettare un mix controllato quando migliora il trigger.
- Rendere ogni description concreta: quando usarla, quando non usarla, e quale
  skill usare invece in caso di overlap.

## Fuori scope

Non implementati in questo step:

- installed skills sync checker;
- telemetria uso skill;
- policy definitiva `LAST-*`;
- nuove skill;
- scoring v3;
- routing AI reale, API AI o embedding.

## Prossimo step

Se i gate passano, il prossimo step consigliato e':

`140-B) Review and Commit Skill Trigger Content Cleanup`
