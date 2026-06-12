# Web UI Linguistic Visual QA Adoption Matrix

## Scope

[F] This matrix evaluates active local web/dashboard repositories for adoption of `as-common-web-ui-linguistic-visual-qa`. Sources are read-only Git status, README/config files, and lightweight framework signals collected during step 1460.

[F] No target repository was modified, no target server was started, no private images were opened, and no production service was accessed during this inventory.

## Priority Rules

- `P1`: local web app is easy to run, low operational risk, useful immediately, and suitable for read-only QA.
- `P2`: useful target, but requires small clarifications or medium-risk guardrails.
- `P3`: potentially useful later, but preparation or context is needed.
- `HOLD`: sensitive data, login/production ambiguity, absent repo, unclear environment, or high risk.

## Adoption Matrix

| Project | Repo path | Exists | Web app type | Framework | Known local start command | Requires login | Sensitive data risk | i18n/multilingual relevance | Visual QA relevance | DOM extraction feasibility | Browser QA feasibility | Read-only pilot feasibility | Risk level | Adoption priority | Recommended next action | Notes |
|---|---|---:|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AI Release Radar | `C:\Users\alberto.ferrari\source\repos\AI_Release_Radar` | yes | Local operator dashboard with Action Center and run detail pages | FastAPI, Jinja2, static assets | `python -m radar_web.app --host 127.0.0.1 --port 8787` | no normal login found | Medium: Bridge run data, scheduler/daily-sim controls must not be clicked | High: EN/IT/FR/DE/ES UI and catalog helpers | High: dashboard, Action Center, long translated labels | High: server-rendered HTML and clear routes | High with local server or headless fallback | High for GET-only pages and no button clicks | LOW | P1 | Run `1470) AI Release Radar Regression Check` as read-only linguistic/visual QA | Best immediate target because the skill was extracted from this case and the app has documented multilingual UI. |
| ASF Blueprint Studio | `C:\Users\alberto.ferrari\source\repos\ASF_Blueprint_Studio` | yes | Local project studio/dashboard with project pages and Live AI Lab surfaces | FastAPI, Jinja2, HTMX-ready server-rendered pages | `python -m uvicorn app.main:app --reload`; fallback `--host 127.0.0.1 --port 8010` | no product login in README; human approval gates exist | Medium: provider/live-lab concepts, approval records, local workspaces | Low/unknown: mainly English baseline from observed docs | High: dashboard, forms, status, live-lab pages and labels | High for server-rendered pages | Medium-high if restricted to GET/read-only routes | Medium: avoid approval/dry-run/fake-transport actions | MEDIUM | P2 | Use as second pilot after selecting safe pages and forbidding live-lab actions | Good visual/DOM candidate, but live/provider areas require explicit no-action guardrails. |
| Mansionario Vivo | `C:\Users\alberto.ferrari\source\repos\Mansionario_Vivo` | yes | Local intranet/business web app | FastAPI, Jinja2, MySQL, session cookie | `.\.venv\Scripts\python.exe -m uvicorn app.main:app --host 127.0.0.1 --port 8000` or `run_dev.ps1` | yes: login page and bcrypt password setup | High: business/intranet data and MySQL environment | Medium: Italian business UI, local labels | High once a safe demo dataset exists | Medium: login/session blocks simple DOM scan | Low without credentials and safe demo data | Low until Alberto authorizes safe review mode | HIGH | HOLD | Manual/safe-review required before any QA run | Repo was already dirty with untracked step195 report files; do not run app or inspect business data in this step. |
| Family Photo Organizer | `C:\Users\alberto.ferrari\source\repos\Family_Photo_Organizer` | yes | Local-first photo archive demo/review app | FastAPI, Jinja2, SQLite/demo runtime when explicitly enabled | `python -m uvicorn backend.app.main:app --reload`; demo requires explicit safe runtime setup | no real auth; logical demo roles only | High: personal/family photo domain; private media must not be opened | Medium: prior UI language polish and local UI text | Medium-high for synthetic/demo UI only | Medium: local server possible with safe demo mode | Medium only with synthetic data and no real media | Low until a synthetic-only scope is authorized | HIGH | HOLD | Keep on hold unless Alberto authorizes synthetic-data-only visual QA | Do not open images, thumbnails, EXIF, archives, or filesystem media paths without explicit consent. |
| Family Photo Organizer ASF | `C:\Users\alberto.ferrari\source\repos\Family_Photo_Organizer_ASF` | no | Not available locally | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a | none | HIGH | HOLD | No action | Repository path not present during step 1460. |
| AI Software Factory | `C:\Users\alberto.ferrari\source\repos\AI_Software_Factory` | yes | Framework/runner repository, not a primary web UI app | Python tooling; README references APIs, runners and docs | No local web dashboard command found in lightweight scan | no app login signal | Medium: OpenAI/provider workflow docs and live-gated tooling | Low for this skill | Low-medium: mostly docs/runner surfaces, not UI pages | Low for current scope | Low unless a concrete dashboard is identified | Low for this skill now | MEDIUM | P3 | Revisit only if a concrete local dashboard route is selected | Better served by workflow/governance skills unless a web UI surface becomes explicit. |
| AI Software Factory 2 | `C:\Users\alberto.ferrari\source\repos\AI_Software_Factory_2` | yes | Ambiguous clone/variant; README appears dashboard/radar-like | Python project | `python -m radar_web.app --host 127.0.0.1 --port 8787` appears in README, but repo identity is ambiguous | no normal login found | Medium: ambiguity and scheduler/radar wording | High if it is intentionally an AI Release Radar clone | Medium | Medium | Medium | Low until identity is clarified | MEDIUM | HOLD | Clarify repository purpose before adoption | Included only because the repo name appeared in the quick candidate-name scan; do not pilot before Alberto confirms its role. |

## Summary

- [F] `AI_Release_Radar` is the recommended P1 because it is documented, local, multilingual, and already has known read-only routes.
- [F] `ASF_Blueprint_Studio` is P2 because it is a local FastAPI/Jinja app but includes live/provider-lab concepts that require strict no-action rules.
- [F] `Mansionario_Vivo` and `Family_Photo_Organizer` are HOLD because they involve login, business data, family media, or private-data risks.
- [F] `AI_Software_Factory` is P3 because the lightweight scan did not identify it as an active web UI target for this skill.
- [F] `Family_Photo_Organizer_ASF` is HOLD because the repository path was absent.
- [INT] `AI_Software_Factory_2` should remain HOLD until Alberto clarifies whether it is a duplicate, archive, or active dashboard repo.
