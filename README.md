# Codex_Skills

Repository centrale delle skill Codex di Alberto Ferrari.

Questa repository contiene:

- skill comuni
- template skill
- documentazione
- validator
- linee guida operative
- istruzioni di progetto ChatGPT/Codex e relativi template

Le skill sono utilizzate direttamente da Codex tramite:

C:\Users\alberto.ferrari\.agents\skills

## Release workflow

Per creare nuove skill, modificare skill esistenti e pubblicare aggiornamenti verificati, usare `docs/release-workflow/100_SKILL_RELEASE_WORKFLOW_PACK.md`.

Nota STEP 0905: per output nel Bridge Dropbox, le skill operative devono preferire i file progressivi step-specifici rispetto a `LAST-*`; per diagnostiche Git critiche devono usare comandi diretti e fermare la pubblicazione se `git diff --cached --check` fallisce.

## Verifica rapida

Da root repository:

```powershell
python validators\repo_health_check.py
```

Il comando esegue i controlli locali di base senza dipendenze esterne: validatore catalogo in modalita severa, catalog freshness, unit test, smoke trial, release workflow check, `git --no-pager diff --check` e report EOL non bloccante.

Include anche lo sync checker installato:

```powershell
python validators\installed_skills_sync_check.py --root .
```

Il controllo e' read-only: confronta cartelle skill attive, Git tracking,
`SKILLS_INDEX.md`, `SKILL_SCORE.md` e file locali a rischio. Non installa, non
copia, non cancella e non modifica file.

Per rigenerare gli artefatti tracciati:

```powershell
python validators\check_agent_skills.py --root . --write-index --write-score
```

`SKILL_SCORE.md` usa lo scoring v2:

- `StructureScore`: igiene, installabilita e riproducibilita della skill;
- `OperationalQualityScore`: score euristico sulla chiarezza operativa e sul rischio di collisione trigger.

Le cartelle `references/` ed `examples/` vuote non aggiungono punti cosmetici.
Per validare la base trigger-eval deterministica:

```powershell
python -m unittest validators.test_trigger_eval
```

Per eseguire solo il validator in modalita severa:

```powershell
python validators\check_agent_skills.py --root . --fail-on-warning
```

Il repository include anche la GitHub Action `Validate Codex Skills`, eseguita su pull request, push su `main` e `workflow_dispatch`.

## Trigger e description

Le description devono essere concrete e orientate a quando usare o non usare la
skill. Per le skill strategiche o Codex-facing preferire inglese tecnico
semplice; per skill personali o di dominio Alberto e' ammesso l'italiano.
Il mix e' accettabile quando aiuta a ridurre ambiguita di routing.

Per creare o aggiornare istruzioni durevoli di progetto per ChatGPT, Codex,
`AGENTS.md` o Copilot usare `as-common-project-instructions-builder`.
