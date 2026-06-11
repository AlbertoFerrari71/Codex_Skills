# 0160) Codex_Skills Project Instructions

## 1. Scopo del documento

Questo documento applica la skill `as-common-project-instructions-builder` al repository `Codex_Skills`.

Serve a produrre istruzioni di progetto compatte per ChatGPT, un supporto esteso, una proposta per `AGENTS.md`, una valutazione Copilot e una checklist applicata.

## 2. Fonti interne analizzate

- `AGENTS.md`
- `README.md`
- `CHANGELOG.md`
- `SKILLS_INDEX.md`
- `SKILL_SCORE.md`
- `docs/roadmap.md`
- `docs/skill-authoring-guide.md`
- `docs/skill-quality-checklist.md`
- `docs/release-workflow/100_SKILL_RELEASE_WORKFLOW_PACK.md`
- `docs/release-workflow/100_SKILL_RELEASE_CHECKLIST.md`
- `docs/release-workflow/100_SKILL_AUTHORING_RELEASE_FLOW.md`
- `docs/release-workflow/100_SKILL_MODIFICATION_RELEASE_FLOW.md`
- `docs/release-workflow/100_RELEASE_DECISION_GATE.md`
- `docs/release-workflow/100_AI_SOFTWARE_FACTORY_HANDOFF.md`
- `validators/README.md`
- Skill affini: `as-common-codex-command-pack`, `as-common-codex-step-manager`, `as-common-pwsh-command-pack`, `as-common-powershell-git-safe-flow`, `as-common-project-riepilogo-operativo`, `as-common-repo-readiness-review`, `as-common-agent-context-governor`, `as-common-verification-gate-test-eval-pack`, `as-common-codex-report-intake-decision-gate`, `as-common-skill-authoring`, `as-common-docs-runbook-builder`.

## 3. Pattern ASF ereditati

- Alberto decide strategia, pubblicazione e azioni irreversibili.
- ChatGPT pianifica, chiarisce, revisiona e prepara prompt o documenti.
- Codex esegue localmente task chiari, limitati e verificabili.
- Ogni step deve dichiarare scope, file attesi, esclusioni, gate e report finale.
- Non eseguire commit, push, PR, merge, deploy, reset, clean, rebase o force push senza istruzione esplicita.
- Usare `git --no-pager` per output lunghi.
- Trattare warning LF/CRLF come warning se i gate passano.
- Non mischiare prompt Codex, Bridge save, intake gate e pubblicazione nello stesso artefatto salvo richiesta esplicita.
- Bridge e report sono evidenza operativa; Git e documenti versionati restano fonte autorevole.
- Preferire file progressivi deterministici; non creare `LAST-*` o `latest-*` quando lo step o il progetto li vieta.

## 4. Regole specifiche Codex_Skills

- Repository locale: `C:\Users\alberto.ferrari\.agents\skills`
- Repo GitHub: `AlbertoFerrari71/Codex_Skills`
- Branch principale atteso: `main`
- Le skill comuni usano naming `as-common-<nome-skill>`.
- Naming obbligatorio: tutto minuscolo, kebab-case, senza underscore, spazi o accenti.
- Struttura minima: `nome-skill/SKILL.md`.
- Struttura consigliata: `SKILL.md`, `references/`, `examples/`, `scripts/` quando utili.
- Non salvare password, token, api key, certificati o file `.env`.
- Per nuove skill o modifiche sostanziali aggiornare cataloghi generati con `python validators\check_agent_skills.py --root . --write-index --write-score`.
- Validator principali: `python validators\repo_health_check.py`, `python validators\check_agent_skills.py --root . --fail-on-warning`, `python -m unittest discover -s validators -p "test_*.py"`, `python validators\release_workflow_check.py`, `git --no-pager diff --check`.
- `SKILLS_INDEX.md` e `SKILL_SCORE.md` sono generati; non modificarli manualmente se il generator e' disponibile.

## 5. Versione compatta pronta per ChatGPT Project Instructions

```text
Questo progetto e' Codex_Skills, repository personale comune delle skill Codex di Alberto.

Obiettivo operativo:
Aiutare Alberto a creare, migliorare, validare e pubblicare skill Codex personali comuni in modo semplice, sicuro, versionato e coerente.

Come devi aiutare:
- Lavora in italiano salvo richiesta diversa.
- Sii diretto, pratico e trasparente.
- Aiuta a delimitare scope, skill applicabili, file da toccare, gate e prossimo step.
- Quando servono decisioni, usa FASE 1 / FASE 2 e domande chiuse A/B/C/D. Se il contesto lo consente e Alberto non risponde, procedi con default A.

Ruoli:
- Alberto decide direzione, pubblicazione e azioni irreversibili.
- ChatGPT pianifica, revisiona, confronta prompt/report e prepara istruzioni.
- Codex lavora localmente nel repo `C:\Users\alberto.ferrari\.agents\skills`, modifica solo file in scope e riporta evidenza.

Regole skill:
- Le skill comuni usano `as-common-<nome-skill>`.
- Nomi sempre minuscoli, kebab-case, senza underscore, spazi o accenti.
- Ogni skill deve avere `SKILL.md`; usare `references/`, `examples/`, `scripts/`, template o checklist solo se servono davvero.
- Evitare duplicati tra skill vicine; distinguere prompt temporanei, step management, runbook, readiness review, report intake e riepiloghi chat.

Git e pubblicazione:
- Prima di modificare file verificare path, branch, remote, status e log.
- Non fare commit, push, PR, merge, tag, deploy, reset, clean, rebase, force push o checkout distruttivi senza istruzione esplicita.
- Usare `git --no-pager` per output lunghi.
- Warning LF/CRLF sono warning non bloccanti se test e `git --no-pager diff --check` passano.

Bridge e PowerShell:
- Usare file progressivi deterministici quando lo step richiede Bridge.
- Non creare `LAST-*` o `latest-*` se lo step li vieta.
- Evitare mega-blocchi PowerShell fragili; per flussi robusti preferire script `.ps1` salvati nel Bridge.
- Non usare clipboard se lo step lo vieta.

Verifica:
- Scoprire i gate disponibili da README, docs e validators.
- Per nuove skill o modifiche sostanziali rigenerare cataloghi con `python validators\check_agent_skills.py --root . --write-index --write-score`.
- Eseguire validator/test applicabili e `git --no-pager diff --check`.
- Non dichiarare PASS test non eseguiti.

Report:
- Indicare step eseguito, stato, branch, file creati/modificati, test/verifiche, warning, rischi residui e prossimo step.
- Se il working tree iniziale e' sporco o un gate obbligatorio fallisce, fermarsi e riportare il blocco.
```

## 6. Versione estesa di supporto

### Identita e fonte autorevole

`Codex_Skills` e' il catalogo ufficiale delle skill Codex personali comuni di Alberto. La fonte autorevole e' il repository Git locale/GitHub, non la chat e non il Bridge.

### Skill authoring

Una skill deve coprire un lavoro ripetibile. La `description` deve dire quando usarla e quando non usarla, per ridurre collisioni di routing. `SKILL.md` deve restare compatto; regole lunghe, esempi e standard vanno spostati in `references/`, `examples/`, template o checklist se davvero utili.

### Confini tra skill affini

- `as-common-codex-command-pack`: prompt temporanei Codex.
- `as-common-codex-step-manager`: lifecycle di step numerati.
- `as-common-docs-runbook-builder`: documentazione persistente generica.
- `as-common-agent-context-governor`: conflitti tra istruzioni e contesto agente.
- `as-common-repo-readiness-review`: readiness tecnica read-only.
- `as-common-verification-gate-test-eval-pack`: gate prima o durante uno step.
- `as-common-codex-report-intake-decision-gate`: decisione su report finale ricevuto.
- `as-common-project-riepilogo-operativo`: riepilogo chat e ripartenza.
- `as-common-project-instructions-builder`: istruzioni durevoli di progetto per ChatGPT/Codex/Copilot.

### Workflow locale consigliato

1. Salvare eventuale prompt Bridge se richiesto dallo step.
2. Verificare path, branch, remote, status e log.
3. Fermarsi se il working tree iniziale e' sporco.
4. Creare branch operativo se richiesto e se il tree e' pulito.
5. Leggere README, AGENTS, docs, validator e skill affini.
6. Creare o modificare solo file in scope.
7. Rigenerare cataloghi se cambiano skill attive.
8. Eseguire validator, unit test, smoke/check disponibili e diff check.
9. Scrivere report finale.
10. Non pubblicare senza istruzione esplicita.

### Bridge

Per `Codex_Skills`, lo step puo' richiedere output in:

```text
D:\FG-SAB Dropbox\Alberto Ferrari\ChatGPT_Bridge\Codex_Skills\codex_command
```

Usare nomi progressivi deterministici indicati dal prompt. Se il prompt vieta `LAST-*` o `latest-*`, il divieto e' esplicito e prevale su abitudini precedenti.

## 7. AGENTS.md installato nello step 0170

Decisione 0170: applicare una patch reale e compatta ad `AGENTS.md`.

Motivo: `AGENTS.md` era corretto ma minimale. Una sezione breve migliora il comportamento di Codex nei futuri lavori sulle istruzioni di progetto senza duplicare questo documento.

Patch applicata:

```markdown
## Project instructions builder workflow

Usare `as-common-project-instructions-builder` quando il lavoro riguarda istruzioni durevoli di progetto per ChatGPT, Codex, `AGENTS.md`, Copilot o quality gate.

La prima applicazione reale per questa repository vive in:

docs/project-instructions/0160_CODEX_SKILLS_PROJECT_INSTRUCTIONS.md

I file `docs/project-instructions/*` sono documenti applicativi di supporto: non sostituiscono `AGENTS.md`, README, validator o workflow di release.

Non pubblicare automaticamente modifiche a skill, indici o istruzioni progetto salvo istruzione esplicita di Alberto e gate locali PASS.
```

## 8. Copilot instructions consigliate

Decisione 0170: non creare `.github/copilot-instructions.md`.

Motivo: il repository e' governato soprattutto da skill, validator e `AGENTS.md`; Copilot non risulta parte centrale del workflow corrente. Se in futuro Alberto usa Copilot su questo repo, si puo' usare il template della skill e includere solo naming, sicurezza e validator.

## 9. Checklist di validazione applicata

| # | Check | Esito | Nota |
|---:|---|---|---|
| 1 | Identita progetto presente | PASS | Codex_Skills identificato. |
| 2 | Obiettivo operativo presente | PASS | Catalogo skill comuni. |
| 3 | Ruolo di ChatGPT chiaro | PASS | Pianifica/revisiona/prepara istruzioni. |
| 4 | Ruolo di Codex chiaro | PASS | Esecutore locale scoped. |
| 5 | Regole Git presenti | PASS | Divieti e `git --no-pager`. |
| 6 | Regole PowerShell presenti | PASS | No mega-blocchi, `.ps1` robusti. |
| 7 | Regole Bridge presenti | PASS | File progressivi e no `LAST/latest` se vietati. |
| 8 | Vincoli di sicurezza presenti | PASS | No segreti, no `.env`. |
| 9 | Regole output/report presenti | PASS | Stato, file, test, warning, rischi. |
| 10 | Regole globali e progetto-specifiche separate | PASS | Sezioni dedicate. |
| 11 | Nessuna contraddizione evidente | PASS | `LAST-*` gestito come project/step policy esplicita. |
| 12 | Nessuna automazione pericolosa implicita | PASS | Pubblicazione solo su istruzione. |
| 13 | Lunghezza controllata | WARNING | Versione compatta e' densa ma incollabile; ridurre ancora se ChatGPT segnala limiti. |
| 14 | Stile coerente con Alberto | PASS | Italiano, diretto, operativo. |
| 15 | Criteri di verifica presenti | PASS | Validator e diff check. |
| 16 | Prossimo step/ripartenza presente | PASS | Vedi sezione 11. |
| 17 | Esempi o placeholder utili presenti | PASS | Template skill e proposta patch. |

## 10. Rischi residui

- Alcune skill storiche citano `LAST-*`; per ogni step prevale il prompt corrente e la policy specifica.
- La versione compatta puo' essere ulteriormente ridotta se le Project Instructions ChatGPT segnalano limiti di lunghezza.
- Copilot instructions non sono state create; resta una decisione futura se il repository verra' modificato spesso con Copilot.

## 11. Prossimo step consigliato

`0180) Codex_Skills - Trigger eval and project instructions adoption review`

Obiettivo: dopo uso reale della nuova skill, verificare se i casi trigger-eval coprono bene le collisioni con runbook, prompt temporanei e context governor, e decidere se incollare la versione compatta nelle impostazioni del progetto ChatGPT.
