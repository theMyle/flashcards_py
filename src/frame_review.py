import random
import customtkinter as ctk
import textwrap
from database import db
from flashcard import Flashcard, FlashcardGroup

class ReviewFrame(ctk.CTkFrame):
    def __init__(self, master, groupID):
        super().__init__(master)

        self.root = master
        self.groupID = groupID
        self.group_info: FlashcardGroup = db.getGroupInfo(self.groupID) # type: ignore
        self.flashcard_group: list[Flashcard] = db.getCards(self.groupID) # type: ignore
        random.shuffle(self.flashcard_group)

        # Review states
        self.card_state = 'front' # front | back
        self.review_state = None # review | mistakes | summary

        try:
            self.number_of_cards = len(self.flashcard_group)
        except:
            self.number_of_cards = 0

        self.current_card_count = 1
        self.current_card: Flashcard = None
        self.mistakes_list = []

        self.correct = 0
        self.mistakes = 0
        # Review states

        # UI 
        self.btn_height=50
        self.btn_width=150
        self.btn_fg = "#1e1e2e"
        self.btn_hover = "#1a1a24"

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=2)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=5)
        self.grid_rowconfigure(3, weight=3)

        self.review_progress = self.create_progress_widget()
        self.middle_widget = self.create_middle_widget()
        self.top_menu_frame = self.create_top_menu()
        self.bottom_menu_frame = self.create_bottom_menu()
        # UI

        self.init_review()


    def create_progress_widget(self):
        review_progress = ctk.CTkLabel(self, text="0/0", font=("mono", 18))
        review_progress.grid(column=0, row=1, padx=0, pady=0)
        return review_progress

    # creates the flashcard widget
    def create_middle_widget(self):
        middle_widget = ctk.CTkButton(self, width=650, height=400, 
                                      command=self.flip, 
                                      text="Loading Flashcard Content",
                                      corner_radius=20, 
                                      font=("mono", 20),
                                      fg_color=self.btn_fg,
                                      hover_color=self.btn_hover)

        middle_widget.grid(column=0, row=2, padx=0, pady=0)
        return middle_widget

    # creates top menu bar
    def create_top_menu(self):
        top_menu_frame = ctk.CTkFrame(self)
        top_menu_frame.grid(row=0, sticky="new")
        top_menu_frame.grid_rowconfigure(0, weight=1)

        back_button = ctk.CTkButton(top_menu_frame, text="Back", 
                                    command=self.back_btn_pressed,
                                    fg_color=self.btn_fg,
                                    hover_color=self.btn_hover,
                                    border_color="#3a3a99",
                                    border_width=0.1) # type: ignore

        back_button.configure(text="Back", width=100)
        back_button.grid(row=0, sticky="w", padx=20, pady=10)
        return top_menu_frame

    # creates bottom menu bar
    def create_bottom_menu(self):
        padding_y=25

        menu_frame = ctk.CTkFrame(self)
        menu_frame.grid(row=3, sticky="sew")
        menu_frame.grid_rowconfigure(0, weight=1)
        menu_frame.grid_columnconfigure(0, weight=1)
        menu_frame.grid_columnconfigure(1, weight=1)
        wrong_button = ctk.CTkButton(menu_frame,
                                          height=self.btn_height, 
                                          width=self.btn_width,
                                          text="Wrong",
                                          command=self.wrong_btn_pressed,
                                          fg_color=self.btn_fg,
                                          hover_color=self.btn_hover)
        wrong_button.grid(column=0, row=0, padx=(200,0), pady=padding_y)
        correct_button = ctk.CTkButton(menu_frame,
                                            height=self.btn_height,
                                            width=self.btn_width, 
                                            text="Correct",
                                            command=self.correct_btn_pressed,
                                            fg_color=self.btn_fg,
                                            hover_color=self.btn_hover)
        correct_button.grid(column=1, row=0, padx=(0, 200), pady=padding_y)
        return menu_frame

    # initialize the review data for review
    def init_review(self):
        if self.flashcard_group == None:
            self.middle_widget.configure(text='No flashcards to review, create some.')
            return

        for card in self.flashcard_group:
            front = 'Front\n\n' + self.wrap_text(card.front)
            back = 'Back\n\n' + self.wrap_text(card.back)
            card.set_front(front)
            card.set_back(back)

        self.review_state = "review"
        self.review_progress.configure(text=f"1/{self.number_of_cards}")
        self.current_card = self.flashcard_group.pop(0)
        self.middle_widget.configure(text=self.current_card.front)

    # flip the flashcard
    def flip(self):
        if self.review_state == "summary":
            return

        # do nothing when there is no card
        if self.current_card is None:
            return

        # flip to back
        if self.card_state == 'front':
            self.middle_widget.configure(text=self.current_card.back)
            self.card_state = 'back'
        # flip to front
        else:
            self.middle_widget.configure(text=self.current_card.front)
            self.card_state = 'front'

    def correct_btn_pressed(self):
        # check what state the app is in
        if self.review_state == 'review':
            # when there are no items yet
            if self.flashcard_group is None:
                return

            # when there are no cards left
            if len(self.flashcard_group) == 0:
                # will run once then change state
                self.correct += 1
                if len(self.mistakes_list) > 0:
                    self.review_state = 'mistakes'
                    self.flashcard_group = self.mistakes_list
                    self.current_card_count = 0
                    self.number_of_cards = len(self.mistakes_list)
                    self.review_progress.configure(text=f"Reviewing Mistakes {self.current_card_count}/{self.number_of_cards}")
                    self.update_review()
                else:
                    self.review_state = 'summary'
                    self.review_progress.destroy()
                    self.update_review()
                return

            self.correct += 1
            self.update_review()

        # review the mistakes
        elif self.review_state == 'mistakes':
            if len(self.flashcard_group) == 0:
                self.review_state = 'summary'
                self.review_progress.destroy()
            self.update_review()

    def wrong_btn_pressed(self):
        if self.review_state == 'review':
            if self.flashcard_group is None:
                return

            # when there are no cards left
            if len(self.flashcard_group) == 0:
                # will run once then change state
                self.mistakes += 1
                self.mistakes_list.append(self.current_card)

                if len(self.mistakes_list) > 0:
                    self.review_state = 'mistakes'
                    self.flashcard_group = self.mistakes_list
                    self.current_card_count = 0
                    self.number_of_cards = len(self.mistakes_list)
                    self.review_progress.configure(text=f"Reviewing Mistakes {self.current_card_count}/{self.number_of_cards}")
                    self.update_review()
                else:
                    self.review_state = 'summary'
                    self.review_progress.destroy()
                    self.update_review()
                return

            self.mistakes += 1
            self.mistakes_list.append(self.current_card)
            self.update_review()

        # review the mistakes
        elif self.review_state == 'mistakes':
            if len(self.flashcard_group) == 0:
                self.review_state = 'summary'
                self.review_progress.destroy()
            self.update_review()

    def back_btn_pressed(self):
        self.root.load_main()

    # helper func
    def wrap_text(self, text, line_width=50):
        return "\n".join(textwrap.wrap(text, line_width))

    def update_review(self):
        if self.review_state == 'review':
            self.current_card_count += 1
            self.review_progress.configure(text=f"{self.current_card_count}/{self.number_of_cards}")
            self.current_card = self.flashcard_group.pop(0)
            self.middle_widget.configure(text=self.current_card.front)
            self.card_state = 'front'
            return

        if self.review_state == 'mistakes':
            self.current_card_count += 1
            self.review_progress.configure(text=f"Reviewing Mistakes {self.current_card_count}/{self.number_of_cards}")
            self.current_card = self.flashcard_group.pop(0)
            self.middle_widget.configure(text=self.current_card.front)
            self.card_state = 'front'
            return

        if self.review_state == 'summary':
            self.middle_widget.configure(text=f"Review Summary\n\n✅ Correct: {self.correct}\n❎ Mistakes: {self.mistakes}")
            self.bottom_menu_frame.destroy()
            self.card_state = 'front'
            return

