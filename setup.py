import sys
import os
import platform
import subprocess

required_python_version = (3, 8)
venv_dir = "./venv"

check = "✅"
cross = "❌"

def ensure_python_version(major, minor):
    if (sys.version_info.major >= major and sys.version_info.minor >= minor):
        print(f"{check} - python version >= {major}.{minor}")
        return True
    else:
        print(f"{cross} - python version >= {major}.{minor}")
        return False

def ensure_venv():
    try:
        import venv
        print(f"{check} - venv module")
        return True
    except:
        print(f"{cross} - venv module")
        return False

def ensure_pip():
    try:
        import pip
        print(f"{check} - pip {pip.__version__}")
        return True
    except:
        print(f"{cross} - pip {pip.__version__}")
        return False

def main():
    continue_setup = True

    print("Checking Setup Requirements 🚀🚀🚀\n")
    summary = {
        f"{cross} - minimun python version requirement not met. Please update your python installation." : ensure_python_version(required_python_version[0], required_python_version[1]),
        f"{cross} - venv not found, cannot create virtual env.": ensure_venv(),
        f"{cross} - pip not found, cannot install packages.": ensure_pip()
    }

    print('\nSummary 🔍🔍🔍:')
    for i in summary:
        if summary[i] == False:
            continue_setup = False
            print(i)

    if continue_setup == False:
        sys.exit()

    print(f"Requirements fulfilled {check}, proceeding to setup...\n")

    # create venv
    print("Creating virtual env... ", end="", flush=True)
    try:
        import venv
        builder = venv.EnvBuilder(with_pip=True)
        builder.create(venv_dir)
        print(f"{check}")
    except Exception as e:
        print(f"{cross} - Error creating virtual env: {e}")
        return

    # check for requirements.txt
    if os.path.isfile("requirements.txt"):
        print("Installing requirements... ", end="", flush=True)

        python_path = ""
        pip_path = ""

        try:
            system = platform.system().lower()

            if system == "windows":
                python_path = os.path.join(venv_dir, "Scripts", "python.exe")
                pip_path = os.path.join(venv_dir, "Scripts", "pip.exe")

            elif system == "linux":
                python_path = os.path.join(venv_dir, "bin", "python")
                pip_path = os.path.join(venv_dir, "bin", "pip")
            else:
                print(f"{cross} - Script does not support {system} systems, please manually install requirements.txt.")
                return

            if not os.path.isfile(python_path):
                print(f"{cross} - Something wrong with virtual env, python not found (.\\{python_path} does not exist)")
                return
            if not os.path.isfile(pip_path):
                print(f"{cross} - Something wrong with virtual env, pip not found (.\\{pip_path} does not exist).")
                return

            # install requirements.txt
            subprocess.run(
                [pip_path, 'install', '-r', 'requirements.txt'], 
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

            print(check)
        except Exception as e:
            print(f"{cross} - Error installing requirements.txt: {e}")
            return

    print("\nSetup complete!!! 🎉🎉🎉")

main()
