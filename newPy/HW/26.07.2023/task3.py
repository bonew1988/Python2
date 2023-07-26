# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.


from itertools import permutations

MAX_WEIGHT = 10
ITEMS = {
    'Лопата': 4,
    'Фонарь': 1,
    'Вода': 1,
    'Еда': 2,
    'Палатка': 5,
    'Топор': 2,
    'Мангал': 3,
}


def get_availaible_weght(items_set: set([str])) -> float:
    availaible = MAX_WEIGHT
    for i in items_set:
        availaible -= ITEMS[i]
        return availaible


res = set()
current_w_availaible = MAX_WEIGHT
permut_items = permutations(ITEMS.items())

for item_var in permut_items:
    current_w_availaible = MAX_WEIGHT
    temp = set()
    for item, weight in item_var:
        if weight <= current_w_availaible:
            temp.add(item)
            current_w_availaible -= weight
    res.add(tuple(temp))

most_effective_list = []
for item in res:
    current_space = get_availaible_weght(item)
    print(f'{item}, доступно {current_space}')
    most_effective_list.append((item, current_space))

print()
print('самые удачные варианты:')
most_effective = min(most_effective_list, key=lambda x: x[1])
most_effective_list = list(
    filter(lambda x: x[1] == most_effective[1], most_effective_list))
for value in most_effective_list:
    print(value)
