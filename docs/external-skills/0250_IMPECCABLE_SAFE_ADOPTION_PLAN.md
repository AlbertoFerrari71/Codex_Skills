# 0250 Impeccable Safe Adoption Plan

Data: 2026-06-12

Step: 0250) Codex Skills - Impeccable Design Skill Evaluation and Safe Adoption Plan

## Decisione

Default consigliato: **Opzione A - creare in futuro una skill wrapper nostra, leggera e conforme ad `as-common-*`, ispirata alle parti utili di Impeccable**.

Nome consigliato: `as-common-web-ui-design-review`.

Non installare Impeccable direttamente nel repository `C:\Users\alberto.ferrari\.agents\skills`. Non creare `.agents/skills/impeccable` nel catalogo personale. Non usare `npx impeccable skills install` dalla root del catalogo.

## Confronto opzioni

| Opzione | Descrizione | Benefici | Rischi | Decisione |
|---|---|---|---|---|
| A | Skill wrapper nostra `as-common-web-ui-design-review` | Naming conforme, scope controllato, integra governance Alberto, nessuna dipendenza obbligatoria | Richiede uno step futuro di authoring e test | **Consigliata** |
| B | Usare Impeccable come tool esterno nei singoli progetti web | Massimo accesso a detector/Live Mode/CLI ufficiale | Node/npm, install/update, file generati, drift provider | Ammissibile solo in pilot isolato |
| C | Fork/vendor controllato | Controllo versione e patch | Manutenzione alta, licenza/NOTICE, build complessa, provider churn | Non consigliata ora |
| D | Non adottare per ora | Zero rischio operativo | Perde un metodo utile di review UI | Troppo conservativa se pilot documentato |

## Piano pilot sicuro

Fase 1 - Skill wrapper documentale:

1. Creare `as-common-web-ui-design-review` come skill instruction-only.
2. Trigger stretto: review UI/web frontend, dashboard, landing, componenti, screenshot, responsive, accessibility, microcopy.
3. Anti-trigger espliciti: project instructions, AGENTS.md, repo readiness, prompt pack, backend-only, test gate generici.
4. Includere un processo in 5 passaggi:
   - ricostruire target, utenti e job-to-be-done;
   - leggere design context disponibile (`README`, componenti, CSS, eventuale `PRODUCT.md`/`DESIGN.md`);
   - eseguire review UI con categorie fisse;
   - usare browser/screenshot/detector solo se disponibili e autorizzati;
   - produrre report P0-P3 con fix suggeriti e test da fare.
5. Non includere codice Impeccable e non copiare integralmente reference esterne.

Fase 2 - Pilot in un progetto web non critico:

1. Scegliere una branch dedicata in un progetto web locale.
2. Eseguire solo review/screenshot, senza Live Mode e senza auto-polish.
3. Se si prova il CLI, usare solo `npx impeccable detect <target>` o una installazione project-local esplicitamente autorizzata.
4. Registrare file generati e diff.
5. Passare da decision gate prima di ogni adozione stabile.

Fase 3 - Eventuale tool esterno opzionale:

1. Documentare prerequisiti Node.
2. Pin di versione npm o commit.
3. `IMPECCABLE_NO_UPDATE_CHECK=1` per workflow supervisionati.
4. Nessun install user-wide.
5. Nessun update automatico.

## Cosa NON fare

| Divieto | Motivo |
|---|---|
| Non eseguire `npx impeccable skills install` in `Codex_Skills` | Creerebbe una skill `impeccable` non conforme e potenzialmente modifica provider folders. |
| Non installare user-wide in `~/.agents/skills` per questo catalogo | Contamina il catalogo attivo e puo' cambiare routing Codex. |
| Non copiare il sorgente Impeccable nella repo | Rischio licenza/manutenzione e prompt troppo ampio. |
| Non creare fork/vendor subito | Costoso, fragile, richiede build/test esterni. |
| Non usare Live Mode su progetti importanti senza branch e backup | Live Mode scrive varianti in source. |
| Non confondere `PRODUCT.md` con `AGENTS.md` | `PRODUCT.md` e' contesto prodotto/design, non istruzione agente globale. |
| Non trasformare detector estetico in gate assoluto | Alcune regole possono essere false positive o dipendere dal brand. |
| Non usare "bello" come criterio sufficiente | UI deve servire task, accessibilita', responsivita' e dati reali. |

## Gate prima di qualsiasi integrazione

| Gate | PASS | FAIL |
|---|---|---|
| Naming | Skill futura usa `as-common-web-ui-design-review` o nome `as-common-*` equivalente | Nome `impeccable` o non conforme. |
| Scope | Trigger limitato a UI/web design review | Trigger generico su "design", "frontend", "review" senza limiti. |
| Dipendenze | Wrapper senza dipendenze obbligatorie | Richiede Node/npm per attivarsi sempre. |
| Sicurezza | Nessun install/update automatico | Esegue `skills install/update` senza consenso. |
| Separazione docs | `PRODUCT.md`/`DESIGN.md` trattati come design context | Sovrascrive AGENTS/README/project instructions. |
| Git | Branch/status/diff/test controllati | Modifiche dirette senza preflight. |
| Browser | Browser/live mode opzionale e fallibile | Blocco se browser non disponibile. |
| Privacy | Update check disattivabile o dichiarato | Network non dichiarato in ambienti riservati. |
| Report | P0-P3, fatti/ipotesi/raccomandazioni separati | Feedback estetico generico non verificabile. |

## Criteri PASS/FAIL per pilot

PASS:

- La skill wrapper produce review utile senza installare Impeccable.
- Nessuna skill operativa esterna viene creata nel catalogo personale.
- Il report distingue design critique, audit tecnico UI e project instructions.
- Il workflow funziona anche senza browser/live mode.
- Quando il detector esterno e' usato, il comando e' esplicito, read-only e versionato.
- Le raccomandazioni sono ordinate P0-P3 e collegate a fix verificabili.

FAIL:

- Il pilot richiede install globale o user-wide.
- Il wrapper duplica l'intero prompt Impeccable o diventa una mega-skill generica.
- I file `PRODUCT.md`/`DESIGN.md` sovrascrivono documentazione progetto senza conferma.
- Live Mode scrive source non reviewato.
- I gate Git/test/diff vengono saltati.
- La review premia solo estetica e ignora utenti, task, accessibilita' o responsive.

## Scope futura skill `as-common-web-ui-design-review`

La skill futura dovrebbe coprire:

- audit UI;
- visual QA;
- anti-AI-slop;
- design consistency;
- accessibilita';
- responsive;
- microcopy;
- project context tramite `PRODUCT.md`/`DESIGN.md` quando presenti;
- screenshot review;
- browser/live review solo se sicura e disponibile;
- report P0-P3 con next action;
- distinzione tra brand surface e product UI;
- segnalazione quando serve designer umano o identita' visiva professionale.

La skill futura non dovrebbe:

- sostituire `as-common-project-instructions-builder`;
- sostituire `as-common-verification-gate-test-eval-pack`;
- installare tool esterni;
- vendorizzare Impeccable;
- promettere che un detector estetico basti a certificare UX reale;
- agire su backend-only o repo readiness generica.

## Primo workflow consigliato della futura skill

1. Preflight:
   - identificare progetto, target UI, branch, stato Git;
   - capire se lavoro e' review-only o fix autorizzato.
2. Context:
   - leggere `README`, componenti/CSS principali, eventuali `PRODUCT.md`/`DESIGN.md`;
   - se mancano, inferire solo ipotesi e dichiararle.
3. Evidence:
   - source review;
   - screenshot o browser se disponibili;
   - detector opzionale solo se installato/autorizzato.
4. Review:
   - gerarchia e layout;
   - accessibilita';
   - responsive;
   - stato dati/empty/error/loading;
   - microcopy;
   - slop/monoculture;
   - coerenza con identita' e utenti.
5. Report:
   - score non assoluto;
   - P0-P3;
   - fix suggeriti;
   - comandi/test;
   - rischi residui;
   - next step singolo.

## Gestione Impeccable come tool esterno

Uso ammesso solo in futuro e solo se richiesto:

```powershell
$env:IMPECCABLE_NO_UPDATE_CHECK = "1"
npx impeccable detect src --json
```

Note:

- Eseguire da repo web target, non da `Codex_Skills`.
- Preferire target ristretto (`src/components`, route, file) invece di root enorme.
- Non eseguire `npx impeccable skills install/update/link` senza prompt dedicato.
- Non avviare Live Mode senza branch, dev server noto e stop method.

## Proposta prossimo step

0260) Codex Skills - Web UI Design Review Skill Wrapper Pilot

Obiettivo: creare e validare una nuova skill `as-common-web-ui-design-review` instruction-only, con trigger stretto e senza installare Impeccable.
