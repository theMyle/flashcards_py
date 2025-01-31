import subprocess
import os

main_py = os.path.abspath("./src/main.py")
python_path = os.path.abspath("./venv/Scripts/python.exe")

command = [python_path, main_py]
result = subprocess.run(command)
