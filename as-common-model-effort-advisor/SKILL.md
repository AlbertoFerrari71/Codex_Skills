---
name: as-common-model-effort-advisor
description: Usa questa skill quando Alberto chiede quale livello ChatGPT usare o serve un model effort check per compiti Codex, ASF, coding, ricerca, review, decision gate, merge o skill trasversali. Non usarla per cambiare modello automaticamente o per interventi ordinari senza mismatch evidente.
---

# Scopo

Suggerire il livello ChatGPT piu' adatto tra `Istantanea`, `Media`, `Alta`,
`Extra Elevata`, `Pro Standard` e `Pro Estesa`, bilanciando velocita',
consumo operativo e riduzione del rischio.

La skill non cambia il modello. Produce una raccomandazione breve e, quando
utile, segnala se conviene salire, scendere o mantenere il livello dichiarato.

# Quando usarla

Usala quando Alberto chiede esplicitamente:

- "che modello uso?"
- "che livello uso?"
- "serve Pro Estesa?"
- "posso scendere a Media?"
- "model effort check"
- "controlla se il modello e' giusto"
- "sto usando il livello corretto?"

Usala anche senza domanda esplicita solo se il mismatch e' evidente in compiti
significativi: prompt Codex complessi, Mega-step ASF/Codex, review critica,
decision gate, merge, pubblicazione, skill trasversali o rischio alto.

# Quando non usarla

Non usarla per ogni messaggio ordinario. Non usarla per cambiare
automaticamente il modello.

# Usa invece

- `as-common-codex-command-pack` per preparare il prompt Codex completo;
- `as-common-codex-step-manager` per gestire uno step numerato end-to-end;
- `as-common-codex-report-intake-decision-gate` per decidere GO/NO-GO da un report finale;
- `as-common-verification-gate-test-eval-pack` per creare test gate dettagliati;
- `as-common-skill-authoring` per creare o modificare una skill quando la domanda non riguarda il livello modello.

# Input

Richiesto:

- tipo di attivita' o richiesta corrente.

Opzionali:

- livello attualmente selezionato o dichiarato;
- presenza di Codex/ASF;
- impatto a valle;
- rischio e costo dell'errore;
- urgenza o velocita' desiderata;
- presenza di ricerca online;
- presenza di file, report o test;
- decisione di commit, push, merge o pubblicazione.

# Metodo

1. Valuta complessita' cognitiva, rischio operativo e costo dell'errore.
2. Considera lunghezza del contesto, verificabilita' del risultato e impatto a valle.
3. Aumenta il livello per coding, prompt Codex, workflow agentici, fonti online,
   gate decisionali e review adversariali.
4. Riduci il livello quando il compito e' ordinario, breve e facilmente verificabile.
5. Se il livello corrente e' dichiarato, confrontalo con il consigliato.
6. Se il livello corrente non e' verificabile, dillo senza chiedere chiarimenti inutili.
7. Consiglia il minimo livello adeguato, non il massimo disponibile.

# Matrice Alberto/ASF

| Attivita' | Livello consigliato |
|---|---|
| Chat veloce, chiarimento, riscrittura semplice | Istantanea / Media |
| Email commerciale ordinaria | Media |
| Email importante o delicata | Media / Alta |
| Calcolo tecnico semplice ma verificabile | Media / Alta |
| Ricerca online tecnica con fonti | Alta |
| Ricerca online strategica, investimento, innovazione | Pro Standard / Pro Estesa |
| Prompt Codex piccolo e modifica locale chiara | Alta |
| Prompt Codex Mega-step o milestone | Pro Estesa |
| Analisi report Codex standard PASS | Media |
| Analisi report Codex con warning o test falliti | Alta |
| Decisione merge/pubblicazione dopo report ambiguo | Pro Standard |
| Review adversariale di standard, policy, architettura | Pro Estesa |
| Creazione nuova skill comune | Alta / Pro Standard |
| Skill trasversale che cambia workflow ASF | Pro Estesa |
| Debug codice con contesto chiaro | Alta |
| Debug complesso, regressioni o test contraddittori | Pro Standard / Pro Estesa |
| Handoff/riepilogo operativo standard | Media |
| Handoff lungo con molte decisioni e ripartenza progetto | Alta |

Usa `Extra Elevata` come livello intermedio quando `Alta` sembra stretta per
contesto lungo o ragionamento tecnico, ma il costo dell'errore non giustifica
ancora `Pro Standard`.

# Regole ASF/Codex

- Mega-step ASF/Codex: `Pro Estesa`.
- Prompt Codex che guida molti file o modifiche: `Pro Estesa`.
- Prompt Codex piccolo: `Alta`.
- Report Codex PASS standard: `Media`.
- Report Codex con warning: `Alta`.
- Report Codex con merge, pubblicazione o rischio: `Pro Standard`.
- Review indipendente o adversariale: `Pro Estesa`.
- Gate strategico di Alberto: `Pro Standard` o `Pro Estesa`.
- Attivita' di routine verificabile da validator: `Media`.

# Onesta' sul livello corrente

- Non dichiarare di aver letto il model picker se non ci sono evidenze.
- Distingui sempre tra livello dichiarato dall'utente, livello noto dal contesto
  e livello corrente non verificabile.
- Non promettere cambio automatico modello.
- Non trattare `Pro Estesa` come sempre migliore per tutto.
- Indica quando un livello inferiore e' sufficiente.

# Output standard

Di default rispondi cosi':

```text
[Model Effort Check]
Consigliato: <livello>.
Motivo: <1-2 frasi>.
Cambio suggerito: <nessuno / salire / scendere / livello corrente non verificabile>.
```

Se richiesto, puoi aggiungere tabella criteri, punteggio rischio, alternative
A/B/C o motivazione estesa.

# Esempi

- Richiesta semplice: "riscrivi questa frase" -> `Istantanea` o `Media`.
- Prompt Codex Mega-step con molti file e gate -> `Pro Estesa`.
- Report Codex standard PASS recuperato dal Bridge -> `Media`.
- Report Codex con warning o test falliti -> `Alta`.
- Skill trasversale che cambia workflow ASF -> `Pro Estesa`.
- Review di merge ambiguo dopo report incompleto -> `Pro Standard`.
- Debug con stacktrace chiaro e test riproducibile -> `Alta`.
- Handoff lungo per ripartenza progetto con molte decisioni -> `Alta`.

# Controlli finali

Prima di rispondere:

- sii breve;
- non creare ansia da modello;
- consiglia il minimo livello adeguato;
- sali quando il costo dell'errore e' alto;
- scendi quando il compito e' ordinario e verificabile;
- esplicita fatti, ipotesi e limiti quando il livello corrente non e' verificabile.
