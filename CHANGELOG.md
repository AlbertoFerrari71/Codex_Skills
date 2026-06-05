# CHANGELOG

## 090) Skill Smoke Trial Pack

Creazione del pacchetto di smoke trial per skill strategiche e command pack.

- smoke trial delle tre skill strategiche;
- edge cases strani;
- PowerShell command pack trial;
- report intake trial;
- validator smoke cases;
- cataloghi rigenerati.

## 085) PowerShell Command Pack Hardening Rules

Rafforzamento dello standard per command pack PowerShell/Git non banali.

- integrated 20 hardening rules;
- documented direct main push policy D3-C;
- added robust Git parsing and diff cached checks;
- added real `.ps1` payload requirement;
- added DOCX non-blocking and temp path rule;
- added clipboard-on-failure rule;
- regenerated catalog and score.

## 080) PowerShell Paste Termination Hotfix

Correzione della guida sulla terminazione dei blocchi PowerShell copiati/incollati.

- corrected PowerShell paste termination guidance;
- removed reliance on final `Write-Host ";";`;
- documented one useful command plus two fake lines rule;
- documented two or more useful commands plus one fake line rule;
- recommended `.ps1` execution for long or critical flows;
- regenerated catalog and score.

## 070) Codex Report Intake Decision Gate Skill

Creazione della terza skill strategica per verificare report finali Codex prima di decisioni GO/NO-GO.

- aggiunta skill `as-common-codex-report-intake-decision-gate`;
- creati file `references/` per intake report, diff review, decision matrix, evidence check, prompt correttivi e readiness commit/push;
- creati file `examples/` con prompt dimostrativi, sample intake e prompt correttivo NO-GO;
- aggiornata roadmap con 070 completato e prossimi step 080/090;
- rigenerati `SKILLS_INDEX.md` e `SKILL_SCORE.md`.

## 060) Verification Gate Test Eval Pack Skill

Creazione della seconda skill strategica per progettare e applicare verification gate.

- aggiunta skill `as-common-verification-gate-test-eval-pack`;
- creati file `references/` per gate, test matrix, eval, golden sample, stop policy e report finale;
- creati file `examples/` con prompt dimostrativi e sample verification gate;
- aggiornata roadmap con 060 completato e prossimo step 070;
- rigenerati `SKILLS_INDEX.md` e `SKILL_SCORE.md`.

## 050) Agent Context Governor Skill

Creazione della prima skill strategica nuova per governare il contesto operativo degli step Codex.

- aggiunta skill `as-common-agent-context-governor`;
- creati file `references/` per governance contesto, source map, AGENTS.md, conflitti e handoff;
- creati file `examples/` con prompt dimostrativi e sample review;
- aggiornata roadmap con 050 completato e prossimi step 060/070;
- rigenerati `SKILLS_INDEX.md` e `SKILL_SCORE.md`.

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

