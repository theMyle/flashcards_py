$folder_path = ".\venv\"

if (!(Test-Path -Path $folder_path)) {
    Write-Host "Creating virtual environment..."
    python -m venv venv
    Write-Host "Virtual environment successfully created"
}

.\venv\Scripts\pip.exe install -r .\requirements.txt
Write-Host "Required python packages successfully installed"

Write-Host "Running app..."
.\run.ps1
