# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['src\\main.py'],
    pathex=[],
    binaries=[('C:\\Users\\jangk\\AppData\\Local\\Programs\\Python\\Python312\\python312.dll', '.')],  # Add Python DLL
    datas=[
          ('C:\\Users\\jangk\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\site-packages\\customtkinter', 'customtkinter\\')
          ],
    optimize=2,
)

# Creating compressed archive for python modules
pyz = PYZ(a.pure)

# Executable generation
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='flashcard_py',
    upx=True,
    console=False,
    onefile=True,

    runtime_tmpdir=None,
    argv_emulation=False,
    target_arch=None
)
