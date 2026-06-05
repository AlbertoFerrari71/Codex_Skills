# Demo Prompts

These examples show progressive uses of `as-common-pwsh-command-pack`. Each prompt should produce a `.ps1` script, numbered artifacts, LAST artifacts, compact Markdown/DOCX output, and clipboard copy.

## Demo 1 - Read-only Git snapshot

```text
Use as-common-pwsh-command-pack.
Create a PowerShell command pack that checks the current repository branch, git status, last 5 commits, and git diff --check.
No commit, push, PR, merge, release, deploy, or destructive command.
Output under the ASF pwsh_command Bridge folder.
```

Expected shape:

- FASE A only.
- Uses `git --no-pager`.
- Stops on native command failures.
- Produces numbered and LAST artifacts.

## Demo 2 - ASF verification pack

```text
Use as-common-pwsh-command-pack.
Create a robust ASF local verification command pack for C:\Users\alberto.ferrari\source\repos\AI_Software_Factory.
Run python -m pytest, scripts/verify.ps1 if present, python scripts/check_workflow_health.py, git --no-pager diff --check, and git --no-pager status --short.
Do not publish anything.
```

Expected shape:

- FASE A only.
- `pwsh -NoProfile -ExecutionPolicy Bypass -File` launcher.
- Compact report states pass/fail and warnings.
- Clipboard receives `LAST-Output_Compatto.md`.

## Demo 3 - Human-gated PR checks

```text
Use as-common-pwsh-command-pack.
Create a PowerShell command pack with FASE A local verification and optional FASE B PR checks.
FASE B may run gh pr checks --watch only after FASE A passes.
Treat no checks reported / exit code 1 as warning only if all local gates pass.
No commit, push, PR create, merge, release, or deploy.
```

Expected shape:

- FASE A and FASE B are separate.
- `gh pr checks --watch` warning handling is explicit.
- Publication remains blocked by failed tests, verify, health check, or guardrails.

## Demo 4 - Publication-separated pack

```text
Use as-common-pwsh-command-pack.
Create a command pack for a workflow that includes local tests and a later manual publication phase.
FASE A runs verification only.
FASE B lists the manual commit/push/PR commands as review text but does not execute them unless Alberto explicitly asks for a separate publication pack.
FASE C is out of scope.
```

Expected shape:

- No hidden publication.
- The compact output states what was executed and what remains manual.
- Failed verification blocks later phases.