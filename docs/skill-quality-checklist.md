# Skill Quality Checklist

Checklist minima per mantenere pulite e tracciabili le skill Codex personali/comuni.

## Naming

- Usare solo lettere minuscole, numeri e trattini.
- Usare kebab-case.
- Non usare underscore.
- Non usare spazi.
- Non usare accenti o caratteri non ASCII.
- Mantenere identici nome cartella e campo `name:` nel frontmatter.

Esempio valido:

```text
as-common-codex-command-pack
```

## Frontmatter obbligatorio

Ogni skill deve iniziare con frontmatter delimitato da `---`:

```markdown
---
name: as-common-nome-skill
description: Usa questa skill quando ...
---
```

Campi obbligatori:

- `name:`
- `description:`

## Description efficace

La `description` deve spiegare quando usare la skill in modo chiaro e operativo.

Indicazioni:

- evitare descrizioni vuote o troppo brevi;
- restare sotto circa 500 caratteri;
- nominare il contesto pratico in cui la skill va attivata;
- evitare formule generiche come "skill utile".

## Body operativo

Il corpo di `SKILL.md` dovrebbe contenere almeno una sezione operativa, per esempio:

- `# Scopo`
- `# Quando usarla`
- `# Procedura`
- `# Metodo`
- `# Regole`
- `# Output atteso`

## References ed examples

Cartelle consigliate:

```text
nome-skill/
  SKILL.md
  references/
  examples/
```

Usare `references/` per standard, template lunghi o documenti di supporto.
Usare `examples/` per esempi pratici e casi di utilizzo ripetibili.

## File da evitare

Non lasciare nelle skill:

- `*.bak.md`
- `*.backup.md`
- `*~`
- `*.tmp`
- `.env`
- `*.pem`
- `*.key`
- `*.pfx`
- `secrets*`
- `token*`
- `credentials*`

I file backup non vanno cancellati automaticamente dal validator: vanno valutati e rimossi o archiviati in uno step dedicato.
Per backup storici temporanei usare `_archive/backup-skills/`, mantenendoli fuori dalle skill operative.

## Warning su segreti

Il validator segnala parole sospette nei file testuali, per esempio:

- `password`
- `token`
- `api_key`
- `secret`
- `client_secret`
- `private_key`
- `PWD=`
- `UID=`
- `connection string`

Questi warning non sono errori automatici, perché una skill può citare questi termini per spiegare cosa non fare.
Ogni segnalazione va comunque verificata manualmente.

## Come eseguire il validator

Da root repository:

```powershell
Clear-Host
python validators/check_agent_skills.py
python validators/check_agent_skills.py --write-index --write-score
python validators/check_agent_skills.py --fail-on-warning
python validators/test_check_agent_skills.py
# terminatore copia-incolla

```

## Regola verifica

Non dichiarare mai un test superato se non e' stato eseguito. Se una verifica non e' applicabile o non puo' essere eseguita, indicarla come non eseguita con motivo.

## PowerShell paste termination

Ogni blocco PowerShell operativo destinato al copia/incolla deve iniziare con `Clear-Host` e terminare con `# terminatore copia-incolla` seguito da una riga vuota finale reale. Usare questo come default anche per blocchi da una sola riga. Non usare `WScript.Shell`, `SendKeys`, auto-Enter o righe fake come workaround automatici. Per flussi lunghi o critici, preferire un file `.ps1` eseguito con `pwsh -NoProfile -ExecutionPolicy Bypass -File`.

## PowerShell command pack hardening

I command pack PowerShell non banali devono seguire lo standard `as-common-pwsh-command-pack/references/pwsh-command-pack-hardening-standard.md`.

## Release workflow

Prima di pubblicare nuove skill o modifiche sostanziali, usare `docs/release-workflow/100_SKILL_RELEASE_WORKFLOW_PACK.md`.

