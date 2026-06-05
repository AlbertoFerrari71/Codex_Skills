# Demo Prompts

## 1. Review Codex report and decide GO/NO-GO

User request:

```text
Review this final Codex report against the original prompt, Git status, diff, and tests. Decide GO, GO_WITH_WARNINGS, NO_GO_FIXABLE, NO_GO_BLOCKER, or NEEDS_CLARIFICATION.
```

Expected use of this skill:

- extract report claims;
- map each claim to evidence;
- classify missing checks and warnings.

Expected output:

- intake summary;
- evidence checklist;
- decision gate;
- next action.

## 2. Generate corrective prompt after missing tests

User request:

```text
The report says validation was done but does not list commands. Prepare a corrective Codex prompt.
```

Expected use of this skill:

- use the missing verification template;
- require exact commands and final status;
- keep no-commit/no-push constraints.

Expected output:

- corrective prompt;
- required commands;
- expected final report.

## 3. Review unexpected file changes

User request:

```text
Git status shows files that were not in the prompt. Review whether this blocks the step.
```

Expected use of this skill:

- compare expected and actual paths;
- inspect name-status and targeted diffs;
- classify the decision.

Expected output:

- changed-file review;
- decision impact;
- corrective action if needed.

## 4. Prepare commit/push PowerShell after GO

User request:

```text
The gate is GO. Prepare a PowerShell command pack to commit and push this step.
```

Expected use of this skill:

- use the readiness template;
- include pre-commit checks;
- stage intended paths only.

Expected output:

- PowerShell command template;
- checks before commit;
- final status/log commands.

## 5. Classify warning vs blocker

User request:

```text
The report has CRLF warnings and one failed mandatory test. Classify the gate.
```

Expected use of this skill:

- separate non-blocking line-ending notices from failed mandatory checks;
- apply decision matrix.

Expected output:

- warning classification;
- NO_GO_FIXABLE or NO_GO_BLOCKER decision;
- next corrective action.

## 6. Review docs-only Codex step

User request:

```text
Review a docs-only Codex report and decide if the step can be accepted without running code tests.
```

Expected use of this skill:

- verify docs scope;
- check changelog/index updates;
- classify not-run code tests with reason.

Expected output:

- docs evidence review;
- not-run check rationale;
- GO or GO_WITH_WARNINGS decision.
