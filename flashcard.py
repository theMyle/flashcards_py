from typing import List

# unique id - for database integration
# question  - question for the flashcard
# answer    - answer for the flashcard
# bucket    - different buckets have different intervals of showing when reviewing cards
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

# will hold groups of flashcards
class FlashcardGroup:
    def __init__(self, group_id: int,group_name: str, description: str, flashcard_list: List[Flashcard]):
        self.group_id: int = group_id
        self.title: str = group_name
        self.description: str = description
        self.items: List[Flashcard] = flashcard_list
