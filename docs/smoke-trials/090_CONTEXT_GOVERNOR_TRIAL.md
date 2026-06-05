# 090 Context Governor Trial

Skill under trial: `as-common-agent-context-governor`

## Case 1 - Context review pre-step

| Field | Value |
|---|---|
| Input | Repo `Codex_Skills`, hypothetical step 100, multiple candidate skills. |
| Expected output | Context map, active instruction set, open questions, next step. |
| Decision | PASS |

Context map:

| Source | Authority | Active use |
|---|---|---|
| System/developer instructions | Highest | Safety, tool, and coding rules. |
| User step prompt | Step scope | Defines step 100 objective and gates. |
| Repository `AGENTS.md` | Repo rules | Naming, validator, commit/push workflow. |
| Skill docs | Task guidance | Select target skill behavior. |
| Git state | Evidence | Confirms branch, cleanliness, log. |

Active instruction set: follow the current user step, preserve repo rules, run validator and diff gates, do not invent project facts.

Open questions: exact step 100 scope and whether publication is allowed.

Next step: select the narrowest skill set, then run preflight.

## Case 2 - Conflict between instructions

| Field | Value |
|---|---|
| Input | One source says "do not push"; another says "direct main push allowed if gate passes". |
| Expected output | Conflict matrix and decision coherent with D3-C. |
| Decision | PASS |

| Conflict ID | Severity | Source A | Source B | Conflict | Decision | Action |
|---|---|---|---|---|---|---|
| C-090-01 | high | Earlier no-push step | Current step D3-C | Publication rule differs by step. | Current explicit user step controls this step if gates pass. | Permit `git push origin main` only after local gates pass. |

Protected repository warning: if remote branch protection rejects push, switch to branch plus PR as fallback.

## Case 3 - Incomplete AGENTS.md

| Field | Value |
|---|---|
| Input | `AGENTS.md` lacks test commands. |
| Expected output | Missing checklist and proposed correction. |
| Decision | PASS |

Missing checklist:

- setup commands;
- test commands;
- validator commands;
- final verification commands.

Proposed correction:

```markdown
## Verification

- `python validators/test_check_agent_skills.py`
- `python validators/check_agent_skills.py`
- `python validators/check_agent_skills.py --write-index --write-score`
- `git --no-pager diff --check`
```

## Case 4 - Skill overlap

| Field | Value |
|---|---|
| Input | Task may use context governor, verification gate, and report intake. |
| Expected output | Which skill comes first and why. |
| Decision | PASS |

Recommended order:

1. `as-common-agent-context-governor` to map instructions and conflicts.
2. `as-common-verification-gate-test-eval-pack` to define mandatory checks.
3. `as-common-codex-report-intake-decision-gate` to judge the final Codex report.

## Case 5 - Handoff new chat

| Field | Value |
|---|---|
| Input | Close current chat and prepare a new one. |
| Expected output | Prompt seed, known facts, assumptions, open questions. |
| Decision | PASS |

Prompt seed:

```text
Project: Codex_Skills
Current goal: continue after step 090 smoke trial.
Repository: C:\Users\alberto.ferrari\.agents\skills
Branch: main
Known facts: validator exists, catalog and score are generated, D3-C allows direct main push after gates.
Assumptions: working tree should be clean after publication.
Open questions: next step exact scope.
Next recommended step: 100. Skill Release Workflow Pack.
```
