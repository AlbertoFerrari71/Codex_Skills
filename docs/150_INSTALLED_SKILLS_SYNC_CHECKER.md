# 150 - Installed Skills Sync Checker

## Obiettivo

Aggiungere un controllo read-only che diagnostica la coerenza tra skill
installate, repository Git, cataloghi generati e file locali presenti nella
cartella `.agents\skills`.

Lo scopo e' segnalare problemi, non correggerli automaticamente.

## Comando principale

Da root repository:

```powershell
python validators\installed_skills_sync_check.py --root .
```

Exit code:

- `0`: `PASS` oppure `PASS WITH NON-BLOCKING WARNINGS`;
- `1`: `FAIL` per problemi bloccanti;
- `2`: errore uso, argomenti o root non valida.

## Cosa controlla

- Root risolta e presenza dentro `.agents\skills`.
- Branch e HEAD Git quando disponibili.
- Skill attive `as-common-*` con `SKILL.md`.
- Coerenza `name:` nel frontmatter.
- Presenza in `SKILLS_INDEX.md` e `SKILL_SCORE.md`.
- Tracking Git di `SKILL.md` e presenza di file untracked/ignored.
- Backup/temp file dentro skill attive.
- File locali a rischio, inclusi `.env` e nomi con `secret`, `token`,
  `credential` o `password`.
- Catalog freshness riusando la logica di `check_agent_skills.py`.

## Policy `_archive`

`_archive/` non e' considerata una skill attiva. I backup in
`_archive/backup-skills/` sono riportati come informazione e non bloccano il
gate.

## Errori bloccanti

- Skill attiva senza file tracciati Git.
- `SKILL.md` non tracciato.
- `name:` mancante o diverso dalla cartella.
- Skill attiva mancante da `SKILLS_INDEX.md` o `SKILL_SCORE.md`.
- Skill nei cataloghi ma inesistente su disco.
- Cataloghi stale.
- Backup/temp file dentro skill attiva.
- File `.env` nel repository.

## Warning non bloccanti

- File ignored dentro skill attive quando sono cache/temp.
- File locali non tracciati fuori skill attive e non pericolosi.
- Cartelle `as-common-*` vuote o inattive senza `SKILL.md`.
- Nomi file con termini sensibili da verificare manualmente.

## Limiti

Il controllo non installa skill, non copia file, non cancella file e non fa
commit. Non raccoglie telemetria, non registra quali skill vengono usate e non
introduce routing AI, API o embedding.

In CI la root non sara' dentro `.agents\skills`: questo e' solo informativo e
non fa fallire il controllo.
