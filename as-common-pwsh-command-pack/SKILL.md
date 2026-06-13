---
name: as-common-pwsh-command-pack
description: Generate safe logged PowerShell command packs for Alberto with short safe bootstraps, generated .ps1 scripts, numbered outputs, optional LAST mirrors on explicit request, compact Markdown/DOCX reports, explicit file handoff, robust Git parsing, PR-first publication, and Git/Codex/ASF guardrails.
---

# as-common-pwsh-command-pack

Use this skill when Alberto asks for PowerShell command packs, robust Windows command sequences, ASF/Git/Codex verification command packs, Bridge/audit artifacts, or logged scripts that produce reusable output files.

Do not use this skill as the default wrapper for Codex prompts. The default Codex handoff is a clean, self-contained prompt. Use PowerShell only when Alberto asks for Bridge output, audit trail, controlled verification, or controlled publication.

## Use Instead

- `as-common-powershell-git-safe-flow` when Alberto needs Git/PowerShell safety review, command rules, or short command guidance rather than a full logged command pack.
- `as-common-codex-command-pack` when Alberto needs a plain Codex prompt handoff without PowerShell artifacts.

## Canonical Standard

Safe Bootstrap PowerShell Command Pack:

1. Generate a short PowerShell bootstrap.
2. The bootstrap writes a complete `.ps1` file in `pwsh_command`.
3. The bootstrap validates parsing with `[scriptblock]::Create($ScriptText) | Out-Null`.
4. Only if parse-check passes, execute `pwsh -NoProfile -ExecutionPolicy Bypass -File $CommandFile`.
5. All complex logic lives in the generated `.ps1`.
6. The pasted terminal block stays short and robust.
7. The outer wrapper does not contain complex Git logic.
8. The outer wrapper does not contain nested here-strings.
9. The outer wrapper does not use fragile `try/finally`.
10. The pasted terminal block starts with `Clear-Host` and ends with `# terminatore copia-incolla` followed by one real blank final line.

## Bootstrap Requirements

The bootstrap must include:

- wrapper `& { ... }`;
- `$ErrorActionPreference = "Stop"`;
- `$PSNativeCommandUseErrorActionPreference = $false`;
- `Clear-Host` as the first executable line in the pasted bootstrap;
- Bridge directory creation;
- request file generation;
- command `.ps1` generation;
- optional `LAST-Richiesta_Generazione.txt` and `LAST-Comando_Eseguito.ps1` only when explicitly requested;
- parse-check with `[scriptblock]::Create($ScriptText) | Out-Null`;
- execution with `pwsh -NoProfile -ExecutionPolicy Bypass -File $CommandFile`;
- explicit `$LASTEXITCODE` handling;
- clear final message;
- paste terminator comment plus one real trailing blank line.

## Generated Script Requirements

The `.ps1` script should contain, when pertinent:

- robust logging;
- full output artifact;
- compact Markdown artifact;
- DOCX best-effort/non-blocking artifact;
- numbered artifacts always updated; `LAST-*` mirrors only when explicitly requested;
- no automatic clipboard write; if Alberto explicitly requests clipboard copy, use `Get-Content -Path $File -Raw | Set-Clipboard` and never `Set-Clipboard -Path`;
- native command wrapper with allowed exit codes;
- `git --no-pager` for long Git output;
- robust Git status parser;
- scope guard before staging;
- direct Git diagnostics for fragile gates;
- staged diff pre-check before Phase B, commit, push, or PR;
- targeted EOF/whitespace recovery only for files named by `git diff --cached --check`;
- Markdown report generation with line arrays instead of long pasted here-strings;
- tests;
- workflow health check;
- verify gate;
- PR-first publication.

Use `ArgList` as the native-command argument parameter name:

```powershell
function Invoke-NativeCommand {
    param(
        [string] $FileName,
        [string[]] $ArgList = @()
    )
}
```

Do not use `$Args` as a parameter name. `$args` is a PowerShell automatic variable and can cause ambiguity and fragile diagnostics.

## Robust Git Parser

Use:

```powershell
git status --porcelain=v1 --untracked-files=all
```

Reason:

- untracked directories are expanded to individual files;
- scope guards can validate exact new files;
- `git add -- @AllowedPaths` becomes safer;
- path slicing bugs are avoided.

Avoid known bugs:

- losing the first character of `AGENTS.md` and reading it as `GENTS.md`;
- treating untracked `templates/pwsh_command_pack/` as an out-of-scope directory instead of checking files inside it;
- using fragile `Substring(3)` without first requiring porcelain v1 format.

## Forbidden Patterns

Do not put these in the pasted bootstrap:

- complex Git logic;
- test suites;
- long functions;
- DOCX XML;
- nested here-strings;
- fragile `try/finally`;
- separable outer `else` blocks;
- direct publication to `main`;
- `git push origin main` as the default;
- function parameters named `$Args`.

Do not expose sensitive values:

- do not print keys;
- do not save keys;
- do not hash keys;
- do not truncate keys;
- do not print prefixes or suffixes;
- do not record key length;
- do not serialize sensitive values into output, artifacts, logs, DOCX, Markdown, JSON, or clipboard.

## Output Contract

Use four-digit step numbers:

```text
0540
0545
0550
```

Generate numbered artifacts:

```text
NNNN-Richiesta_Generazione_<name>.txt
NNNN-Comando_Eseguito_<name>.ps1
NNNN-Output_Completo_<name>.txt
NNNN-Output_Compatto_<name>.md
NNNN-Output_Compatto_<name>.docx
```

Create `LAST-*` mirrors only when Alberto explicitly requests compatibility pointers:

```text
LAST-Richiesta_Generazione.txt
LAST-Comando_Eseguito.ps1
LAST-Output_Completo.txt
LAST-Output_Compatto.md
LAST-Output_Compatto.docx
```

Numbered artifacts are the preferred evidence source for recovery and report intake. `LAST-*` files are convenience pointers and can be stale. When reading an output from the Bridge, prefer the step-specific numbered file cited by the report, use `LAST-*` only as fallback, and verify step, filename, and timestamp/server_modified before trusting it.

DOCX is best-effort. Produce full TXT and compact Markdown first. If DOCX fails, write a non-blocking warning and a `.docx.failed.txt` or placeholder where useful.

## Bridge Retrieval Rule

When an output/log/report path is under:

```text
D:\FG-SAB Dropbox\Alberto Ferrari\ChatGPT_Bridge
```

before asking Alberto to paste the content, try to retrieve it through the Dropbox/Bridge connector if available.

Operational order:

1. Search the specific numbered/progressive file first, for example `0910A-Output_Diagnostica_Diretta_Git_Cached_Diff.txt`.
2. Only if the numbered file is not found, try `LAST-Output_Compatto.md` or `LAST-Output_Completo.txt`.
3. If `LAST` exists but step, filename, timestamp, or server_modified is old or incoherent, say so and do not use it as evidence.
4. If the Bridge is not accessible or the file is not synced/indexed yet, ask Alberto for the smallest useful excerpt, such as `## Cached diff check`, `## Cached diff names`, or `## Git status short`, or ask for the exact numbered path.

Do not ask for "paste everything" by default.

## Direct Git Diagnostics

For critical Git diagnostics, especially after a failure, prefer direct commands with the real command visible:

```powershell
git status --short
git status -sb
git diff --cached --name-status
git diff --cached --check
git diff --name-status
git diff --check
```

Save full output, capture `$LASTEXITCODE` immediately after each command, and continue collecting diagnostic evidence when non-zero exit codes are expected. Avoid generic wrappers that obscure how `git` arguments are passed. Use `git --no-pager` only when the direct form is known to be accepted in that context.

## Markdown Output Generation

For generated Markdown reports, prefer line arrays and explicit joins:

```powershell
$Lines = @()
$Lines += "# Titolo"
$Lines += ""
$Lines += "## Sezione"
$Lines += "testo"
Set-Content -Path $File -Value ($Lines -join "`r`n") -Encoding UTF8
```

Avoid long pasted here-strings containing Markdown, triple backticks, JSON, interpolation, or non-trivial multiline text. Here-strings are acceptable only for short controlled text without truncation risk.

## Cached Diff Recovery

Before relaunching Phase B or any commit/push/PR phase with staged files, run:

```powershell
git diff --cached --check
```

If it fails, stop publication. Read the real output, identify only the reported files, back them up before automatic edits, fix only those files, restage only those files, then rerun:

```powershell
git diff --cached --check
git diff --check
```

Resume Phase B only when both checks pass. For `new blank line at EOF`, remove extra final blank lines only from the files named by the cached diff check, leaving exactly one final newline.

## Publication

Publishing to `main` is PR-first by default:

1. commit on the step branch;
2. push the step branch;
3. run `gh pr create`;
4. run `gh pr merge`;
5. run `git checkout main`;
6. run `git pull --ff-only origin main`;
7. run final verification.

Do not default to `git push origin main`.

If local `main` is ahead of `origin/main`:

```text
main...origin/main [ahead N]
```

Do not push `main` directly. Create a publish branch from local `main`, push that branch, open a PR, merge the PR, realign local `main`, then verify.

## LF/CRLF

LF/CRLF warnings on Windows are non-blocking only when all of these pass:

- `git --no-pager diff --check`;
- tests;
- workflow health check;
- verify gate.

## Provenance

STEP 536 introduced the Safe Bootstrap hardening. STEP 540 validated it in a real ASF publication flow with safe bootstrap plus branch/PR. STEP 545 finalized the reusable draft. STEP 546 exports this file as the installable skill form.
