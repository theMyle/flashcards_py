
# check for existing virtual environment
if (!(Test-Path -Path ".\venv\"))
{
    Write-Host "Creating virtual environment..."
    python -m venv venv
    Write-Host "Virtual environment successfully created`n"

    Write-Host "Installing python packages..."
    .\venv\Scripts\pip.exe install -r .\requirements.txt > $null
    Write-Host "Required python packages successfully installed`n"
}

Write-Host "Running app..."
.\venv\Scripts\python.exe .\src\main.py
