import customtkinter as ctk
from frame_main import MainFrame
from database import FlashcardDB

# Main class for the app
class App(ctk.CTk):
    def __init__(self, title):
        super().__init__()

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        self.current_window = None
        self.title(title)
        self.padding = 20
        self.height = 720 - 120
        self.width =  1280 - 120
        self.window_x_pos = (screen_width - self.width) // 2
        self.window_y_pos = (screen_height - self.height) // 2
        self.minsize(self.width, self.height)
        self.geometry(f"{self.width}x{self.height}+{self.window_x_pos}+{self.window_y_pos}")
        self.frame_main = MainFrame(self,self)

    # changes content of the current window to a new specified frame
    def change_frame(self, frame):
        if self.current_window != None:
            self.current_window.pack_forget()

        self.current_window = frame
        self.current_window.pack(fill="both", expand=True)

    def load_main(self):
        if self.current_window != None:
            self.current_window.pack_forget()

        self.current_window = self.frame_main
        self.current_window.pack(fill="both", expand=True)


if __name__ == "__main__":
    app_name = "Flashcard App"
    app = App(app_name)
    app.load_main()
    app.mainloop()
