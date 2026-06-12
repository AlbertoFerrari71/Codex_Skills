---
name: as-common-codex-prompt-length-advisor
description: Usa questa skill quando Alberto deve valutare un prompt Codex troppo lungo, mega-prompt o prompt monolitico con rischio troncamento, END_OF_PROMPT, REGOLE FINALI, CONTROLLO INTEGRITÀ PROMPT, prompt packet, prompt da 20k/30k/45k/70k/100k caratteri, context used in Codex o crescita contesto durante il run. Non usarla per scrivere prompt generici, scegliere il modello o gestire uno step numerato end-to-end.
---

# Scopo

Valutare se un prompt Codex gia' preparato o in preparazione e' abbastanza
corto, leggibile, integro e robusto per restare un prompt unico, oppure se va
alleggerito o diviso in prompt packet e file di supporto.

Principio: il prompt Codex monolitico, visibile, copiabile e autosufficiente
resta il default quando e' ragionevole. La packetization e' un fallback.

# Quando usare questa skill

Usala quando Alberto chiede di:

- controllare un prompt Codex troppo lungo o un mega-prompt;
- valutare rischio troncamento, `END_OF_PROMPT`, `REGOLE FINALI` o
  `CONTROLLO INTEGRITÀ PROMPT`;
- decidere se un prompt da 20k, 30k, 45k, 70k o 100k caratteri puo' restare
  monolitico;
- stimare rumore, duplicazioni, log incollati o diff troppo estesi;
- valutare crescita del contesto durante un run Codex;
- decidere se usare prompt unico, prompt alleggerito o prompt index + task file.

# Quando NON usarla

Non usarla per:

- preparare da zero un prompt Codex operativo: usa
  `as-common-codex-command-pack`;
- gestire lifecycle, report e gate di uno step numerato: usa
  `as-common-codex-step-manager`;
- riconciliare istruzioni agentiche o conflitti di contesto ampi: usa
  `as-common-agent-context-governor`;
- creare istruzioni durevoli di progetto o `AGENTS.md`: usa
  `as-common-project-instructions-builder`;
- scegliere il livello ChatGPT o il reasoning effort: usa
  `as-common-model-effort-advisor`;
- progettare test, smoke, eval o stop policy: usa
  `as-common-verification-gate-test-eval-pack`;
- valutare un report finale Codex gia' prodotto: usa
  `as-common-codex-report-intake-decision-gate`.

# Input richiesti

- Il prompt Codex completo, come testo o come path a un file.
- L'obiettivo operativo del prompt, se non e' gia' chiaro.

# Input opzionali

- Soglia di tolleranza del progetto o vincoli specifici di Alberto.
- Dimensione stimata del run, numero file da leggere, comandi test previsti.
- Policy del progetto su Bridge, report, commit, push, PR, merge e deploy.

# Processo operativo

1. Verificare integrita' minima del prompt.
2. Misurare caratteri, righe, parole e token stimati.
3. Classificare la lunghezza con le soglie operative.
4. Cercare rumore, duplicazioni, diff, traceback e log estesi.
5. Valutare se il prompt induce crescita incontrollata del contesto durante il
   run Codex.
6. Controllare publish safety, distinguendo divieti da richieste positive.
7. Raccomandare l'azione piu' leggera che mantiene il workflow di Alberto.

Per una misura ripetibile usa lo script:

```powershell
python as-common-codex-prompt-length-advisor\scripts\prompt_length_advisor.py path\to\prompt.md
python as-common-codex-prompt-length-advisor\scripts\prompt_length_advisor.py path\to\prompt.md --json
type path\to\prompt.md | python as-common-codex-prompt-length-advisor\scripts\prompt_length_advisor.py --json
```

# Soglie operative

Le soglie sono euristiche di qualita', leggibilita' e rischio operativo, non
limiti tecnici garantiti dei modelli o di Codex.

| Caratteri | Status | Azione |
|---:|---|---|
| fino a 30.000 | `OK` | prompt unico consigliato |
| 30.001-45.000 | `OK_GRANDE` | prompt unico ancora accettabile, warning leggero |
| 45.001-70.000 | `REVIEW` | ridurre boilerplate, duplicazioni e log inutili |
| 70.001-100.000 | `SPLIT_CONSIGLIATO` | proporre prompt index + task file senza imporlo |
| oltre 100.000 | `SPLIT_FORTE` | prompt unico sconsigliato salvo casi eccezionali |

Vedi `references/thresholds.md` per esempi e interpretazione.

# Controlli di integrita' prompt

Verificare:

- presenza di una sentinella finale `END_OF_PROMPT_XXXX`;
- presenza di `CONTROLLO INTEGRITÀ PROMPT`;
- presenza di `REGOLE FINALI`;
- code fence Markdown chiusi;
- report finale deterministico;
- divieto esplicito di commit, push, PR, merge e deploy quando pertinente;
- assenza di finale brusco, elenco interrotto, path Windows spezzati o blocchi
  PowerShell multilinea apparentemente non chiusi.

Vedi `references/prompt_integrity_rules.md`.

# Controlli di rumore e duplicazione

Segnalare attenzione quando il prompt contiene:

- heading ripetuti o sezioni duplicate;
- paragrafi quasi identici;
- vincoli ripetuti molte volte;
- diff completi incollati;
- log pytest completi invece di sintesi;
- traceback lunghi;
- output shell estesi;
- storia non utile allo step corrente.

# Controlli di rischio crescita contesto durante run Codex

Distinguere la lunghezza del prompt iniziale dal contesto generato durante il
run. Un prompt medio puo' diventare rischioso se chiede a Codex di accumulare
letture e output senza limiti.

Segnalare rischio quando chiede di:

- leggere tutto il repository o intere directory senza filtro;
- aprire file enormi senza criteri;
- stampare output completi dei test lunghi;
- eseguire diff senza `git --no-pager`;
- fare scansioni indiscriminate;
- produrre report troppo prolissi;
- accumulare log completi nel Bridge;
- fare molte verifiche esplorative senza limiti.

Vedi `references/codex_context_growth_notes.md`.

# Publish safety

Non generare falsi allarmi per divieti come:

- non fare commit;
- non fare push;
- non aprire PR;
- non fare merge;
- non fare deploy.

Segnalare warning o fail quando compaiono richieste positive o ambigue come
`fai commit`, `pusha`, `apri PR`, `mergia`, `pubblica` o `deploya` senza una
sezione di autorizzazione esplicita e senza gate.

# Output atteso

Restituire:

- `PROMPT_LENGTH_STATUS`;
- metriche principali;
- rischio prompt iniziale;
- rischio crescita durante run;
- esito controlli integrita';
- rumore/duplicazioni;
- publish safety;
- suggerimento operativo;
- dettagli sintetici;
- raccomandazione finale.

# Raccomandazioni possibili

Usa una delle seguenti raccomandazioni, adattandola al caso:

- `Usa prompt unico.`
- `Usa prompt unico ma alleggerisci queste parti.`
- `Dividi solo le sezioni storiche in file riferimento.`
- `Dividi in prompt index + task file.`

# Non-obiettivi

La skill non deve:

- imporre sempre la packetization;
- sostituire il command pack;
- sostituire il model effort advisor;
- promettere stime token precise;
- dichiarare limiti tecnici assoluti;
- pubblicare, committare o modificare repository.

# Controlli finali

Prima di concludere:

- dichiarare che le soglie sono euristiche;
- separare rischio prompt iniziale e rischio crescita runtime;
- non confondere divieti publish con richieste publish positive;
- evitare trigger generici come "prompt", "Codex", "scrivi un prompt" o
  "fai step";
- mantenere la raccomandazione piu' leggera compatibile con integrita' e
  leggibilita'.
