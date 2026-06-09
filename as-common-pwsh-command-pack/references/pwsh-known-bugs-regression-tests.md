# PowerShell Known Bugs Regression Tests

Use these historical cases as a regression checklist for non-trivial command packs.

| Case | Historical bug | Regression test |
|---|---|---|
| STEP 490 demo trial | Demo flow passed too easily and did not reproduce real command-pack failures. | Run a demo that includes failure, warning, generated artifacts, and final status. |
| False success output | A success message was printed even after a failure path. | Require `$StepOk` and print completion only when it is true. |
| Separatable `if/else` blocks | Paste could split related PowerShell blocks. | Use a single wrapper `& { ... }` or a real `.ps1` payload. |
| Encoding mismatch | `utf8NoBOM` writer was not portable enough. | Use `.NET` UTF-8 without BOM helpers. |
| Git status parsing | Parsing trimmed `git status --short` incorrectly. | Use `git status --porcelain=v1` and parse status/path separately. |
| DOCX lock in Dropbox | Temporary DOCX work happened in a synced folder. | Use `$env:TEMP` or system temp for DOCX temp folders. |
| Lost repo location | Output function left the session outside the repository. | `Write-CompactOutput` must call `Set-Location -Path $RepoRoot`. |
| Pending PR checks | `gh pr checks` pending state returned exit code 8. | Treat exit code 8 as controlled only when local gates pass and output confirms pending state. |
| LF/CRLF warnings | Line-ending warnings were confused with gate failure. | Treat as non-blocking only when diff-check exit code is 0. |
| Paste termination | Final newline loss left a useful command waiting. | Apply step 080 fake-line rule or prefer a real `.ps1` file. |
| STEP 0900 stale LAST | Bridge was readable but `LAST-*` could be older than the progressive output. | Retrieve the numbered/progressive file first; use `LAST-*` only after checking step, filename, and timestamp/server_modified. |
| STEP 0900 Git wrapper usage | A generic PowerShell wrapper passed Git arguments incorrectly and returned only Git usage. | For failed diagnostics, run direct visible commands and capture output plus `$LASTEXITCODE` immediately. |
| STEP 0900 Markdown here-string | A pasted Markdown here-string remained open at the PowerShell `>>` prompt. | Use line arrays for generated Markdown reports; allow here-strings only for short controlled text without triple backticks. |
| STEP 0900 cached diff EOF | Phase B stopped on `git diff --cached --check` with `new blank line at EOF`. | Stop publication, fix only files named by Git, back them up, restage only those files, then rerun cached and unstaged diff checks. |
