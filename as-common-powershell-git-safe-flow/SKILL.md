---
name: as-common-powershell-git-safe-flow
description: Usa questa skill quando devi generare o verificare comandi PowerShell/Git sicuri, linee guida Git o blocchi brevi per Alberto su Windows. Non usarla per costruire command pack PowerShell completi con Bridge, report e artifact riutilizzabili.
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

# Quando NON usarla

Non usarla per:
- generare un command pack operativo completo con file `.ps1`, log, report e output Bridge;
- preparare un prompt Codex temporaneo senza comandi PowerShell;
- governare tutto il lifecycle di uno step numerato.

# Usa invece

- `as-common-pwsh-command-pack` quando serve un pacchetto operativo completo con script, Bridge, report e artifact.
- `as-common-codex-command-pack` quando serve solo un prompt Codex.
- `as-common-codex-step-manager` quando il lavoro e' gestire uno step numerato end-to-end.

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

# Diagnostiche Git critiche

Per diagnostiche delicate usa comandi Git diretti ed espliciti, soprattutto se un gate fallisce:

```powershell
git status --short
git status -sb
git diff --cached --name-status
git diff --cached --check
git diff --name-status
git diff --check
```

Evita wrapper generici che costruiscono array di argomenti Git in modo opaco quando devi capire un errore reale. In questi casi salva l'output completo, registra subito `$LASTEXITCODE`, non fermare la raccolta evidenze al primo exit code diverso da zero se lo scopo e' diagnostico, e usa `git --no-pager` solo quando la forma del comando e' certa.

# Here-string Markdown fragili

Nei blocchi PowerShell da incollare in terminale evita here-string lunghe che contengono Markdown complesso, triple backtick, JSON, interpolazioni o testo multilinea non banale. Se l'incolla viene troncato o la chiusura non arriva, PowerShell resta nel prompt `>>`.

Per report Markdown generati da PowerShell preferisci righe esplicite:

```powershell
$Lines = @()
$Lines += "# Titolo"
$Lines += ""
$Lines += "## Sezione"
$Lines += "testo"
Set-Content -Path $File -Value ($Lines -join "`r`n") -Encoding UTF8
```

Usa here-string solo per testi brevi, controllati, senza triple backtick e senza rischio di troncamento.

# Cached diff check e fix mirato EOF

Prima di rilanciare una Phase B o prima di commit/push/PR quando esistono file staged, esegui:

```powershell
git diff --cached --check
```

Se fallisce, non rilanciare la fase e non pubblicare. Leggi l'output reale, identifica solo i file segnalati, fai backup prima di qualunque correzione automatica, correggi solo quei file, ristagia solo quei file e poi riesegui:

```powershell
git diff --cached --check
git diff --check
```

Per `new blank line at EOF`, rimuovi righe vuote finali extra solo dai file indicati dal diff check, lasciando una sola newline finale. Non usare reset, clean o fix globali su tutta la repository.

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
