---
name: as-common-skill-authoring
description: Usa questa skill quando Alberto vuole creare, rinominare, migliorare o organizzare skill Codex secondo il naming as-common-* e as-<project-key>-*.
---

# Scopo

Creare skill Codex pulite, piccole, versionabili e coerenti con lo schema di naming di Alberto.

# Naming standard

Usa sempre nomi:
- tutto minuscolo;
- con trattini;
- senza underscore;
- senza spazi;
- senza accenti;
- cartella = campo `name:` nel `SKILL.md`.

# Pattern

Skill comuni personali:

```text
as-common-<nome-skill>
```

Percorso:

```text
$HOME\.agents\skills
```

Skill locali di repository:

```text
as-<project-key>-<nome-skill>
```

Percorso:

```text
REPO\.agents\skills
```

# Project-key standard

- `ai-factory`
- `mansionario`
- `family-photo`
- `cdg`
- `fem-disco`
- `diamsign`
- `agglodetect`
- `sabbiarelli`
- `fergra`
- `einvoix`

# Struttura skill

Ogni skill deve avere almeno:

```text
nome-skill/
  SKILL.md
```

Opzionali:

```text
  references/
  scripts/
  assets/
```

# Regole di progettazione

1. Una skill deve coprire un solo lavoro ripetibile.
2. La `description` deve dire chiaramente quando usarla e quando non usarla.
3. Non creare skill enormi che coprono tutto.
4. Evita duplicati tra skill comuni e locali.
5. Se la skill è solo una preferenza generale breve, meglio `AGENTS.md` o memoria; se è una procedura ripetibile, meglio skill.
6. Parti instruction-only; aggiungi script solo se migliorano davvero affidabilità e ripetibilità.
7. Inserisci esempi pratici solo se aiutano a far partire correttamente la skill.

# Template base

```markdown
---
name: as-common-nome-skill
description: Usa questa skill quando ...
---

# Scopo

# Quando usarla

# Quando non usarla

# Procedura

# Formato output

# Regole importanti
```
