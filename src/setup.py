from cx_Freeze import setup, Executable

build_options = {
    "packages": ["customtkinter"],
}

setup(
    name="FlashcardPy",
    version="1.0",
    description="A simple flashcard app",
    options={"build_exe": build_options},
    executables=[Executable("main.py", base="Win32GUI", target_name="FlashcardApp.exe")]
)
