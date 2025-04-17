
# check for existing virtual environment
if (!(Test-Path -Path ".\venv\")) {
    Write-Host "Creating virtual environment..."
    python -m venv venv
    Write-Host "Installing python packages..."
    .\venv\Scripts\pip.exe install -r .\requirements.txt > $null
}

Write-Host "Running app..."
.\venv\Scripts\python.exe .\src\main.py
