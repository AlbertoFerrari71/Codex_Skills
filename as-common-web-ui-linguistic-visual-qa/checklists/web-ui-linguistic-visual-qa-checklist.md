# Web UI Linguistic Visual QA Checklist

## 0. Safety

- [ ] Repo path verificato.
- [ ] Branch e working tree verificati.
- [ ] Modalita Git dichiarata: solo report, micro-fix o PR draft.
- [ ] No reset/clean/rebase/force push/`--no-verify`.
- [ ] No scheduler, email, deploy, tag, release o runtime LLM.
- [ ] Pulsanti operativi vietati elencati.
- [ ] Cartella Bridge evidenze fuori dal repo target.

## 1. Contesto UI

- [ ] Cataloghi i18n letti.
- [ ] Template/componenti principali letti.
- [ ] Formatter enum/stati/codici identificati.
- [ ] CSS/layout responsivo controllato.
- [ ] Endpoint tecnici separati dalla UI.
- [ ] Allowlist e termini sospetti definiti.

## 2. Server

- [ ] Comando server individuato.
- [ ] Porta preferita o fallback documentata.
- [ ] PID/processo avviato dallo step registrato.
- [ ] Server non invasivo e locale.
- [ ] Stop finale limitato al server avviato dallo step.

## 3. Browser e fallback

- [ ] In-app Browser provato, se disponibile.
- [ ] Metodo effettivo dichiarato.
- [ ] Fallback reale usato se browser non disponibile.
- [ ] Visible text salvato per pagina/lingua.
- [ ] Screenshot salvati con nomi stabili.

## 4. Linguistic DOM scan

- [ ] Baseline language controllata come riferimento.
- [ ] Target languages controllate.
- [ ] Residui baseline cercati.
- [ ] Enum raw e codici stato cercati.
- [ ] Placeholder/fallback non localizzati cercati.
- [ ] Termini sospetti classificati con snippet/contesto.
- [ ] Match brevi controllati con confini parola e case sensitivity adeguata.
- [ ] Testi originali/dinamici e report raw/collassati separati dalle label UI.
- [ ] Endpoint JSON esclusi dai difetti UI.
- [ ] Falsi positivi motivati.

## 5. Visual QA

- [ ] Desktop screenshot per pagine/lingue prioritarie.
- [ ] Mobile minimo richiesto completato.
- [ ] Badge e card controllati.
- [ ] Bottoni, nav, header e filtri controllati.
- [ ] Overflow e parole tagliate controllati.
- [ ] Valori tecnici lunghi controllati.
- [ ] Layout responsive controllato.

## 6. Micro-fix, se autorizzati

- [ ] Difetti reali distinti da falsi positivi.
- [ ] Fix concentrati su cataloghi/formatter centralizzati.
- [ ] Nessun find/replace cieco.
- [ ] Nessun redesign.
- [ ] Nessuna modifica ai repo read-only.
- [ ] Test aggiornati solo se non fragili.

## 7. Gate

- [ ] Unit test eseguiti o dichiarati non disponibili.
- [ ] Validator/smoke test eseguiti o dichiarati non disponibili.
- [ ] `git diff --check` PASS, se repo modificato.
- [ ] `git diff --cached --check` PASS, se staging presente.
- [ ] Warning classificati.

## 8. Report

- [ ] `Visual_QA_Matrix.md` completo.
- [ ] `DOM_Suspects.json` valido.
- [ ] `Review_Notes.md` con finding e limiti.
- [ ] Screenshot e visible text collegati al report.
- [ ] Read-only o micro-fix confermati.
- [ ] Stato finale standard scelto.
- [ ] Decisione merge/no merge motivata.
- [ ] Prossimo step consigliato.