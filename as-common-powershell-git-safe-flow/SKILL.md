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

1. Nei blocchi PowerShell multilinea, lascia una riga finale vuota.
2. Nei comandi PowerShell a riga singola destinati al copia/incolla, aggiungi una seconda riga innocua:
   ```powershell
   Write-Host ""
   ```
3. Non usare `setx PATH ...` per modifiche permanenti del PATH: può troncare il PATH. Usa invece:
   ```powershell
   [Environment]::SetEnvironmentVariable("Path", $nuovoPath, "User")
   ```
4. Evita comandi distruttivi (`Remove-Item -Recurse -Force`, reset, clean, checkout forzati) senza spiegare cosa eliminano e senza conferma esplicita.
5. Se uno script `.ps1` è bloccato da Execution Policy, preferisci soluzioni trasparenti:
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
   - `git status --short`
   - `git --no-pager log --oneline --max-count=N`
3. Prima del commit esegui, quando applicabile:
   - test automatici;
   - `git diff --check`;
   - verify gate del progetto;
   - controllo file modificati.
4. Per repository Windows valuta `.gitattributes` standard, ma non mischiare normalizzazione line endings a step funzionali salvo richiesta.
5. I warning LF/CRLF non sono fallimento se test, verify gate e `git diff --check` passano.

# Gestione `gh pr checks --watch`

Quando usi `gh pr checks --watch`, gestisci il caso "no checks reported" / exit code 1 senza errore rosso invasivo:

```powershell
$oldPref = $PSNativeCommandUseErrorActionPreference
$PSNativeCommandUseErrorActionPreference = $false

gh pr checks --watch
$ghExitCode = $LASTEXITCODE

$PSNativeCommandUseErrorActionPreference = $oldPref

if ($ghExitCode -eq 0) {
    Write-Host "Checks completati correttamente."
} elseif ($ghExitCode -eq 1) {
    Write-Host "Attenzione: gh pr checks ha restituito exit code 1. Verificare se è solo 'no checks reported'."
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
