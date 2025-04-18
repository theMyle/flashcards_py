@echo off

IF NOT EXIST "venv\" (
  python setup.py
)

.\venv\Scripts\python.exe src\main.py
