# Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.

from random import randint

__all__ = ['generate_random_file_names']

def give_namer() -> str:
    name: str = ''
    for _ in range(randint(4, 7)):
        name += chr(randint(98, 122))
    return name.capitalize()


def generate_random_file_names(file: str, lines: int) -> None:
    file += '.txt'
    with open(file, 'a', encoding='UTF-8') as f:
        for _ in range(lines):
            f.write(f'{give_namer()} \n')


if __name__ == '__main__':
    generate_random_file_names('testfile', 5)
