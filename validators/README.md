# Validators

Controlli locali per il catalogo Codex_Skills. Tutti i comandi usano solo la
standard library Python e non scrivono file, salvo quando indicato.

## Health check rapido

Da root repository:

```powershell
python validators\repo_health_check.py
```

Il comando esegue:

- validazione catalogo skill in modalita severa;
- controllo catalog freshness di `SKILLS_INDEX.md` e `SKILL_SCORE.md`;
- unit test dei validator;
- smoke trial temporanei;
- controllo wiring del release workflow;
- `git --no-pager diff --check`;
- report EOL con `git ls-files --eol`.

Il report EOL e' non bloccante: segnala anomalie preesistenti come `w/mixed`
senza fallire il gate se tutti i controlli bloccanti passano.

## Comandi singoli

```powershell
python validators\check_agent_skills.py --root .
python validators\check_agent_skills.py --root . --fail-on-warning
python validators\check_agent_skills.py --root . --fail-on-warning --check-catalog-freshness
python -m unittest discover -s validators -p "test_*.py"
python validators\smoke_trial_cases.py
python validators\release_workflow_check.py
git --no-pager diff --check
```

## Aggiornare file generati

Aggiorna indice e score solo quando vuoi rigenerare gli artefatti tracciati:

```powershell
python validators\check_agent_skills.py --root . --write-index --write-score
```

Prima di rigenerare, rimuovere o archiviare eventuali backup locali se non
devono comparire in `SKILLS_INDEX.md`.

Se il catalog freshness fallisce, rigenerare gli artefatti con il comando sopra
e rieseguire `python validators\repo_health_check.py`.

## Sensitive values scan

Il validator intercetta valori sensibili verosimili in:

- cartelle skill attive `as-common-*` e `as-*`;
- `docs/`;
- `templates/`;
- file root principali (`README.md`, `AGENTS.md`, `CHANGELOG.md`, `SKILLS_INDEX.md`, `SKILL_SCORE.md`, `.gitattributes`, `.gitignore`);
- `.github/workflows/*.yml` e `.github/workflows/*.yaml`.

Sono accettati placeholder espliciti come `<UID_PLACEHOLDER>`,
`<PWD_PLACEHOLDER>`, `<OPENAI_API_KEY>`, `your-api-key-here`, `REDACTED` e
`***`. La parola tecnica `secret` non genera warning da sola.

Policy `_archive/`: escluso dallo scan bloccante per conservare backup storici
senza bloccare la pubblicazione del catalogo attivo.

## Link-check references/examples

Nei file `SKILL.md`, le sezioni `References`, `Examples`, `Riferimenti` ed
`Esempi` possono dichiarare link o path verso `references/...` ed
`examples/...`. I file dichiarati mancanti sono errori bloccanti. Skill senza
references/examples restano valide.

## GitHub Action

La workflow `.github/workflows/validate-skills.yml` usa `ubuntu-latest` ed
esegue validator severo, unit test e health-check su pull request, push su
`main` e avvio manuale.
