from pydoc import text
from turtle import width
import customtkinter as ctk

class ReviewFrame(ctk.CTkFrame):
    def __init__(self, master, group):
        super().__init__(master)

        self.flashcard_group = group
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=4)
        self.grid_rowconfigure(2, weight=2)
        self.btn_height=50
        self.btn_width=150

        self.middle_widget = self.create_middle_widget()
        self.top_menu_frame = self.create_top_menu()
        self.bottom_menu_frame = self.create_bottom_menu()

    # creates the flashcard widget
    def create_middle_widget(self):
        middle_widget = ctk.CTkButton(self, width=650, height=400, command=self.flip, text="Flashcard Content",
                                  corner_radius=20)
        middle_widget.grid(column=0, row=1, padx=0, pady=0)
        return middle_widget

    # creates top menu bar
    def create_top_menu(self):
        top_menu_frame = ctk.CTkFrame(self)
        top_menu_frame.grid(row=0, sticky="new")
        top_menu_frame.grid_rowconfigure(0, weight=1)
        back_button = ctk.CTkButton(top_menu_frame, text="Back", command=self.back_btn_pressed)
        back_button.configure(text="Back", width=100)
        back_button.grid(row=0, sticky="w", padx=20, pady=10)
        return top_menu_frame

    # creates bottom menu bar
    def create_bottom_menu(self):
        padding_y=25

        menu_frame = ctk.CTkFrame(self)
        menu_frame.grid(row=2, sticky="sew")
        menu_frame.grid_rowconfigure(0, weight=1)
        menu_frame.grid_columnconfigure(0, weight=1)
        menu_frame.grid_columnconfigure(1, weight=1)
        wrong_button = ctk.CTkButton(menu_frame,
                                          height=self.btn_height, 
                                          width=self.btn_width,
                                          text="Wrong",
                                          command=self.wrong_btn_pressed)
        wrong_button.grid(column=0, row=0, padx=(200,0), pady=padding_y)
        correct_button = ctk.CTkButton(menu_frame,
                                            height=self.btn_height,
                                            width=self.btn_width, 
                                            text="Correct",
                                            command=self.correct_btn_pressed)
        correct_button.grid(column=1, row=0, padx=(0, 200), pady=padding_y)
        return menu_frame

    # initialize the review data for review
    def init_review(self):
        pass

    # flip the flashcard
    def flip(self):
        pass
        #TODO

    def correct_btn_pressed(self):
        pass
        #TODO

    def wrong_btn_pressed(self):
        pass
        #TODO

    def back_btn_pressed(self):
        pass