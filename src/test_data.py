from flashcard import Flashcard, FlashcardGroup
from typing import List

print("--- YOU ARE USING TESTING DATA ---")
print("--- YOU ARE USING TESTING DATA ---")
print("--- YOU ARE USING TESTING DATA ---\n")

# Generate a list of FlashcardGroup data
def generate_test_data(group_count: int, card_count: int = 10) -> List[FlashcardGroup]:
    group_list = []

    for i in range(1, group_count + 1):
        card_list = []
        for j in range(1, card_count + 1):
            card_list.append(Flashcard(j, f"Group {i}: flashcard {j}", f"answer {j}"))
        group = FlashcardGroup(i,f"Title: Group {i} Math or Something", f"short description for group {i}", card_list)
        group_list.append(group)

    return group_list
