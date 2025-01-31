@echo off

if not exist "setup.ps1" (
    :: Create an empty file
    type nul > setup.ps1
    :: Copy the content of the file 
    copy /Y "scripts\setup.ps1" "runner.ps1" > nul
)

:: Run
powershell -ExecutionPolicy Bypass -File "runner.ps1"