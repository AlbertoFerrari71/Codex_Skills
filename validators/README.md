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
- installed skills sync check;
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
python validators\installed_skills_sync_check.py --root .
python -m unittest discover -s validators -p "test_*.py"
python validators\smoke_trial_cases.py
python validators\release_workflow_check.py
git --no-pager diff --check
```

## Installed skills sync check

`validators/installed_skills_sync_check.py` diagnostica lo stato installato
delle skill quando la repository coincide con `C:\Users\alberto.ferrari\.agents\skills`
o quando viene copiata in un'altra posizione.

Il controllo e' read-only e non installa, copia, cancella o modifica file. In
particolare verifica:

- root e posizione rispetto a `.agents\skills`;
- skill attive `as-common-*` con `SKILL.md`;
- coerenza `name:` del frontmatter;
- presenza in `SKILLS_INDEX.md` e `SKILL_SCORE.md`;
- tracking Git di `SKILL.md` e file locali untracked/ignored;
- backup/temp file dentro skill attive;
- policy `_archive/backup-skills/`, trattata come area inattiva;
- file `.env` e nomi locali a rischio.

Errori bloccanti includono skill attive non tracciate, `SKILL.md` non tracciato,
`name:` diverso dalla cartella, mismatch nei cataloghi e backup/temp dentro una
skill attiva. Warning non bloccanti includono cache/ignored file e file locali
non tracciati fuori dalle skill attive quando non sono pericolosi.

Fuori da `.agents\skills`, come in GitHub Actions, il controllo segnala solo
informazione e non fallisce per la posizione della root.

## Aggiornare file generati

Aggiorna indice e score solo quando vuoi rigenerare gli artefatti tracciati:

```powershell
python validators\check_agent_skills.py --root . --write-index --write-score
```

Prima di rigenerare, rimuovere o archiviare eventuali backup locali se non
devono comparire in `SKILLS_INDEX.md`.

Se il catalog freshness fallisce, rigenerare gli artefatti con il comando sopra
e rieseguire `python validators\repo_health_check.py`.

## Scoring v2

`SKILL_SCORE.md` separa due dimensioni:

- `StructureScore`: misura igiene della cartella skill, frontmatter,
  coerenza `name:`, description valida, sezioni operative, assenza di
  backup/temp file, link `references/`/`examples/` dichiarati e warning/errori;
- `OperationalQualityScore`: misura in modo euristico trigger chiaro,
  description specifica, anti-trigger, output contract, riferimenti o esempi
  reali, cross-reference e collisione testuale semplice con skill vicine.

Le cartelle `references/` ed `examples/` vuote non danno credito: contano solo
file reali o link dichiarati che puntano a file esistenti. Lo score operativo
non e' un classificatore semantico e non usa AI, API o embedding.

## Trigger eval deterministico

La base trigger-eval vive in:

- `validators/trigger_eval_cases.json`
- `validators/test_trigger_eval.py`

Il test verifica formato JSON, ID univoci, input non vuoti, tags presenti e
skill attese/negative esistenti. Per lanciarlo singolarmente:

```powershell
python -m unittest validators.test_trigger_eval
```

Il comando di discovery generale lo include automaticamente:

```powershell
python -m unittest discover -s validators -p "test_*.py"
```

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
