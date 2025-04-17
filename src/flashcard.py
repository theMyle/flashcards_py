from typing import List

# STRUCTURE OF FLASHCARDS
# unique id - for database integration
# question  - question for the flashcard
# answer    - answer for the flashcard
# bucket    - different buckets have different intervals of showing when reviewing cards (0,1,2)
# buffer    - will dictate whether to move up or down a bucket
class Flashcard:
    def __init__(self, id: int, front: str, back: str):
        self.__id: int = id
        self.__front: str = front
        self.__back: str = back
        # self.bucket: int = bucket
        # self.buffer_count: int = buffer_count

    def __repr__(self):
        return f"(id={self.__id}, front={self.__front}, back={self.__back})"

    @property
    def id(self):
        return self.__id
    @property
    def front(self):
        return self.__front
    @property
    def back(self):
        return self.__back

    # setters
    def set_id(self, newId:int):
        self.__id = newId
    def set_front(self, newFront: str):
        self.__front = newFront
    def set_back(self, newBack: str):
        self.__back= newBack


# will hold groups of flashcards
class FlashcardGroup:
    def __init__(self, group_id: int,group_name: str):
        self.group_id: int = group_id
        self.title: str = group_name

        """
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
        """
