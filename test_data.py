from flashcard import Flashcard, FlashcardGroup
from typing import List

print("--- YOU ARE USING TESTING DATA ---")
print("--- YOU ARE USING TESTING DATA ---")
print("--- YOU ARE USING TESTING DATA ---\n")

# Generate a list of FlashcardGroup data
def generate_test_data(group_count: int, item_per_group: int = 10) -> List[FlashcardGroup]:
    group_list: List[FlashcardGroup] = []

    for i in range(1, group_count + 1):
        temp = []
        for j in range(1, item_per_group + 1):
            temp.append(Flashcard(j, f"Group {i}: flashcard {j}", f"answer {j}", 1, 0))
        group = FlashcardGroup(i,f"Title: Group {i} Math or Something", f"short description for group {i}", temp)
        group_list.append(group)

    return group_list
