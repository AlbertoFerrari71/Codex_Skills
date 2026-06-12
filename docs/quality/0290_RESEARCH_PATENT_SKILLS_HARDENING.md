# 0290) Research And Patent Skills Hardening

Data: 2026-06-12

Skill:

- `as-common-deep-research-industriale`
- `as-common-technical-patent-draft`

## Problemi Trovati

| Skill | Problema |
|---|---|
| as-common-deep-research-industriale | Trigger validi ma troppo ampi; anti-trigger assenti; fonti, stime, ipotesi e raccomandazioni non abbastanza contrattuali. |
| as-common-technical-patent-draft | Skill utile ma boundary legale troppo corto; claim draft, prior art, FTO e validita non abbastanza delimitati. |

## Modifiche Fatte

| Skill | Modifiche |
|---|---|
| as-common-deep-research-industriale | Rafforzati trigger su materiali, chimici/minerali, norme, fornitori, processi, brevetti come fonte tecnica, benchmark e stime tecnico-economiche. Aggiunti anti-trigger e output pratico. |
| as-common-technical-patent-draft | Rafforzati trigger per disclosure, documenti per consulente, stato dell'arte, differenze tecniche, esempi e claim draft non legale. Aggiunti anti-trigger legali espliciti. |

## Trigger Positivi Rafforzati

- Materiali industriali, coating, prodotti chimici/minerali.
- Norme tecniche, prodotti commerciali, fornitori e mercato.
- Processi produttivi, tecnologie emergenti e benchmark.
- Brevetti come fonte tecnica per ricerca industriale.
- Disclosure inventive, algoritmi, processi, varianti e figure per consulente.

## Anti-Trigger

| Skill | Anti-trigger principali |
|---|---|
| as-common-deep-research-industriale | Email, debug codice, project instructions, UI review, prompt Codex, curiosita generica, semplice riassunto senza ricerca. |
| as-common-technical-patent-draft | Parere legale definitivo, deposito brevetto, FTO definitiva, validita garantita, contraffazione, traduzione pura, email. |

## Rischi Legali/Tecnici

- Patent skill non deve sostituire consulente brevettuale.
- Claim draft e FTO sono solo materiale tecnico preparatorio.
- Deep research deve citare fonti quando tema e' aggiornabile, commerciale, normativo o di mercato.
- Brevetti possono essere fonte tecnica, ma non prova di liberta di operare.

## Limiti

- Nessuna web search reale eseguita in questo step.
- Nessuna prior art professionale eseguita.
- Nessun documento legale prodotto.

## Reference Aggiunte

| Skill | Reference |
|---|---|
| as-common-deep-research-industriale | `references/research-output-rubric.md`, `references/source-quality-and-uncertainty.md` |
| as-common-technical-patent-draft | `references/invention-disclosure-checklist.md`, `references/legal-boundary-notes.md` |

## Test Aggiunti

| Skill | Test |
|---|---|
| as-common-deep-research-industriale | `tests/test_skill_contract.py` |
| as-common-technical-patent-draft | `tests/test_skill_contract.py` |

## Esempi Real-Use

- Valutare coating industriale con fonti, rischi, fornitori e piano prove.
- Usare brevetti come fonte tecnica per materiali e varianti, senza claim legali.
- Preparare disclosure tecnica per algoritmo QR/glitter con figure e domande per consulente.
- Separare stato dell'arte, differenze tecniche e dati mancanti.
