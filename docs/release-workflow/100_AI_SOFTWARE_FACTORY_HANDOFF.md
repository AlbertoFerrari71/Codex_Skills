# 100 AI Software Factory Handoff

## Current `Codex_Skills` state

The skill repository now has a stable catalog, validator, smoke trial pack, PowerShell hardening rules, and release workflow documents.

Strategic skills available:

- `as-common-agent-context-governor`;
- `as-common-verification-gate-test-eval-pack`;
- `as-common-codex-report-intake-decision-gate`;
- `as-common-pwsh-command-pack`;
- `as-common-powershell-git-safe-flow`.

## How to use these skills in the next ASF step

1. Start with `as-common-agent-context-governor` to rebuild current ASF context, repo state, active instructions, and applicable skills.
2. Use `as-common-verification-gate-test-eval-pack` to define tests, smoke checks, stop policy, and GO/NO-GO evidence before changing ASF.
3. Use `as-common-codex-report-intake-decision-gate` to review the final Codex report against the prompt, Git state, diffs, and tests.
4. Use `as-common-pwsh-command-pack` when Alberto needs robust PowerShell command packs with logs, artifacts, clipboard, and publication gates.
5. Use `as-common-powershell-git-safe-flow` for compact Git/PowerShell command review and paste-safe blocks.

## Recommended ASF restart

Recommended next step: identify the next actionable ASF workflow step, then run a context and verification planning pass before implementation.

The first ASF action should be read-oriented unless Alberto gives a concrete implementation step.

## Prompt seed for AI Software Factory restart

```text
Ripartiamo dal progetto AI Software Factory usando le skill operative aggiornate nella repository Codex_Skills. Prima di proporre lo step successivo, usa la logica di as-common-agent-context-governor per ricostruire contesto, vincoli attivi, stato repo e skill applicabili. Poi prepara il prossimo step con verification gate esplicito e report intake finale.
```

## Handoff checklist

- Confirm ASF repository path and branch.
- Confirm latest ASF commit and working tree status.
- Identify whether the next ASF step is read-only, docs-only, implementation, release, or cleanup.
- Define mandatory checks before editing.
- Define publication policy before commit/push.
- Record open questions before running Codex implementation.
