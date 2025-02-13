@echo off

powershell unblock-file "./scripts/setup.ps1"
powershell -ExecutionPolicy Bypass "./scripts/setup.ps1"
