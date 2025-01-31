import customtkinter as ctk

from card import Flashcard, FlashcardGroup

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

        # self.col2 = FlashcardGroupScrollWidget()
        # self.col2.grid(column=1, row=0)

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
        self.lbl_group_title.grid(row=0, column=0, sticky='new', padx=10, pady=(10,2))
        self.lbl_group_title.configure(font=("", heading_size))

        self.group_title = ctk.CTkTextbox(col1, height=10)
        self.group_title.insert("0.0", self.flashcard_group_info.title)
        self.group_title.grid(row=1, column=0, sticky='ew', padx=10)
        self.group_title.bind('<Return>', lambda event: 'break')
        self.group_title.bind('<Tab>', lambda event: 'break')

        # Save/Cancel Button
        buttons = ctk.CTkFrame(col1)
        buttons.grid(row=2, sticky="ew", padx=10, pady=10)

        buttons.grid_columnconfigure(0, weight=1)
        buttons.grid_columnconfigure(1, weight=1)
        buttons.grid_rowconfigure(0, weight=0)

        save_btn = ctk.CTkButton(buttons, text="Save", height=btn_height, command=self.save_btn)
        cancel_btn = ctk.CTkButton(buttons, text="Cancel", height=btn_height, command=self.cancel_btn)
        save_btn.grid(column=0, row=0, pady=10)
        cancel_btn.grid(column=1, row=0)

        # Edit fields
        edit = ctk.CTkFrame(col1)
        edit.grid(row=3, sticky="nswe", padx=10, pady=(0, 10))

        return col1
    
    def save_btn(self):
        print("Saving")
        pass

    def cancel_btn(self):
        self.root.load_main()
