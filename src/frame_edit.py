import customtkinter as ctk

from flashcard import Flashcard, FlashcardGroup

class EditFrame(ctk.CTkFrame):
    def __init__(self, master, group_info):
        super().__init__(master)

        self.root = master
        self.flashcard_group_info: FlashcardGroup = group_info

        self.grid_columnconfigure(0, weight = 1)
        self.grid_columnconfigure(1, weight = 5)
        self.grid_rowconfigure(0, weight = 1)

        self.col1 = self.create_col_1()
        self.col1.grid(column=0, row=0, sticky="nsew")

        self.col2 = FlashcardScrollWidget(self, self.flashcard_group_info.items)
        self.col2.grid(column=1, row=0, sticky="nsew")
        self.col2.load_groups()

    def create_col_1(self):
        heading_size = 14
        btn_height = 35

        # Layout
        col1 = ctk.CTkFrame(self)
        col1.grid_rowconfigure(0, weight=0)
        col1.grid_rowconfigure(1, weight=0)
        col1.grid_rowconfigure(2, weight=0)
        col1.grid_rowconfigure(3, weight=1)
        col1.grid_columnconfigure(0, weight=1)

        # Group Title
        self.lbl_group_title = ctk.CTkLabel(col1, text="Group Title")
        self.lbl_group_title.grid(row=0, column=0, sticky='ew', padx=10, pady=(5,2))
        self.lbl_group_title.configure(font=("", heading_size))

        self.group_title = ctk.CTkTextbox(col1, height=10)
        self.group_title.insert("0.0", self.flashcard_group_info.title)
        self.group_title.grid(row=1, column=0, sticky='ew', padx=10)
        self.group_title.bind('<Return>', lambda event: 'break')
        self.group_title.bind('<Tab>', lambda event: 'break')

        # Save/Cancel Button
        # Saving all edited configurations
        buttons = ctk.CTkFrame(col1, fg_color="transparent")
        buttons.grid(row=2, sticky="ew", padx=10, pady=2)
        buttons.grid_columnconfigure(0, weight=3)
        buttons.grid_columnconfigure(1, weight=1)
        buttons.grid_columnconfigure(2, weight=3)
        buttons.grid_rowconfigure(0, weight=0)

        save_btn = ctk.CTkButton(buttons, text="Save Changes", height=btn_height, command=self.save_btn)
        cancel_btn = ctk.CTkButton(buttons, text="Cancel", height=btn_height, command=self.cancel_btn)
        save_btn.grid(column=0, row=0, pady=10, sticky="ew")
        cancel_btn.grid(column=2, row=0, sticky="ew")

        # Edit fields
        # Fields for editing individual flashcards
        edit = ctk.CTkFrame(col1)
        edit.grid(row=3, sticky="nswe", padx=10, pady=10)

        edit.grid_rowconfigure(0, weight=1)
        edit.grid_rowconfigure(1, weight=1)
        edit.grid_rowconfigure(2, weight=1)
        edit.grid_rowconfigure(3, weight=1)
        edit.grid_rowconfigure(4, weight=1)
        edit.grid_rowconfigure(5, weight=1)
        edit.grid_rowconfigure(6, weight=1)
        edit.grid_columnconfigure(0, weight=1)

        self.editSelectedCardID = ctk.CTkLabel(edit, text="CARD ID: NO CARD SELECTED")
        self.editCardFront = ctk.CTkLabel(edit, text="Edit Card Front")
        self.editCardFrontTextBox = ctk.CTkTextbox(edit)
        self.editCardBack = ctk.CTkLabel(edit, text="Edit Card Back")
        self.editCardBackTextBox = ctk.CTkTextbox(edit)
        self.clearButton = ctk.CTkButton(edit, text="Clear", command=self.clear_btn)
        self.confirmButton = ctk.CTkButton(edit, text="Confirm Edit", command=self.confirm_btn)
        
        self.editSelectedCardID.grid(column=0, row=0, sticky="we")
        self.editCardFront.grid(column=0, row=1, sticky="w")
        self.editCardFrontTextBox.grid(column=0, row=2, sticky="ew")
        self.editCardBack.grid(column=0, row=3, sticky="w")
        self.editCardBackTextBox.grid(column=0, row=4, sticky="ew")

        self.clearButton.grid(column=0, row=5)
        self.confirmButton.grid(column=0, row=6)

        return col1

    def save_btn(self):
        # TODO 
        print("Saving")
        self.root.load_main()

    def cancel_btn(self):
        self.root.load_main()

    def clear_btn(self):
        self.editSelectedCardID.configure(text="Selected Card ID: Cleared")
        self.editCardFrontTextBox.delete("0.0", "end")
        self.editCardBackTextBox.delete("0.0", "end")
        print("Clear")

    def confirm_btn(self):
        pass


# scrollbar widget for individual cards
class FlashcardScrollWidget(ctk.CTkScrollableFrame):
    def __init__(self, master, card_list):
        super().__init__(master)
        self.items = card_list

    def load_groups(self):
        for card in self.items:
            item = FlashcardCardFrame(self, card)
            item.pack(fill="x", pady=5, padx=1)


class FlashcardCardFrame(ctk.CTkFrame):
    def __init__(self, master, card):
        super().__init__(master)

        # members
        self.flashcard_card_info: Flashcard = card 
        self.configure(fg_color="#1E1E1E")

        # design config
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

        print(self.flashcard_card_info.front)

        self.title_label = ctk.CTkLabel(self, font=(self.font_family, self.title_font_size),
                                        text=self.flashcard_card_info.front,
                                        text_color="white",
                                        wraplength=500)
        self.title_label.grid(column=2, row=0, padx=20, sticky="w")

        self.review_btn = ctk.CTkButton(self, text="Review",
                                        width=self.btn_width, height=self.btn_height,
                                        font=(self.font_family, self.button_font_size))
        self.review_btn.grid(column=0, row=0, padx=(17,0), pady=15, sticky="W")

        self.edit_btn = ctk.CTkButton(self, text="Manage",
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
