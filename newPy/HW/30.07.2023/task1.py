# Напишите функцию для транспонирования матрицы. Пример: [[1, 2, 3], [4, 5, 6]] -> [[1,4], [2,5], [3, 6]]
data = [
    [1, 2, 3],
    [4, 5, 6]
]

rows = len(data)
cols = len(data[0])

trans_data = [[0 for _ in range(rows)] for _ in range(cols)]

for i in range(rows):
    for j in range(cols):
        trans_data[j][i] = data[i][j]

print('Исходная матрица: ')
for row in data:
    print(row)
print('Транспонированная матрица: ')
for row in trans_data:
    print(row)
