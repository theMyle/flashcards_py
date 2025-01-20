import customtkinter as ctk
from typing import List
from card import FlashcardGroup, Flashcard

from frame_main import MainFrame
from frame_edit import EditFrame
from frame_review import ReviewFrame

# Main class for the app
class App(ctk.CTk):
    def __init__(self, title):
        super().__init__()

        self.current_window = None
        self.title(title)
        self.padding = 20
        # self.height = 500
        # self.width = 1000 
        self.height = 720 
        self.width = 1280
        self.window_x_pos = 50
        self.window_y_pos = 150
        # self.resizable(False,False)
        self.minsize(self.width, self.height)
        self.geometry(f"{self.width}x{self.height}+{self.window_y_pos}+{self.window_x_pos}")
        # self.geometry(f"{self.width}x{self.height}")

    def change_frame(self, frame):
        if self.current_window != None:
            self.current_window.pack_forget()

        self.current_window = frame
        self.current_window.pack(fill="both", expand=True)

    # 1. Main App Menu Frame
    def load_main(self):
        if self.current_window != None:
            self.current_window.pack_forget()

        self.current_window = MainFrame(self, self)
        self.current_window.pack(fill="both", expand=True)

if __name__ == "__main__":
    app_name = "Flashcard App"
    app = App(app_name)
    app.load_main()
    app.mainloop()
