---
name: as-common-powershell-git-safe-flow
description: Usa questa skill quando devi generare o verificare comandi PowerShell/Git sicuri per Alberto su Windows, inclusi branch, test, commit, push, PR, merge, log, diff e gh checks.
---

# Scopo

Produrre comandi PowerShell/Git sicuri, copiabili e adatti al modo di lavorare di Alberto su Windows.

# Quando usarla

Usala per:
- blocchi PowerShell da incollare nel terminale;
- verifiche Git;
- branch, commit, push, merge;
- controlli `pytest`, script `verify.ps1`, `git diff --check`;
- gestione `gh pr checks --watch`;
- correzioni PATH o configurazioni Windows.

# Regole PowerShell per Alberto

1. Non usare `Write-Host ";";` come garanzia tecnica di esecuzione: è solo un marker visivo.
2. Per un solo comando utile destinato al copia/incolla, usa due righe fake dopo il comando:
   ```powershell
   <comando utile>
   Write-Host "Linea fake 1 - termina il comando utile precedente"
   Write-Host "Linea fake 2 - se resta in attesa, premere Enter qui"
   ```
3. Per due o più comandi utili, aggiungi una sola riga fake finale:
   ```powershell
   <comando utile 1>
   <comando utile 2>
   Write-Host "Linea fake - se resta in attesa, premere Enter qui"
   ```
4. Per blocchi lunghi o critici, preferisci un file `.ps1` eseguito con `pwsh -NoProfile -ExecutionPolicy Bypass -File ...`.
5. Non usare `setx PATH ...` per modifiche permanenti del PATH: può troncare il PATH. Usa invece:
   ```powershell
   [Environment]::SetEnvironmentVariable("Path", $nuovoPath, "User")
   ```
6. Evita comandi distruttivi (`Remove-Item -Recurse -Force`, reset, clean, checkout forzati) senza spiegare cosa eliminano e senza conferma esplicita.
7. Se uno script `.ps1` è bloccato da Execution Policy, preferisci soluzioni trasparenti:
   - comando manuale;
   - `.cmd`/`.bat` controllabile;
   - oppure `powershell.exe -NoProfile -ExecutionPolicy Bypass -File ...` solo se serve davvero.

# Regole Git per Alberto

1. Usa sempre `git --no-pager` per output potenzialmente lunghi:
   - `git --no-pager log ...`
   - `git --no-pager diff ...`
   - `git --no-pager show ...`
2. Prima di modifiche importanti verifica:
   - `git branch --show-current`
   - `git status --porcelain=v1` per parsing robusto;
   - `git status --short` solo per output umano rapido;
   - `git --no-pager log --oneline --max-count=N`
3. Prima del commit esegui, quando applicabile:
   - test automatici;
   - `git --no-pager diff --check`;
   - `git --no-pager diff --cached --check` dopo lo staging;
   - verify gate del progetto;
   - controllo file modificati.
4. Per repository Windows valuta `.gitattributes` standard, ma non mischiare normalizzazione line endings a step funzionali salvo richiesta.
5. I warning LF/CRLF non sono fallimento se test, verify gate e `git diff --check` passano.
6. Il push diretto su `main` e' consentito quando Alberto lo richiede e tutti i gate locali passano; branch + PR resta alternativa per repository protette o step che richiedono review.

# Gestione `gh pr checks --watch`

Quando usi `gh pr checks --watch`, gestisci i casi "no checks reported" o pending con exit code 1 oppure 8 senza errore rosso invasivo, se l'output testuale conferma che non si tratta di fallimento reale:

```powershell
$oldPref = $PSNativeCommandUseErrorActionPreference
$PSNativeCommandUseErrorActionPreference = $false

gh pr checks --watch
$ghExitCode = $LASTEXITCODE

$PSNativeCommandUseErrorActionPreference = $oldPref

if ($ghExitCode -eq 0) {
    Write-Host "Checks completati correttamente."
} elseif ($ghExitCode -eq 1 -or $ghExitCode -eq 8) {
    Write-Host "Attenzione: gh pr checks ha restituito exit code $ghExitCode. Verificare se e' solo no-checks/pending."
} else {
    throw "gh pr checks fallito con exit code $ghExitCode"
}
```

# Formato output

Quando prepari comandi, separa sempre:
- scopo;
- blocco da incollare;
- risultato atteso;
- attenzione/rischi.
