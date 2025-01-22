import customtkinter as ctk
from frame_main import MainFrame


# Main class for the app
class App(ctk.CTk):
    def __init__(self, title):
        super().__init__()

        self.current_window = None
        self.title(title)
        self.padding = 20
        self.height = 720 
        self.width = 1280
        self.window_x_pos = 50
        self.window_y_pos = 150
        self.minsize(self.width, self.height)
        self.geometry(f"{self.width}x{self.height}+{self.window_y_pos}+{self.window_x_pos}")

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
    app.frame_main.load_content()
    app.mainloop()
