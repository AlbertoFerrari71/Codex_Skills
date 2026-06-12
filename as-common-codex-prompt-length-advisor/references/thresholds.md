# Thresholds

Le soglie sono euristiche operative per qualita', leggibilita' e rischio di
errore umano. Non sono limiti tecnici garantiti dei modelli o di Codex.

| Caratteri | Status | Interpretazione |
|---:|---|---|
| 0-30.000 | `OK` | Prompt unico consigliato. |
| 30.001-45.000 | `OK_GRANDE` | Prompt unico ancora accettabile, con warning leggero. |
| 45.001-70.000 | `REVIEW` | Conviene ridurre boilerplate, duplicazioni, log e storia non utile. |
| 70.001-100.000 | `SPLIT_CONSIGLIATO` | Proporre split leggero, senza imporlo. |
| oltre 100.000 | `SPLIT_FORTE` | Prompt unico sconsigliato salvo casi eccezionali. |

Default Alberto: mantenere il prompt monolitico quando e' leggibile, completo e
sotto soglia ragionevole. Mega-Step significa milestone grande, non
Mega-Prompt obbligatorio.

Esempi:

- 28k caratteri con sentinella, regole finali e output limitato: prompt unico.
- 38k caratteri con poco rumore: prompt unico con warning.
- 55k caratteri con report vecchi e log estesi: alleggerire prima dell'uso.
- 85k caratteri con storia lunga: spostare storico e riferimenti in file di
  supporto.
- 120k caratteri: usare prompt index + task file, salvo motivazione esplicita.
