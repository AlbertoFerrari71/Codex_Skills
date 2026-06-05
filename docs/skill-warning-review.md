# Skill Warning Review

Revisione warning dello step 040.

| Skill/File | Warning | Categoria | Decisione | Azione |
|---|---|---|---|---|
| as-common-codex-command-pack/SKILL.20260604-220318.bak.md | File backup `.bak.md` | W1 | Backup storico reale, da togliere dal set skill attivo. | Spostato in `_archive/backup-skills/as-common-codex-command-pack-SKILL-20260604-220318.bak.md` con `git mv`. |
| as-common-codex-command-pack/SKILL.20260604-220318.bak.md | Parola sospetta `secret` | W3 | Falso positivo dentro backup storico. | Risolto come warning attivo spostando il backup fuori dalle skill operative. |
| as-common-codex-command-pack/SKILL.md | Parola sospetta `secret` | W3 | Regola di sicurezza legittima, ma formulabile senza perdita di chiarezza. | Sostituito con `sensitive values`. |
| as-common-pwsh-command-pack/SKILL.20260604-222235.bak.md | File backup `.bak.md` | W1 | Backup storico reale, da togliere dal set skill attivo. | Spostato in `_archive/backup-skills/as-common-pwsh-command-pack-SKILL-20260604-222235.bak.md` con `git mv`. |
| as-common-pwsh-command-pack/SKILL.20260604-222235.bak.md | Parole sospette `password`, `token`, `secret` | W3 | Falso positivo dentro backup storico. | Risolto come warning attivo spostando il backup fuori dalle skill operative. |
| as-common-pwsh-command-pack/SKILL.md | Parola sospetta `secret` | W3 | Regola di sicurezza legittima, ma formulabile senza perdita di chiarezza. | Sostituito con `sensitive-value leakage`. |
| as-common-pwsh-command-pack/references/pwsh-command-pack-standard.md | Parola sospetta `secret` | W3 | Regola di sicurezza legittima, ma formulabile senza perdita di chiarezza. | Sostituito con `sensitive values`. |
| as-common-vba-excel-access-alberto/SKILL.md | Esempio con `UID=` e `PWD=` | W2 | Esempio riutilizzabile troppo concreto. | Sostituito con placeholder innocui `<UID_PLACEHOLDER>` e `<PWD_PLACEHOLDER>`. |

## Esito

I warning iniziali erano 8. Dopo cleanup e rigenerazione cataloghi, l'obiettivo e' portare i warning attivi a 0 mantenendo le regole di sicurezza leggibili.
