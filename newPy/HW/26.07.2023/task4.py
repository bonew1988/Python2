from typing import Dict, Set


def find_common_items(friends_items: Dict[str, Set[str]]) -> Set[str]:
    common_items = set.intersection(*friends_items.values())
    return common_items


def find_unique_items(friends_items: Dict[str, Set[str]]) -> Set[str]:
    all_items = set.union(*friends_items.values())
    item_counts = {item: sum(
        item in items for items in friends_items.values()) for item in all_items}
    unique_items = {item for item, count in item_counts.items() if count == 1}
    return unique_items


friends_items = {
    "Друг 1": {"топор", "палатка", "фонарик", "кружка", "ложка", "удочка"},
    "Друг 2": {"плащ", "спальник", "фонарик", "котелок", "ложка", "кружка", "удочка"},
    "Друг 3": {"тент", "спальник", "фонарик", "кружка", "лопата", "ложка"},
}

common_items = find_common_items(friends_items)
unique_items = find_unique_items(friends_items)

print("Вещи, которые взяли все друзья:", common_items)
print("Уникальные вещи:", unique_items)
