# Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых чисел и их факториалов.

# Задание №2
# Доработаем задачу 1.
# Создайте менеджер контекста, который при выходе
# сохраняет значения в JSON файл.


import json


class Factorial:

    def __init__(self, k):
        self.k = k

        self.values = []

    def __call__(self, num):
        res = 1
        for i in range(1, num + 1):
            res *= i
        if len(self.values) >= self.k:
            self.values.pop(0)
        self.values.append({num: res})
        return res

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open(r'/home/bonew/Рабочий стол/newPY/Python2/newPy/zoo.json', 'w', encoding='utf-8') as f:
            json.dump(self.values, f)


if __name__ == '__main__':

    f = Factorial(4)
    # print(f(5))
    # print(f(6))
    # print(f(7))
    # print(f(8))
    # print(f(9))
    # print(f(10))
    print(f.values)
    with f as copy_:
        print(copy_(3))
        print(copy_(4))
        print(copy_(5))
        print(copy_(6))
        print(copy_(7))
        print(copy_(8))
