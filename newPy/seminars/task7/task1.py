# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции.

from random import uniform, randint


def generate_random_file(file: str, lines: int) -> None:
    file += '.txt'
    with open(file, 'a', encoding='UTF-8') as f:
        for _ in range(lines):
            f.write(f'{randint(-1000, 1000)} | {uniform(-1000, 1000)} \n')


if __name__ == '__main__':
    generate_random_file('testfile1', 5)
