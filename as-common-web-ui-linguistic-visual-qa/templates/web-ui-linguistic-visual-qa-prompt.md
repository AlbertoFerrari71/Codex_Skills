# <STEP_ID>) Web UI Linguistic Visual QA Prompt

## Contesto

- Project: <PROJECT_NAME>
- Repo path: <REPO_PATH>
- Bridge root: <BRIDGE_ROOT>
- Base branch: <BASE_BRANCH>
- Target branch/PR: <TARGET_BRANCH_OR_PR>
- Git mode: <GIT_MODE>

## Obiettivo

Eseguire QA linguistica e visuale della web UI locale, con DOM text extraction, screenshot matrix, classificazione sospetti e decisione finale di merge readiness.

## Server locale

- Server command: <SERVER_COMMAND>
- Preferred host/port: <HOST_PORT>
- Fallback ports: <FALLBACK_PORTS>
- Base URL: <BASE_URL>

Regole server:

- avviare solo server locali necessari;
- non fermare processi non avviati dallo step;
- salvare `Server_Info.json` e `Server_Stop_Info.json`;
- non premere pulsanti operativi.

## Lingue e pagine

- Baseline language: <BASELINE_LANGUAGE>
- Target languages: <TARGET_LANGUAGES>
- Pages to check: <PAGES_TO_CHECK>
- Optional detail page: <DETAIL_PAGE>
- Technical endpoints: <TECHNICAL_ENDPOINTS>

## Termini

- Allowlist: <ALLOWLIST>
- Suspicious/forbidden terms: <SUSPICIOUS_TERMS>
- Product names not to translate: <PRODUCT_NAMES>

## Viewport

- Desktop viewport: <DESKTOP_VIEWPORT>
- Mobile viewport: <MOBILE_VIEWPORT>

## Metodo richiesto

1. Safety preflight Git/read-only.
2. Analisi i18n/template/CSS/formatter.
3. Browser walkthrough con in-app Browser se disponibile.
4. Fallback dichiarato: Chrome headless, Playwright, Selenium o HTTP DOM extraction.
5. Visible text extraction per pagina/lingua.
6. Screenshot desktop e mobile minimi.
7. Classificazione DOM suspects: difetto reale, residuo ammesso, falso positivo, falso positivo substring, endpoint tecnico, dato tecnico grezzo, testo originale/dinamico, report raw/collassato, lingua baseline.
8. Micro-fix solo se autorizzati da <GIT_MODE>.
9. Test/gate: <TEST_COMMANDS>.
10. Report Bridge finale.

## Output Bridge

Creare:

```text
<BRIDGE_ROOT>/web_smoke/<STEP_ID>_web_ui_linguistic_visual_qa_<TIMESTAMP>/
```

File minimi:

- `Visual_QA_Matrix.md`
- `DOM_Suspects.json`
- `Review_Notes.md`
- `Server_Info.json`
- `Server_Stop_Info.json`
- `visible_text_<lang>_<page>.txt`
- `<lang>_<page>.png`
- `<lang>_<page>_mobile.png`
- `Report_Codex.md`

## Vincoli

- No reset, clean, rebase, force push o `--no-verify`.
- No scheduler, email, tag, release o deploy.
- No runtime LLM calls.
- No azioni distruttive nella web app.
- No merge automatico.
- Non modificare repo target in modalita read-only.

## Report finale

Usare uno stato:

- `PASS_READY_FOR_HUMAN_MERGE`
- `PASS_WITH_MICROFIX_READY_FOR_HUMAN_MERGE`
- `PASS_PR_DRAFT`
- `PASS_LOCAL_ONLY`
- `PARTIAL_PR_NEEDS_FIX`
- `BLOCKED_GIT_STATE`
- `BLOCKED_BROWSER_QA`
- `BLOCKED_TEST_FAILURE`
- `BLOCKED_AMBIGUOUS_SCOPE`

Includere pagine/lingue, metodo browser/fallback, screenshot, visible text, finding, test, vincoli rispettati e prossimo step.