
# check for python installation
Write-Host "Checking Python Installation..."
$pythonPath = Get-Command python -ErrorAction SilentlyContinue
if (!($pythonPath))
{
	Write-Host "Error: No python installation found" -ForegroundColor Red
	exit 1
}

Write-Host "Python Installation Found: " -NoNewline
$python_version = & python --version
Write-Host "$python_version`n" -ForegroundColor Green


# check for existing virtual environment
if (!(Test-Path -Path ".\venv\"))
{
    Write-Host "Creating virtual environment..."
    python -m venv venv
    Write-Host "Virtual environment successfully created`n"
}


Write-Host "Installing python packages..."
.\venv\Scripts\pip.exe install -r .\requirements.txt > $null
Write-Host "Required python packages successfully installed`n"


Write-Host "Running app..."
.\run.ps1
