from turtle import st
import customtkinter as ctk

from flashcard import Flashcard, FlashcardGroup
from database import db
from card_edit_popup import open_popup_create, open_popup_edit

class EditFrame(ctk.CTkFrame):
    def __init__(self, master, flascardGroupID: int, parent):
        super().__init__(master)

        self.root = master
        self.groupID = flascardGroupID
        self.parent = parent

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=9)
        self.grid_columnconfigure(0, weight=1)

        # query cards items from db
        self.groupItems = db.getCards(self.groupID)
        self.groupInfo: FlashcardGroup = db.getGroupInfo(self.groupID)

        self.col2 = FlashcardScrollWidget(self, self.groupItems)
        self.col2.configure(fg_color="transparent")
        self.col2.grid(column=0, row=1, sticky="nsew")
        self.col2.load_cards()

        # nav bar includes:
        # Back button, group name (editable), insert new card button 
        self.topMenuBar = ctk.CTkFrame(self)
        self.topMenuBar.grid(column=0, row=0, sticky="nsew")
        self.topMenuBar.grid_rowconfigure(0, weight=1)
        self.topMenuBar.grid_columnconfigure(0, weight=1)
        self.topMenuBar.grid_columnconfigure(1, weight=1)
        self.topMenuBar.grid_columnconfigure(2, weight=10)
        self.topMenuBar.grid_columnconfigure(3, weight=2)

        button_width = 100  # Set a uniform width for buttons

        self.back_button = ctk.CTkButton(self.topMenuBar, text='Back', width=button_width, command=self.cancel_btn)
        self.back_button.grid(column=0, row=0)

        self.title_label = ctk.CTkLabel(self.topMenuBar, text="Group Name")
        self.title_label.grid(column=1, row=0) 

        self.title_textbox = ctk.CTkTextbox(self.topMenuBar, height=25, wrap="none", activate_scrollbars=False)
        self.title_textbox.insert("0.0", self.groupInfo.title)
        self.title_textbox.bind("<Return>", self.update_groupName)  # Bind Enter key to a function
        self.title_textbox.grid(column=2, row=0, padx=10, pady=10, sticky="ew")

        self.insert_card_button = ctk.CTkButton(self.topMenuBar, text='Insert Card', width=button_width, command=self.create_card)
        self.insert_card_button.grid(column=3, row=0)

    def update_groupName(self, event=None):
        new_title = self.title_textbox.get("0.0", "end").strip()
        db.updateGroupInfo(self.groupID, new_title)
        self.parent.title_label.configure(text=new_title)
        return "break"

    def create_card(self):
        open_popup_create(self, self.groupID)

    def cancel_btn(self):
        self.root.load_main()


# scrollbar widget for individual cards
class FlashcardScrollWidget(ctk.CTkScrollableFrame):
    def __init__(self, master, card_list):
        super().__init__(master)
        self.items = card_list

    def load_cards(self):
        if self.items != None:
            for card in self.items:
                item = FlashcardCardFrame(self, card)
                item.pack(fill="x", pady=5, padx=1)

    def add_card(self, card):
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
        # self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=50)
        self.grid_columnconfigure(3, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # trim text here since it might become too long
        self.title_label = ctk.CTkLabel(self, font=(self.font_family, (self.title_font_size) - 1),
                                        text=self.flashcard_card_info.front,
                                        text_color="white",
                                        wraplength=500)
        self.title_label.grid(column=2, row=0, padx=20, pady=10)

        self.edit_btn = ctk.CTkButton(self, text="Edit",
                                        width=self.btn_width,
                                        height=self.btn_height,
                                        font=(self.font_family, self.button_font_size),
                                        command=self.edit_card)
        self.edit_btn.grid(column=1, row=0, padx=10, pady=10, sticky="W")

        self.delete_btn = ctk.CTkButton(self, text="Delete",
                                        width=self.btn_width,
                                        height=self.btn_height,
                                        font=(self.font_family, self.button_font_size),
                                        fg_color="#424242",
                                        hover_color="#D32F2F",
                                        command=self.delete_card)
        self.delete_btn.grid(column=3, row=0, padx=10, pady=10, sticky="E")

    def edit_card(self):
        card = self.flashcard_card_info
        open_popup_edit(self, card)

    def update_card_info(self, updatedCard):
        self.flashcard_card_info = updatedCard
        self.title_label.configure(text=updatedCard.front)

    def delete_card(self):
        card = self.flashcard_card_info
        db.deleteCard(card.id)
        self.destroy()

