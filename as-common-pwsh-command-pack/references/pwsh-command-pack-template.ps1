#Requires -Version 7.0
[CmdletBinding()]
param(
    [Parameter()]
    [ValidateNotNullOrEmpty()]
    [string]$CommandPackName = 'asf-command-pack',

    [Parameter()]
    [ValidateNotNullOrEmpty()]
    [string]$RequestText = 'Generated PowerShell command pack.',

    [Parameter()]
    [ValidateNotNullOrEmpty()]
    [string]$BridgeRoot = 'D:\FG-SAB Dropbox\Alberto Ferrari\ChatGPT_Bridge',

    [Parameter()]
    [ValidateNotNullOrEmpty()]
    [string]$OutputRoot = 'D:\FG-SAB Dropbox\Alberto Ferrari\ChatGPT_Bridge\AI_Software_Factory\pwsh_command',

    [Parameter()]
    [ValidateNotNullOrEmpty()]
    [string]$RepositoryRoot = (Get-Location).Path,

    [Parameter()]
    [ValidateSet('A', 'B', 'C')]
    [string]$Phase = 'A',

    [Parameter()]
    [switch]$AllowPublication
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$PSDefaultParameterValues['Out-File:Width'] = 2000
$PSDefaultParameterValues['Out-File:Encoding'] = 'utf8NoBOM'

if (Get-Variable -Name PSNativeCommandUseErrorActionPreference -Scope Global -ErrorAction SilentlyContinue) {
    $PSNativeCommandUseErrorActionPreference = $true
}

$script:FullLogLines = [System.Collections.Generic.List[string]]::new()
$script:Warnings = [System.Collections.Generic.List[string]]::new()
$script:Failures = [System.Collections.Generic.List[string]]::new()
$script:StartedAt = Get-Date

function Format-SafeFileName {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [string]$Name
    )

    $normalized = $Name.ToLowerInvariant().Normalize([System.Text.NormalizationForm]::FormD)
    $builder = [System.Text.StringBuilder]::new()
    foreach ($character in $normalized.ToCharArray()) {
        $category = [System.Globalization.CharUnicodeInfo]::GetUnicodeCategory($character)
        if ($category -ne [System.Globalization.UnicodeCategory]::NonSpacingMark) {
            [void]$builder.Append($character)
        }
    }

    $safe = [regex]::Replace($builder.ToString(), '[^a-z0-9-]+', '-')
    $safe = [regex]::Replace($safe, '-{2,}', '-').Trim('-')
    if ([string]::IsNullOrWhiteSpace($safe)) {
        return 'command-pack'
    }
    return $safe
}

function Get-NextCommandPackNumber {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [string]$Path
    )

    if (-not (Test-Path -LiteralPath $Path)) {
        return '0001'
    }

    $numbers = Get-ChildItem -LiteralPath $Path -File -ErrorAction Stop |
        Where-Object { $_.Name -match '^(?<number>\d{4})-' } |
        ForEach-Object { [int]$Matches['number'] }

    if (-not $numbers) {
        return '0001'
    }

    return ('{0:0000}' -f (($numbers | Measure-Object -Maximum).Maximum + 1))
}

function Out-Utf8NoBomFile {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [string]$LiteralPath,

        [Parameter(Mandatory)]
        [AllowEmptyString()]
        [string]$Content
    )

    $encoding = [System.Text.UTF8Encoding]::new($false)
    [System.IO.File]::WriteAllText($LiteralPath, $Content, $encoding)
}

function Add-LogLine {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [AllowEmptyString()]
        [string]$Message
    )

    $line = '[{0}] {1}' -f (Get-Date -Format 'yyyy-MM-dd HH:mm:ss'), $Message
    $script:FullLogLines.Add($line)
    Write-Output $line
}

function Add-WarningLine {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [string]$Message
    )

    $script:Warnings.Add($Message)
    Add-LogLine "WARNING: $Message"
}

function Add-FailureLine {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [string]$Message
    )

    $script:Failures.Add($Message)
    Add-LogLine "FAILURE: $Message"
}

function Test-NativeExitCode {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [int]$ExitCode,

        [Parameter(Mandatory)]
        [string]$Label,

        [Parameter()]
        [AllowEmptyString()]
        [string]$OutputText = '',

        [Parameter()]
        [switch]$TreatGhNoChecksAsWarning
    )

    if ($ExitCode -eq 0) {
        return
    }

    $isNoChecksWarning = $TreatGhNoChecksAsWarning -and
        $ExitCode -eq 1 -and
        ($OutputText -match '(?i)no checks reported|no checks|could not find any checks')

    if ($isNoChecksWarning) {
        Add-WarningLine "$Label returned exit code 1 with no checks reported. Treating as controlled warning because local gates must still pass."
        return
    }

    throw "$Label failed with exit code $ExitCode."
}

function Invoke-LoggedNativeCommand {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [string]$Label,

        [Parameter(Mandatory)]
        [string]$FilePath,

        [Parameter()]
        [string[]]$ArgumentList = @(),

        [Parameter()]
        [string]$WorkingDirectory = (Get-Location).Path,

        [Parameter()]
        [switch]$TreatGhNoChecksAsWarning
    )

    Add-LogLine "START $Label"
    Add-LogLine ('COMMAND {0} {1}' -f $FilePath, ($ArgumentList -join ' '))
    Add-LogLine "WORKDIR $WorkingDirectory"

    Push-Location -LiteralPath $WorkingDirectory
    try {
        $commandOutput = & $FilePath @ArgumentList 2>&1
        $nativeExitCode = $LASTEXITCODE
    }
    finally {
        Pop-Location
    }

    $outputText = ($commandOutput | Out-String).TrimEnd()
    if (-not [string]::IsNullOrWhiteSpace($outputText)) {
        foreach ($line in ($outputText -split "`r?`n")) {
            Add-LogLine $line
        }
    }
    else {
        Add-LogLine '<no output>'
    }

    Test-NativeExitCode -ExitCode $nativeExitCode -Label $Label -OutputText $outputText -TreatGhNoChecksAsWarning:$TreatGhNoChecksAsWarning
    Add-LogLine "END $Label exit=$nativeExitCode"
}

function Invoke-GhPrChecksWarningAware {
    [CmdletBinding()]
    param(
        [Parameter()]
        [string]$WorkingDirectory = (Get-Location).Path
    )

    Invoke-LoggedNativeCommand -Label 'gh pr checks --watch' -FilePath 'gh' -ArgumentList @('pr', 'checks', '--watch') -WorkingDirectory $WorkingDirectory -TreatGhNoChecksAsWarning
}

function Test-PublicationGate {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [bool]$TestsPassed,

        [Parameter(Mandatory)]
        [bool]$VerifyPassed,

        [Parameter(Mandatory)]
        [bool]$HealthCheckPassed,

        [Parameter(Mandatory)]
        [bool]$GuardrailsPassed
    )

    $blockedReasons = [System.Collections.Generic.List[string]]::new()
    if (-not $TestsPassed) { $blockedReasons.Add('tests failed or were not run') }
    if (-not $VerifyPassed) { $blockedReasons.Add('verify failed or was not run') }
    if (-not $HealthCheckPassed) { $blockedReasons.Add('health check failed or was not run') }
    if (-not $GuardrailsPassed) { $blockedReasons.Add('guardrails failed or were not run') }

    if ($blockedReasons.Count -gt 0) {
        throw ('Publication phase blocked: {0}.' -f ($blockedReasons -join '; '))
    }
}

function ConvertTo-OpenXmlText {
    [CmdletBinding()]
    param(
        [Parameter()]
        [AllowEmptyString()]
        [string]$Text = ''
    )

    return [System.Security.SecurityElement]::Escape($Text)
}

function ConvertTo-CompactDocx {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [string]$MarkdownPath,

        [Parameter(Mandatory)]
        [string]$DocxPath
    )

    Add-Type -AssemblyName System.IO.Compression.FileSystem
    $tempRoot = Join-Path ([System.IO.Path]::GetTempPath()) ('asf-docx-' + [System.Guid]::NewGuid().ToString('N'))

    try {
        $wordPath = Join-Path $tempRoot 'word'
        $relsRoot = Join-Path $tempRoot '_rels'
        New-Item -ItemType Directory -Force -LiteralPath $wordPath | Out-Null
        New-Item -ItemType Directory -Force -LiteralPath $relsRoot | Out-Null

        $contentTypesXml = @"
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
</Types>
"@
        Out-Utf8NoBomFile -LiteralPath (Join-Path $tempRoot '[Content_Types].xml') -Content $contentTypesXml

        $rootRelsXml = @"
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>
"@
        Out-Utf8NoBomFile -LiteralPath (Join-Path $relsRoot '.rels') -Content $rootRelsXml

        $paragraphs = [System.Collections.Generic.List[string]]::new()
        foreach ($line in (Get-Content -LiteralPath $MarkdownPath -ErrorAction Stop)) {
            $escapedLine = ConvertTo-OpenXmlText -Text $line
            $paragraphs.Add("<w:p><w:r><w:t xml:space=""preserve"">$escapedLine</w:t></w:r></w:p>")
        }
        if ($paragraphs.Count -eq 0) {
            $paragraphs.Add('<w:p><w:r><w:t>Empty report.</w:t></w:r></w:p>')
        }

        $bodyXml = $paragraphs -join [Environment]::NewLine
        $documentXml = @"
<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:body>
$bodyXml
    <w:sectPr><w:pgSz w:w="12240" w:h="15840"/><w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440"/></w:sectPr>
  </w:body>
</w:document>
"@
        Out-Utf8NoBomFile -LiteralPath (Join-Path $wordPath 'document.xml') -Content $documentXml

        if (Test-Path -LiteralPath $DocxPath) {
            Remove-Item -LiteralPath $DocxPath -Force
        }
        [System.IO.Compression.ZipFile]::CreateFromDirectory($tempRoot, $DocxPath)
    }
    finally {
        if (Test-Path -LiteralPath $tempRoot) {
            Remove-Item -LiteralPath $tempRoot -Recurse -Force
        }
    }
}

function Invoke-LastArtifactCopy {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)]
        [hashtable]$Artifacts,

        [Parameter(Mandatory)]
        [string]$Path
    )

    Copy-Item -LiteralPath $Artifacts.Request -Destination (Join-Path $Path 'LAST-Richiesta_Generazione.txt') -Force
    Copy-Item -LiteralPath $Artifacts.Script -Destination (Join-Path $Path 'LAST-Comando_Eseguito.ps1') -Force
    Copy-Item -LiteralPath $Artifacts.FullOutput -Destination (Join-Path $Path 'LAST-Output_Completo.txt') -Force
    Copy-Item -LiteralPath $Artifacts.CompactMarkdown -Destination (Join-Path $Path 'LAST-Output_Compatto.md') -Force
    Copy-Item -LiteralPath $Artifacts.CompactDocx -Destination (Join-Path $Path 'LAST-Output_Compatto.docx') -Force

    try {
        Get-Content -Raw -LiteralPath (Join-Path $Path 'LAST-Output_Compatto.md') | Set-Clipboard
        Add-LogLine 'Copied LAST-Output_Compatto.md to clipboard.'
    }
    catch {
        Add-WarningLine "Set-Clipboard failed: $($_.Exception.Message)"
    }
}

function Invoke-CommandPack {
    [CmdletBinding()]
    param()

    New-Item -ItemType Directory -Force -LiteralPath $OutputRoot | Out-Null
    $safeName = Format-SafeFileName -Name $CommandPackName
    $number = Get-NextCommandPackNumber -Path $OutputRoot

    $artifacts = @{
        Request = Join-Path $OutputRoot "$number-Richiesta_Generazione_$safeName.txt"
        Script = Join-Path $OutputRoot "$number-Comando_Eseguito_$safeName.ps1"
        FullOutput = Join-Path $OutputRoot "$number-Output_Completo_$safeName.txt"
        CompactMarkdown = Join-Path $OutputRoot "$number-Output_Compatto_$safeName.md"
        CompactDocx = Join-Path $OutputRoot "$number-Output_Compatto_$safeName.docx"
    }

    $testsPassed = $false
    $verifyPassed = $false
    $healthCheckPassed = $false
    $guardrailsPassed = $false
    $finalStatus = 'FAILED'

    try {
        Out-Utf8NoBomFile -LiteralPath $artifacts.Request -Content $RequestText
        if (-not [string]::IsNullOrWhiteSpace($PSCommandPath)) {
            Copy-Item -LiteralPath $PSCommandPath -Destination $artifacts.Script -Force
        }
        else {
            Out-Utf8NoBomFile -LiteralPath $artifacts.Script -Content '# Script path was not available in this host.'
        }

        Add-LogLine 'PowerShell command pack started.'
        Add-LogLine "Bridge root: $BridgeRoot"
        Add-LogLine "Output root: $OutputRoot"
        Add-LogLine "Repository root: $RepositoryRoot"
        Add-LogLine "Phase: $Phase"

        Invoke-LoggedNativeCommand -Label 'git status --short' -FilePath 'git' -ArgumentList @('--no-pager', 'status', '--short') -WorkingDirectory $RepositoryRoot
        $guardrailsPassed = $true

        Invoke-LoggedNativeCommand -Label 'git diff --check' -FilePath 'git' -ArgumentList @('--no-pager', 'diff', '--check') -WorkingDirectory $RepositoryRoot

        if (Test-Path -LiteralPath (Join-Path $RepositoryRoot 'scripts\verify.ps1')) {
            Invoke-LoggedNativeCommand -Label 'scripts/verify.ps1' -FilePath 'pwsh' -ArgumentList @('-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', 'scripts/verify.ps1') -WorkingDirectory $RepositoryRoot
            $verifyPassed = $true
            $testsPassed = $true
        }
        else {
            Add-WarningLine 'scripts/verify.ps1 not found; run project-specific tests manually before publication.'
        }

        if (Test-Path -LiteralPath (Join-Path $RepositoryRoot 'scripts\check_workflow_health.py')) {
            Invoke-LoggedNativeCommand -Label 'Workflow Health Check' -FilePath 'python' -ArgumentList @('scripts/check_workflow_health.py') -WorkingDirectory $RepositoryRoot
            $healthCheckPassed = $true
        }
        else {
            Add-WarningLine 'scripts/check_workflow_health.py not found; health check not applicable for this repository.'
            $healthCheckPassed = $true
        }

        if ($Phase -in @('B', 'C')) {
            if (-not $AllowPublication) {
                throw 'Publication phase requested but -AllowPublication was not provided.'
            }
            Test-PublicationGate -TestsPassed:$testsPassed -VerifyPassed:$verifyPassed -HealthCheckPassed:$healthCheckPassed -GuardrailsPassed:$guardrailsPassed
            Add-LogLine 'Publication gate passed, but this template does not run commit, push, PR, merge, release, deploy, or restart automatically.'
        }

        $finalStatus = 'PASSED'
    }
    catch {
        Add-FailureLine $_.Exception.Message
        $finalStatus = 'FAILED'
    }
    finally {
        $endedAt = Get-Date
        $duration = New-TimeSpan -Start $script:StartedAt -End $endedAt
        $fullOutput = $script:FullLogLines -join [Environment]::NewLine
        Out-Utf8NoBomFile -LiteralPath $artifacts.FullOutput -Content ($fullOutput + [Environment]::NewLine)

        $warningBlock = if ($script:Warnings.Count -gt 0) { $script:Warnings -join [Environment]::NewLine } else { 'None' }
        $failureBlock = if ($script:Failures.Count -gt 0) { $script:Failures -join [Environment]::NewLine } else { 'None' }
        $compactMarkdown = @"
# PowerShell Command Pack Output

- Status: $finalStatus
- Started: $($script:StartedAt.ToString('o'))
- Ended: $($endedAt.ToString('o'))
- DurationSeconds: $([math]::Round($duration.TotalSeconds, 2))
- Phase: $Phase
- OutputRoot: $OutputRoot
- RepositoryRoot: $RepositoryRoot

## Artifacts

- Request: $($artifacts.Request)
- Script: $($artifacts.Script)
- FullOutput: $($artifacts.FullOutput)
- CompactMarkdown: $($artifacts.CompactMarkdown)
- CompactDocx: $($artifacts.CompactDocx)

## Guardrails

- Launcher: pwsh -NoProfile -ExecutionPolicy Bypass -File
- Git long output: git --no-pager
- Publication requires explicit phase and passing tests, verify, health check, and guardrails.
- No commit, push, PR, merge, release, deploy, or restart is executed by default.
- setx PATH is forbidden.

## Warnings

$warningBlock

## Failures

$failureBlock
"@
        Out-Utf8NoBomFile -LiteralPath $artifacts.CompactMarkdown -Content $compactMarkdown
        ConvertTo-CompactDocx -MarkdownPath $artifacts.CompactMarkdown -DocxPath $artifacts.CompactDocx
        Invoke-LastArtifactCopy -Artifacts $artifacts -Path $OutputRoot
    }

    if ($finalStatus -ne 'PASSED') {
        exit 1
    }
}

Invoke-CommandPack