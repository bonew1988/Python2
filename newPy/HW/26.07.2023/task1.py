# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов. [1, 2, 3, 1, 2, 4, 5] -> [1, 2]

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5]
result = []
UNIQUE_COUNT = 1
for i in data:
    if i not in result and data.count(i) > UNIQUE_COUNT:
        result.append(i)
print(f'{data} -> {result}')
