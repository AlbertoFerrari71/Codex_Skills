# CHANGELOG

## 040) Skill Quality Cleanup

Pulizia e uniformazione dopo la fondazione del catalogo skill.

- archiviati i backup `.bak.md` tracciati in `_archive/backup-skills/`;
- aggiunta documentazione `_archive/README.md`;
- aggiornata `.gitignore` per evitare futuri backup temporanei;
- aggiunta review warning in `docs/skill-warning-review.md`;
- migliorate `as-common-codex-command-pack` e `as-common-vba-excel-access-alberto` con `references/` ed `examples/`;
- sostituiti esempi sensibili con placeholder o termini equivalenti;
- aggiornato il validator per ignorare esplicitamente `_archive/`;
- rigenerati `SKILLS_INDEX.md` e `SKILL_SCORE.md`.

## 030) Skill Catalog & Validator Foundation

Creazione della base di catalogazione e validazione delle skill Codex.

- aggiunto validator principale `validators/check_agent_skills.py`;
- aggiunti test standard library `validators/test_check_agent_skills.py`;
- aggiunta generazione automatica di `SKILLS_INDEX.md`;
- aggiunta generazione automatica di `SKILL_SCORE.md`;
- aggiornata documentazione qualità e authoring skill;
- mantenuta la rilevazione dei file backup senza cancellarli.

## 010

Creazione Governance Pack iniziale.

- README
- AGENTS
- docs
- templates
- validators
- gitignore
- gitattributes

