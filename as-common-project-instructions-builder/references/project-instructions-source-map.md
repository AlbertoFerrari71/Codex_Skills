# Project Instructions Source Map

Usa questa mappa quando devi decidere quali informazioni trasformare in istruzioni permanenti.

## Gerarchia pratica

1. Istruzioni di sistema e developer: non copiarle nei file progetto; rispettarle durante il lavoro.
2. Istruzioni globali di Alberto: includerle solo se aiutano il progetto specifico.
3. `AGENTS.md` del repository: fonte principale per Codex e agenti locali.
4. README, roadmap, changelog, decisioni e workflow: fonti versionate per contesto, stato e regole.
5. Bridge e report di step: evidenza operativa, non fonte permanente salvo decisione trasferita in docs.
6. Chat e memoria storica: utili per orientarsi, ma da verificare contro i file correnti.

## Cosa includere

- Obiettivo operativo del progetto.
- Ruoli di ChatGPT, Codex e Alberto.
- Vincoli non negoziabili.
- Branch e workflow Git se stabili.
- Comandi di test e verifica se verificati.
- Regole di sicurezza su dati, segreti, originali, deploy o sistemi esterni.
- Output finale e report richiesti.
- Prossimo step o regola di ripartenza.

## Cosa escludere

- Cronologia lunga di tentativi.
- Log completi.
- Output runtime.
- Dettagli di branch vecchi.
- Decisioni superate.
- Todo generici senza impatto operativo.
- Promesse di automazione non autorizzata.
- Segreti, token, password, chiavi, certificati, `.env`.

## Regola di compressione

Se una regola non cambia il comportamento dell'agente in un caso concreto, non metterla nelle istruzioni compatte. Se e' utile come contesto, spostarla nel documento esteso.
