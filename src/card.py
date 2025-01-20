from typing import List

# STRUCTURE OF FLASHCARDS
# unique id - for database integration
# question  - question for the flashcard
# answer    - answer for the flashcard
# bucket    - different buckets have different intervals of showing when reviewing cards (0,1,2)
# buffer    - will dictate whether to move up or down a bucket
class Flashcard:
    def __init__(self, id: int, question: str, answer: str, bucket: int, buffer_count: int):
        self.__id: int = id
        self.__question: str = question
        self.__answer: str = answer
        self.bucket: int = bucket
        self.buffer_count: int = buffer_count

    def __repr__(self):
        return f"(id={self.__id}, question={self.__question}, answer={self.__answer}, bucket={self.bucket}, buffer={self.buffer_count})"

    @property
    def id(self):
        return self.__id
    @property
    def question(self):
        return self.__question
    @property
    def answer(self):
        return self.__answer

    # setters
    def set_id(self, new_id:int):
        self.__id = new_id
    def set_question(self, new_question: str):
        self.__question = new_question
    def set_answer(self, new_answer: str):
        self.__question = new_answer


# will hold groups of flashcards
class FlashcardGroup:
    def __init__(self, group_id: int,group_name: str, description: str, flashcard_list: List[Flashcard]):
        self.group_id: int = group_id
        self.title: str = group_name
        self.description: str = description

        self.items: List[Flashcard] = flashcard_list
        self.bucket_0: List[Flashcard] = []
        self.bucket_1: List[Flashcard] = []
        self.bucket_2: List[Flashcard] = []

        # Load cards into their respective buckets
        for card in self.items:
            match card.bucket:
                case 0:
                    self.bucket_0.append(card)
                case 1:
                    self.bucket_1.append(card)
                case 2:
                    self.bucket_2.append(card)
                case _:
                    print(f"Invalid Bucket: {card.bucket}")
