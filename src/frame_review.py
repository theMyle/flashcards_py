import customtkinter as ctk

class ReviewFrame(ctk.CTkFrame):
    def __init__(self, master, group):
        super().__init__(master)

        self.flashcard_group = group
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=2)
        self.grid_rowconfigure(1, weight=1)
        self.btn_height=50
        self.btn_width=150

        # flashcard that flips
        self.card = ctk.CTkButton(self, width=650, height=400, command=self.flip)
        self.card.grid(column=0, row=0, padx=0, pady=0)

        # buttons/menu frame
        self.menu_frame = ctk.CTkFrame(self)
        self.menu_frame.grid(row=1, sticky="nsew")
        self.menu_frame.grid_rowconfigure(0, weight=1)
        self.menu_frame.grid_columnconfigure(0, weight=1)
        self.menu_frame.grid_columnconfigure(1, weight=1)
        self.wrong_button = ctk.CTkButton(self.menu_frame,
                                          height=self.btn_height, 
                                          width=self.btn_width,
                                          text="Wrong",
                                          command=self.wrong_btn_pressed)
        self.wrong_button.grid(column=0, row=0, padx=(200,0))
        self.correct_button = ctk.CTkButton(self.menu_frame,
                                            height=self.btn_height,
                                            width=self.btn_width, 
                                            text="Correct",
                                            command=self.correct_btn_pressed)
        self.correct_button.grid(column=1, row=0, padx=(0, 200))

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