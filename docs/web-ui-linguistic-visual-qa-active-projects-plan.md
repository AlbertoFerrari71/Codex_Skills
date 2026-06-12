# Web UI Linguistic Visual QA Active Projects Plan

## Adoption Strategy

[F] Step 1460 creates an adoption plan for `as-common-web-ui-linguistic-visual-qa`; it does not execute full QA on target repositories and does not apply application fixes.

[INT] Adoption should proceed from low-risk, already documented local dashboards toward more sensitive or operational systems only after Alberto provides explicit scope and safety constraints.

## Recommended Pilot Order

1. `1470) Use Web UI Linguistic Visual QA Skill on AI Release Radar Regression Check`.
2. `1480) Use Web UI Linguistic Visual QA Skill on ASF Blueprint Studio Full Review`, after selecting safe GET-only pages and explicitly forbidding live-lab actions.
3. Mansionario Vivo only after Alberto provides a safe demo/login scope and confirms no production data will be accessed.
4. Family Photo Organizer only with synthetic/demo data and explicit prohibition on opening real personal photos, thumbnails, EXIF, or archive paths.
5. AI Software Factory only if a concrete local web dashboard surface is identified.

## Safety Rules

- Check `git status -sb` and `git status --porcelain=v1` before and after every target repo inspection.
- Save screenshots, visible text, DOM suspects and reports only in Bridge or a declared temp location outside the target repo.
- Do not create branches, commits, PRs, report files, caches, screenshots or temp outputs in target repositories during read-only adoption pilots.
- Do not press operational buttons, approval controls, export controls, prompt-generation controls, daily-run controls, scheduler controls or provider/live-lab actions.
- Do not start servers unless the command is documented, local, credential-free, non-production and useful for the specific pilot.
- Prefer GET-only route coverage for first adoption runs.
- Keep API JSON, logs, raw report payloads and diagnostic data separate from visible UI label findings.

## When To Use Read-Only Mode

Use read-only mode when the goal is candidate assessment, regression evidence, merge-readiness review, or initial pilot coverage. Read-only mode is mandatory for target repos unless Alberto explicitly authorizes micro-fix scope.

## When To Ask For Consent

Ask Alberto before:

- using credentials or login-only pages;
- touching business, family, production-like or provider/live data;
- opening images, thumbnails, EXIF or filesystem media paths;
- triggering actions that write Bridge decisions, exports, dry-run results, provider envelopes or approval records;
- creating any branch/commit/PR outside Codex_Skills;
- changing scheduler, live provider, email, deploy, tag or release state.

## Avoiding Repository Contamination

- Write target-specific evidence to `D:\FG-SAB Dropbox\Alberto Ferrari\ChatGPT_Bridge\<Project>\...` or another explicit external evidence folder.
- Capture pre/post `git status --porcelain=v1` for each target repo.
- Stop if a target repo changes unexpectedly during the run and classify the step as blocked until the cause is understood.
- Do not clean, reset, stash, checkout or modify target repositories to make them look clean.
- Treat pre-existing dirty target state as external context and document it separately from skill findings.

## Handling Sensitive Projects

For Mansionario Vivo and Family Photo Organizer, the first acceptable step is not a full visual QA run. It is a consented safe-review setup that defines demo data, allowed pages, forbidden routes/actions, credentials handling, and evidence boundaries.

## Proposed Next Steps

- `1460-B) Review and Merge Skill Adoption Matrix` for this documentation pack.
- `1470) Use Web UI Linguistic Visual QA Skill on AI Release Radar Regression Check` as the first real adoption pilot.
- `1480) Use Web UI Linguistic Visual QA Skill on ASF Blueprint Studio Full Review` only after the safe page/action allowlist is explicit.

## Minimum Prompt Inputs For 1470

- Repo path: `C:\Users\alberto.ferrari\source\repos\AI_Release_Radar`.
- Server command: `python -m radar_web.app --host 127.0.0.1 --port <free-port>`.
- Pages: home, Action Center, one run detail page when a safe sample exists.
- Languages: EN baseline plus IT/FR/DE/ES.
- Forbidden actions: daily simulation trigger, decision write buttons, prompt generation, scheduler changes, exports, emails, deploys and live/runtime LLM calls.
- Evidence: Bridge folder with visible text, screenshot matrix, DOM suspects and final report.
- Git mode: read-only target repo, no target branch/commit/PR.
