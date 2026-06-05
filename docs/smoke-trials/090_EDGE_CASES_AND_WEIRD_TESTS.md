# 090 Edge Cases And Weird Tests

This file documents borderline and historical cases that should not be hidden by happy-path validation.

| Case | Input / condition | Expected behavior | Blocking? | Skill involved |
| ---- | ----------------- | ----------------- | --------- | -------------- |
| 1 | Description long but under validator limit. | Accepted. | No | Skill authoring / validator |
| 2 | Skill without `examples/` in temp sandbox. | Validator table/score shows examples absent. | No by current policy | Validator |
| 3 | Skill with underscore in temp sandbox. | Validator error and non-zero exit. | Yes | Validator |
| 4 | Backup `.bak.md` in active skill. | Warning for backup/temp file. | Warning unless fail-on-warning | Validator |
| 5 | `_archive/` contains invalid skill. | Ignored by validator. | No | Validator |
| 6 | File contains word `token` in safety policy. | Warning, not automatic error. | No unless policy says fail on warnings | Validator |
| 7 | Git status path contains spaces. | Porcelain parser preserves path. | Depends | PowerShell command pack |
| 8 | Git porcelain rename row. | Parser checks both old and new paths. | Depends | PowerShell command pack |
| 9 | File outside `$allowedPaths`. | Block before staging/commit. | Yes | PowerShell command pack |
| 10 | `gh pr checks` exit code 8 pending. | Controlled warning if output confirms pending and local gates pass. | No by itself | PowerShell/Git safe flow |
| 11 | CRLF/LF warning with exit code 0. | GO_WITH_WARNINGS. | No | Verification gate |
| 12 | `fatal: not a git repository` after output function. | Prevented by `Set-Location -Path $RepoRoot`. | Yes if it occurs | PowerShell command pack |
| 13 | DOCX lock simulated. | Warning; Markdown output continues. | No | PowerShell command pack |
| 14 | `reset --hard` requested without backup branch. | Block until backup branch is created or user explicitly changes scope. | Yes | PowerShell/Git safe flow |
| 15 | Codex report declares success but tests failed. | NO_GO_BLOCKER. | Yes | Report intake / verification gate |
| 16 | Codex report has no next step. | Ask for correction or add next-step recommendation. | Fixable | Report intake |
| 17 | Prompt authorizes commit but not push. | Commit may be allowed; push remains blocked. | Push blocks | Report intake |
| 18 | Prompt forbids commit but report says commit done. | NO_GO_BLOCKER and recovery review. | Yes | Report intake |
| 19 | Clipboard failure simulated. | Warning; artifact still written. | No | PowerShell command pack |
| 20 | Dropbox path with spaces and apostrophes. | Use quoted/literal paths and avoid temp DOCX in synced folders. | Depends | PowerShell command pack |

## Notes

- Current validator policy does not treat missing `examples/` as an error or warning; it is visible through score/table fields.
- Sensitive-word findings are warnings because safety documentation may intentionally mention unsafe terms.
- All destructive or publication-like tests must be simulated or run in a temporary sandbox.
