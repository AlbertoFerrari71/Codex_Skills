# Demo Prompts

## 1. Create verification gate for a Python/FastAPI step

User request:

```text
Create a verification gate for this FastAPI change before commit. Include unit tests, import smoke, route health check, Git diff check, and final GO/NO-GO decision.
```

Expected use of this skill:

- classify risk;
- build a matrix;
- define mandatory commands;
- state stop conditions.

Expected output:

- verification matrix;
- ordered command list;
- not-run policy;
- final report template.

## 2. Create verification gate for a PowerShell/Git workflow

User request:

```text
Design a verification gate for a PowerShell command pack that can commit only after local checks pass.
```

Expected use of this skill:

- separate local verification from publication actions;
- require `git status --short` and `git --no-pager diff --check`;
- define no-publish behavior on failed gates.

Expected output:

- phase gate;
- mandatory commands;
- failure policy;
- final evidence list.

## 3. Create eval pack for Codex report quality

User request:

```text
Create an eval pack to check whether Codex final reports include files changed, commands run, failures, warnings, not-run checks, and next step.
```

Expected use of this skill:

- create representative cases;
- define pass criteria;
- choose manual or checklist grading.

Expected output:

- eval matrix;
- grading method;
- regression notes.

## 4. Create golden sample policy for document generation

User request:

```text
Define how this project should use golden samples for generated Markdown reports without making comparisons too brittle.
```

Expected use of this skill:

- define folder names;
- decide update approval;
- separate structural checks from exact text checks.

Expected output:

- golden sample policy;
- checklist;
- update procedure.

## 5. Review a failed test report and decide GO / NO-GO

User request:

```text
The unit tests failed but docs are updated. Review the report and decide whether the step can proceed to push.
```

Expected use of this skill:

- classify the failure;
- enforce no publication when mandatory checks fail;
- produce corrective action.

Expected output:

- NO-GO decision;
- failed evidence;
- correction prompt or next step.

## 6. Build a smoke test checklist for a UI flow

User request:

```text
Build a smoke checklist for the login and dashboard UI flow before merge.
```

Expected use of this skill:

- identify primary user path;
- define screenshot or Playwright evidence;
- connect UI check to release gate.

Expected output:

- smoke checklist;
- mandatory vs optional UI checks;
- not-run handling.
