import tkinter as tk
from tkinter import ttk

root = tk.Tk()

# Enable High DPI Scaling
try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)  # Fix blurry UI on Windows
except:
    pass

root.title("Sharp Tkinter UI")
root.geometry("400x300")

label = ttk.Label(root, text="This text should be sharp!", font=("Arial", 14))
label.pack(pady=20)

root.mainloop()
