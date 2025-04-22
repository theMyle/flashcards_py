import customtkinter as ctk
from typing import List

from flashcard import FlashcardGroup
from frame_edit import EditFrame
from frame_review import ReviewFrame
from database import db
from card_edit_popup import show_error_popup

# Main window for the application
# The first window to interact with
class MainFrame(ctk.CTkFrame):
    def __init__(self, master, root):
        super().__init__(master)

        self.parent = master

        # I prolly should decouple business logic and my UI config!!!
        self.grid_columnconfigure(0, weight = 1)
        self.grid_rowconfigure(0, weight = 1)
        self.grid_rowconfigure(1, weight = 10)

        # Menu widgets
        self.menu = ctk.CTkFrame(self)
        self.menu.grid(column=0, row=0, sticky="nsew")
        self.menu.grid_columnconfigure(0, weight=1)
        self.menu.grid_columnconfigure(1, weight=11)
        self.menu.grid_columnconfigure(2, weight=1)
        self.menu.grid_rowconfigure(0, weight=1)

        self.menu.search_lbl = ctk.CTkLabel(self.menu, text="Search")
        self.menu.search_bar = ctk.CTkTextbox(self.menu, height=25, wrap="none", activate_scrollbars=False)
        self.menu.create_btn = ctk.CTkButton(self.menu, 
                                             text="Create New", 
                                             width=100, 
                                             height=30,
                                             command=self.create_new_set)

        self.menu.search_lbl.grid(column=0, row=0)
        self.menu.search_bar.grid(column=1, row=0, sticky="ew")
        self.menu.search_bar.bind("<Key>", self.search_event_handler)
        self.menu.create_btn.grid(column=2, row=0)

        # Flashcards Group List
        self.groupList = FlashcardGroupScrollWidget(self, root, db.getGroups())
        self.groupList.configure(fg_color="transparent")
        self.groupList.grid(column = 0, row = 1, sticky="nsew")
        self.groupList.load_groups()


    # creates a new set, inserts to database and updates the UI too
    def create_new_set(self):
        dialog = ctk.CTkInputDialog(text="Enter Group Name", title="Create New Flashcard Group")
        sw = dialog.winfo_screenwidth()
        sh = dialog.winfo_screenheight()

        w = dialog.winfo_width()
        h = dialog.winfo_height()

        dialog.geometry(f"+{(sw - w) // 2}+{(sh-h) // 2}")

        groupName = dialog.get_input()
        if groupName == "":
            show_error_popup(self, "Group name cannot be empty!")
            return 
        elif groupName == None:
            return
        else:
            groupName.strip()

        groupID = db.insertGroup(groupName)
        self.groupList.insert_group(groupName, groupID)


    # No time to implement this shit yet
    def search_event_handler(self, event):
        text = self.menu.search_bar.get("0.0", "end").strip()

        if event.keysym == "Return":
            print(f"Todo Search: {text}")
            return "break"

        elif event.keysym == "BackSpace":
            print(f"Character deleted")

        elif event.keysym == "Escape":
            print("Clear")


# scrollbar widget for flashcard groups
# a scrollbar container since it is required if I want scrollbar
class FlashcardGroupScrollWidget(ctk.CTkScrollableFrame):
    def __init__(self, master, root, group_list: List[FlashcardGroup]):
        super().__init__(master)

        self.root = root
        self.items = group_list

    def load_groups(self):
        if self.items != None:
            for item in self.items:
                item = FlashcardGroupFrame(self, self.root, item.title, item.group_id)
                item.pack(fill="x", pady=5, padx=1)

    def insert_group(self, group_name, group_ID):
        """Inserts a new group into the UI"""
        item = FlashcardGroupFrame(self, self.root, group_name, group_ID)
        item.pack(fill="x", pady=5, padx=1)


# Widget for flashcard group holding the buttons, title and others group information
# The individual groups frame with buttons each
class FlashcardGroupFrame(ctk.CTkFrame):
    def __init__(self, master, root, group_name, group_id):
        super().__init__(master)

        # members
        self.root = root
        self.group_name = group_name
        self.group_id = group_id
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

        self.title_label = ctk.CTkLabel(self, font=(self.font_family, self.title_font_size),
                                        text=self.group_name,
                                        text_color="white",
                                        wraplength=500)
        self.title_label.grid(column=2, row=0, padx=20, sticky="w")

        self.review_btn = ctk.CTkButton(self, text="Review",
                                        width=self.btn_width, height=self.btn_height,
                                        font=(self.font_family, self.button_font_size),
                                        command=self.review_window)
        self.review_btn.grid(column=0, row=0, padx=(17,0), pady=15, sticky="W")

        self.edit_btn = ctk.CTkButton(self, text="Manage Cards",
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

    # I should let all of these function manage the database instead of supplying them 
    # all the same data for easy refactorting down the line

    # change current window to review window 
    def review_window(self):
        frame = ReviewFrame(self.root, self.group_id)
        self.root.change_frame(frame)

    # change current window to edit window 
    def edit_window(self):
        frame = EditFrame(self.root, self.group_id, self)
        self.root.change_frame(frame)

    # a deletion pop up for confirmation
    def delete_prompt(self):

        # Create a prompt here for delete confirmation
        # TODO!

        db.deleteGroup(self.group_id)
        self.destroy()

