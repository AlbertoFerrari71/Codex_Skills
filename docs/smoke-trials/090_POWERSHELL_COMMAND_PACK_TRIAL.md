# 090 PowerShell Command Pack Trial

Skills under trial:

- `as-common-pwsh-command-pack`
- `as-common-powershell-git-safe-flow`

## Cases

| Case | Input / condition | Expected behavior | Decision |
|---:|---|---|---|
| 1 | One useful command plus two fake lines. | Useful command terminates before any possible wait. | PASS |
| 2 | Two useful commands plus one fake line. | Both useful commands terminate before fake line. | PASS |
| 3 | Complex block uses one `& { ... }`. | Paste-safe wrapper. | PASS |
| 4 | Separable `if/else` block. | Mark risky; prefer wrapper or `.ps1`. | PASS |
| 5 | `$StepOk` controlled success. | Completion printed only after `$StepOk = $true`. | PASS |
| 6 | UTF-8 without BOM via .NET. | `[System.Text.UTF8Encoding]::new($false)` present. | PASS |
| 7 | `AllowNull` / `AllowEmptyString`. | File/log helpers accept empty content where valid. | PASS |
| 8 | Git porcelain v1. | Use `git status --porcelain=v1` for parsing. | PASS |
| 9 | File outside `$allowedPaths`. | Block before staging/commit. | PASS |
| 10 | Cached diff check. | Run before commit. | PASS |
| 11 | DOCX non-blocking and temp outside Dropbox. | DOCX failure warning, Markdown continues. | PASS |
| 12 | Clipboard in error. | Compact output attempted in `finally`. | PASS |

## Case 1 - Paste termination, one useful command

```powershell
Get-Date
Write-Host "Linea fake 1 - termina il comando utile precedente"
Write-Host "Linea fake 2 - se resta in attesa, premere Enter qui"
```

Expected result:

- `Get-Date` executes;
- if the paste loses the final newline, waiting occurs on a fake line, not on `Get-Date`.

## Case 2 - Paste termination, two useful commands

```powershell
Get-Date
Get-Date
Write-Host "Linea fake - se resta in attesa, premere Enter qui"
```

Expected result: both useful commands execute before any possible wait.

## Case 3 - Single wrapper

Required shape:

```powershell
& {
    $ErrorActionPreference = "Stop"
    # all conditional logic here
}
```

Expected result: no standalone `if` or `else` fragment is left vulnerable to paste splitting.

## Case 4 - Separable if/else risk

Risky shape:

```powershell
if ($ok) {
    Write-Host "OK"
}
else {
    Write-Host "NO"
}
```

Expected behavior: mark as risky for paste-heavy workflows; use one wrapper or save a real `.ps1`.

## Case 5 - Controlled `$StepOk`

Expected behavior: success text appears only after all mandatory gates pass.

## Case 6 - UTF-8 without BOM via .NET

Required implementation:

```powershell
[System.Text.UTF8Encoding]::new($false)
```

Do not depend on host-specific `Set-Content -Encoding utf8NoBOM` behavior.

## Case 7 - Empty string parameters

Expected behavior: standard helpers use `AllowNull` and `AllowEmptyString` where empty logs or files are valid.

## Case 8 - Git porcelain v1

Required command:

```powershell
git status --porcelain=v1
```

Expected behavior: parse status and path separately. Do not parse human output from `git status --short`.

## Case 9 - `$allowedPaths`

Condition: `git status --porcelain=v1` reports `M unrelated/file.txt`.

Expected behavior: block because the path is outside `$allowedPaths`.

## Case 10 - Cached diff check

Required command before commit:

```powershell
git --no-pager diff --cached --check
```

Expected behavior: commit is blocked if staged whitespace errors exist.

## Case 11 - DOCX non-blocking / temp outside Dropbox

Expected behavior:

- DOCX conversion failure logs a warning;
- compact Markdown remains authoritative;
- temporary DOCX work uses `$env:TEMP`, not a synced Dropbox folder.

## Case 12 - Clipboard in error

Expected behavior: even on failure, `finally` tries to write and copy `Output_Compatto.md`.
