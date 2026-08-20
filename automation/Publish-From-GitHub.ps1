$ErrorActionPreference = "Stop"

$RepoRoot = (Resolve-Path (Join-Path $PSScriptRoot "..")).Path
$Remote = "r2:506th-arma3-mods"
$Manifest = Join-Path $PSScriptRoot "manifest.json"
$HashCache = Join-Path $PSScriptRoot ".manifest_hash_cache.json"
$Generator = Join-Path $PSScriptRoot "generate_manifest.py"

function Require-Command {
    param([string]$Name)
    if (-not (Get-Command $Name -ErrorAction SilentlyContinue)) {
        throw "Required command '$Name' was not found in PATH."
    }
}

Require-Command "git"
Require-Command "rclone"
Require-Command "py"

Push-Location $RepoRoot
try {
    git lfs install --local
    if ($LASTEXITCODE -ne 0) { throw "git lfs install failed." }

    git lfs pull
    if ($LASTEXITCODE -ne 0) { throw "git lfs pull failed." }
}
finally {
    Pop-Location
}

& rclone sync $RepoRoot $Remote -P `
    --s3-no-check-bucket `
    --exclude ".git/**" `
    --exclude ".github/**" `
    --exclude "automation/**" `
    --exclude "publisher/**" `
    --exclude "updater/**" `
    --exclude ".gitignore" `
    --exclude ".gitattributes" `
    --exclude "manifest.json" `
    --exclude ".506th_updater_state.json" `
    --exclude ".manifest_hash_cache.json" `
    --exclude "*.506thdownload"

if ($LASTEXITCODE -ne 0) { throw "Repository sync failed." }

& py $Generator $RepoRoot -o $Manifest --cache $HashCache
if ($LASTEXITCODE -ne 0) { throw "Manifest generation failed." }

& rclone copyto $Manifest "$Remote/manifest.json" -P --s3-no-check-bucket
if ($LASTEXITCODE -ne 0) { throw "Manifest upload failed." }
