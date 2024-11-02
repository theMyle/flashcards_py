from idlelib.zoomheight import set_window_geometry

import customtkinter as ctk
from typing import List
from flashcard import FlashcardGroup, Flashcard


# A menu frame containing buttons
class NavBarFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.btn_width = 150

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.search_bar= ctk.CTkEntry(self)
        self.search_bar.bind("<Return>", self.filter_groups)
        self.search_bar.grid(column=0, row=0, sticky="EWN", pady=20, padx=10)
        self.create_btn= ctk.CTkButton(self,
                                       text="CREATE NEW SET",
                                       command=self.create_new_flashcard_set,
                                       width=self.btn_width)
        self.create_btn.grid(column=0, row=1, sticky="N", pady=20)

    # Button functions
    def create_new_flashcard_set(self):
        print("Creating a new one")
        print("Todo!") # TODO!!!!!

        window = ctk.CTkToplevel(self)
        window.title("Create New Group")
        window.geometry("400x400+800+200")
        window.attributes('-topmost', 'true')

    # Search bar function
    def filter_groups(self, event):
        print(f"Search this shit: {self.search_bar.get()}. event: {event}")
        print("TODO!") # TODO!!!!!

# A list containing flashcard items
class WidgetFlashcardGroupList(ctk.CTkScrollableFrame):
    def __init__(self, master, group_list: List[FlashcardGroup]):
        super().__init__(master)

        self.items = group_list

        # load items into the gui
        for group in self.items:
            item = FlashcardGroupItem(self, group)
            item.pack(fill="x", pady=5, padx=1)


# Item to be shown in the menu list
class FlashcardGroupItem(ctk.CTkFrame):
    def __init__(self, master, group: FlashcardGroup):
        super().__init__(master)

        self.flashcard_group = group

        self.configure(fg_color="#1E1E1E")
        self.btn_height = 40
        self.btn_width = 70
        self.font_family = "mono"
        self.title_font_size = 16
        self.button_font_size = 12

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=50)
        self.grid_columnconfigure(3, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.title_label = ctk.CTkLabel(self, font=(self.font_family, self.title_font_size),
                                        text=self.flashcard_group.title,
                                        wraplength=250)
        self.title_label.grid(column=2, row=0, padx=10, pady=10)

        self.review_btn = ctk.CTkButton(self, text="Review",
                                        width=self.btn_width, height=self.btn_height,
                                        font=(self.font_family, self.button_font_size),
                                        command=self.review)
        self.review_btn.grid(column=0, row=0, padx=(17,0), pady=15, sticky="W")

        self.edit_btn = ctk.CTkButton(self, text="Edit",
                                      width=self.btn_width, height=self.btn_height,
                                      font=(self.font_family, self.button_font_size),
                                      fg_color="#3A3A3A",
                                      hover_color="#5A5A5A")
        self.edit_btn.grid(column=1, row=0, padx=5, sticky="W")

        self.delete_btn = ctk.CTkButton(self, text="Delete",
                                        width=self.btn_width,
                                        height=self.btn_height,
                                        font=(self.font_family, self.button_font_size),
                                        fg_color="#424242",
                                        hover_color="#D32F2F")
        self.delete_btn.grid(column=3, row=0, padx=(0,10), sticky="E")

    # review function
    def review(self):
        print("REVIEWING")
        print(self.flashcard_group.items)
        print("TODO!!!") # TODO!!

# Main class for the app
class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Defaults
        self.padding = 20
        self.height = 500
        self.width = 800
        self.window_x_pos = 150
        self.window_y_pos = 400

        self.title("Flashcard App")
        self.resizable(False,False)
        self.geometry(f"{self.width}x{self.height}+{self.window_y_pos}+{self.window_x_pos}")

        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 3)
        self.grid_rowconfigure(0,weight = 1)

        # Menu buttons
        self.col1 = NavBarFrame(self)
        self.col1.grid(column=0, row=0, sticky="nsew")

        # Flashcards Group List
        from test_data import generate_test_data        # REMOVE THIS SHIT! For testing only!
        self.col2 = WidgetFlashcardGroupList(self, generate_test_data(50))
        self.col2.grid(column = 1, row = 0, sticky="nsew", padx=(2,0))

if __name__ == "__main__":
    app = App()
    app.mainloop()