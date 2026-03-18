param(
    [Parameter(Mandatory = $true)]
    [string]$Name
)

$repoRoot = Split-Path -Parent $PSScriptRoot
$templateDir = Join-Path $repoRoot "skills\_template"
$targetDir = Join-Path $repoRoot "skills\$Name"

if (Test-Path $targetDir) {
    Write-Error "Skill '$Name' already exists."
    exit 1
}

Copy-Item $templateDir $targetDir -Recurse

$skillPath = Join-Path $targetDir "SKILL.md"
$content = Get-Content $skillPath -Raw
$description = "Describe what this skill does and when to use it. Mention concrete triggers, repositories, file types, or workflows so Claude can activate it correctly."
$content = $content.Replace("{{SKILL_NAME}}", $Name)
$content = $content.Replace("{{SKILL_DESCRIPTION}}", $description)
Set-Content -Path $skillPath -Value $content

Write-Host "Created skill scaffold at $targetDir"
