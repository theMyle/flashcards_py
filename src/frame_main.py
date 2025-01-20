import customtkinter as ctk
from typing import List

from card import FlashcardGroup
from frame_edit import EditFrame
from frame_review import ReviewFrame

# Main window for the application
# The first window to interact with
class MainFrame(ctk.CTkFrame):
    def __init__(self, master, root):
        super().__init__(master)

        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 5)
        self.grid_rowconfigure(0, weight = 1)

        # Menu widgets
        self.col1 = NavMenuFrame(self)
        self.col1.grid(column=0, row=0, sticky="nsew")

        # Flashcards Group List
        from test_data import generate_test_data        # REMOVE THIS SHIT! For testing only!
        self.col2 = FlashcardGroupScrollWidget(self, root, generate_test_data(50))
        self.col2.grid(column = 1, row = 0, sticky="nsew", padx=(2,0))


# Menu frame containing buttons and functionalities for searching
# and creating new flashcard groups
class NavMenuFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.btn_width = 150

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=3)

        # search widget
        self.search_widget = ctk.CTkFrame(self)
        self.search_widget.grid(column=0, row=0, sticky="EWN", pady=20, padx=10)
        self.search_widget.grid_columnconfigure(0, weight=1)
        self.search_widget.grid_rowconfigure(0, weight=1)
        self.search_widget.grid_rowconfigure(1, weight=1)

        # search bar widget grid and column configurations
        self.lbl_search_bar = ctk.CTkLabel(self.search_widget, text="Search")
        self.lbl_search_bar.grid(column=0, row=0, sticky="N", padx=10, pady=(10,0))
        self.search_bar = ctk.CTkEntry(self.search_widget)
        self.search_bar.bind("<Return>", self.filter_groups)
        self.search_bar.grid(column=0, row=1, sticky="EWN", pady=(0, 20), padx=10)

        # flashcard group creator widget
        self.group_creator_widget = ctk.CTkFrame(self)
        self.group_creator_widget.grid(column=0, row=1, sticky="EWN", pady=20, padx=10)
        self.group_creator_widget.grid_columnconfigure(0, weight=1)
        self.group_creator_widget.grid_rowconfigure(0, weight=1)
        self.group_creator_widget.grid_rowconfigure(1, weight=1)

        # flashcard group creator widget grid and column configs
        self.lbl_group_creator_name= ctk.CTkLabel(self.group_creator_widget)
        self.lbl_group_creator_name.grid(column=0, row=1, sticky="W", padx=10, pady=(10,5))
        self.lbl_group_creator_name.configure(text="Group Name")
        self.group_name_entry= ctk.CTkEntry(self.group_creator_widget)
        self.group_name_entry.grid(column=0, row=2, sticky="EWN", pady=(0, 20), padx=10)
        self.create_btn= ctk.CTkButton(self.group_creator_widget,
                                       text="CREATE NEW SET",
                                       command=self.create_new_flashcard_set,
                                       width=self.btn_width)
        self.create_btn.grid(column=0, row=99, sticky="N", pady=(0, 20))

    def create_new_flashcard_set(self):
        print("Creating a new one")
        print("Todo!") # TODO

    # Search Bar (Enter - Pressed)
    def filter_groups(self, event):
        print(f"Search: {self.search_bar.get()}")
        print(f"Event: {event}")
        print("TODO!") # TODO


# scrollbar widget for flashcard groups
class FlashcardGroupScrollWidget(ctk.CTkScrollableFrame):
    def __init__(self, master, root, group_list: List[FlashcardGroup]):
        super().__init__(master)

        self.items = group_list

        # load items into the widget
        for group in self.items:
            item = FlashcardGroupFrame(self, root, group)
            item.pack(fill="x", pady=5, padx=1)


# Widget for flashcard group holding the buttons, title and others group information
class FlashcardGroupFrame(ctk.CTkFrame):
    def __init__(self, master, root, group: FlashcardGroup):
        super().__init__(master)

        # members
        self.root = root
        self.flashcard_group = group
        self.title_label = None
        self.review_btn = None
        self.edit_btn = None
        self.delete_btn = None

        # design config
        self.configure(fg_color="#1E1E1E")
        self.btn_height = 60
        self.btn_width = 100
        self.font_family = "mono"
        self.title_font_size = 18
        self.button_font_size = 14

        # layout config
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=50)
        self.grid_columnconfigure(3, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.title_label = ctk.CTkLabel(self, font=(self.font_family, self.title_font_size),
                                        text=self.flashcard_group.title,
                                        text_color="white",
                                        wraplength=500)
        self.title_label.grid(column=2, row=0, padx=20, sticky="w")
        self.review_btn = ctk.CTkButton(self, text="Review",
                                        width=self.btn_width, height=self.btn_height,
                                        font=(self.font_family, self.button_font_size),
                                        command=self.review_window)
        self.review_btn.grid(column=0, row=0, padx=(17,0), pady=15, sticky="W")
        self.edit_btn = ctk.CTkButton(self, text="Edit",
                                      width=self.btn_width, height=self.btn_height,
                                      font=(self.font_family, self.button_font_size),
                                      fg_color="#3A3A3A",
                                      hover_color="#5A5A5A",
                                      command=self.edit_window)
        self.edit_btn.grid(column=1, row=0, padx=5, sticky="W")
        self.delete_btn = ctk.CTkButton(self, text="Delete",
                                        width=self.btn_width,
                                        height=self.btn_height,
                                        font=(self.font_family, self.button_font_size),
                                        fg_color="#424242",
                                        hover_color="#D32F2F",
                                        command=self.delete_prompt)
        self.delete_btn.grid(column=3, row=0, padx=(0,10), sticky="E")

    # change current window to review window TODO
    def review_window(self):
        frame = ReviewFrame(self.root, self.flashcard_group)
        self.root.change_frame(frame)
    
    # change current window to edit window TODO
    def edit_window(self):
        frame = EditFrame(self.root)
        self.root.change_frame(frame)

    # a deletion pop up for confirmation TODO
    def delete_prompt(self):
        pass