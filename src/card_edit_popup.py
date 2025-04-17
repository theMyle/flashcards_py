from typing import Optional
import customtkinter as ctk
from flashcard import Flashcard
from database import db

def show_error_popup(parent, message):
    """Displays an error popup with the given message."""
    error_popup = ctk.CTkToplevel(parent)
    error_popup.title("Error")
    error_popup.geometry("300x150")
    error_popup.resizable(False, False)

    # Add a label to display the error message
    error_label = ctk.CTkLabel(error_popup, text=message, font=("Arial", 14), wraplength=280)
    error_label.pack(pady=20)

    # Add an OK button to close the popup
    ok_button = ctk.CTkButton(error_popup, text="OK", command=error_popup.destroy)
    ok_button.pack(pady=10)

    # Make the popup modal
    error_popup.grab_set()


class PopupWindow(ctk.CTkToplevel):
    def __init__(self, parent, operation, cardInfo: Optional[Flashcard], groupID):
        super().__init__(parent)

        self.groupID = groupID
        self.parent = parent
        self.operation = operation

        self.cardInfo: Flashcard
        if cardInfo is not None:
            self.cardInfo = cardInfo

        self.geometry("640x500+200+60")
        self.resizable(False, False)

        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure((0, 2), weight=1)
        self.grid_rowconfigure(1, weight=5)

        # Card front and back textboxes
        self.card_front_label = ctk.CTkLabel(self, text="Front", font=('Arial', 14))
        self.card_front = ctk.CTkTextbox(self, wrap="word", font=('Arial', 16))

        self.card_back_label = ctk.CTkLabel(self, text="Back", font=('Arial', 14))
        self.card_back = ctk.CTkTextbox(self, wrap="word", font=('Arial', 16))

        if operation == 'edit':
            self.card_front.insert("end", self.cardInfo.front)
            self.card_back.insert("end", self.cardInfo.back)
            self.title("Edit Card")
        else:
            self.title("New Card")

        # Place labels and textboxes in two columns
        self.card_front_label.grid(column=0, row=0, padx=10, pady=5, sticky="we")
        self.card_front.grid(column=0, row=1, padx=10, pady=5, sticky="nsew")

        self.card_back_label.grid(column=1, row=0, padx=10, pady=5, sticky="we")
        self.card_back.grid(column=1, row=1, padx=10, pady=5, sticky="nsew")

        # Buttons
        self.btn_save = ctk.CTkButton(self, text="Save", command=self.save)
        self.btn_back = ctk.CTkButton(self, text="Back", command=self.back)

        # Place buttons below the textboxes
        self.btn_save.grid(column=0, row=2, padx=10, pady=10, sticky="ew")
        self.btn_back.grid(column=1, row=2, padx=10, pady=10, sticky="ew")

    # Save button
    def save(self):
        new_front = self.card_front.get("1.0", "end-1c")
        new_back = self.card_back.get("1.0", "end-1c")

        # Add check here, front or back must not be empty
        if not new_front or not new_back:
            show_error_popup(self, "Both the front and back of the card must be filled!")
            return

        if self.operation == 'create':
            card = Flashcard(self.groupID, new_front, new_back)
            db.insertCard(self.groupID, new_front, new_back)
            self.parent.col2.add_card(card)

            # Clear the inputs
            self.card_front.delete("0.0", "end")
            self.card_back.delete("0.0", "end")

        elif self.operation == 'edit':
            card = Flashcard(self.cardInfo.id, new_front, new_back)
            db.updateCard(card.id, card.front, card.back)
            self.parent.update_card_info(card)

        self.destroy()

    # Back button
    def back(self):
        self.destroy()

def open_popup_create(app, groupID):
    popup = PopupWindow(app, operation='create', groupID=groupID, cardInfo=None)
    popup.grab_set()  # Makes the popup modal (disables main window interaction)

def open_popup_edit(app, cardInfo):
    popup = PopupWindow(app, operation='edit', groupID=None, cardInfo=cardInfo)
    popup.grab_set()  # Makes the popup modal (disables main window interaction)
