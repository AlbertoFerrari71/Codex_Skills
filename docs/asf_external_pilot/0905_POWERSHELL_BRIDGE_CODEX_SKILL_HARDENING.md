# 0905 PowerShell Bridge Codex Skill Hardening

Status:
- local-only Codex_Skills hardening
- no commit
- no push
- no PR
- no merge
- no deploy
- no tag

Purpose:
Integrate the ASF STEP 0900 recovery lessons into Alberto's reusable operational skills before the future 0910A controlled push.

Rules integrated:
- Bridge Dropbox retrieval must prefer the numbered/progressive file before `LAST-*`.
- `LAST-*` is a convenience fallback and must be checked for step, name, and timestamp/server_modified coherence.
- Critical Git diagnostics must use direct visible commands and save output plus exit code.
- Pasted PowerShell blocks must avoid long Markdown here-strings.
- `git diff --cached --check` blocks Phase B/publication until fixed.
- EOF blank-line recovery must be scoped to files reported by Git, with backup and selective restaging.
- If Bridge is unavailable, request only the smallest useful report section.

Next:
0910A) Codex_Skills Controlled Push Execution, only after explicit Alberto approval.
