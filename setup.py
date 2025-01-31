import subprocess
import os

setup_script = os.path.abspath("./setup.ps1")
command = ["powershell", "-NoProfile", "-Command", setup_script]
result = subprocess.run(command)
