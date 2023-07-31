# -----------------------------------------------------------------------------------

# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

from random import randint
from sys import argv

__all__ = ['game']


def game(start: int = 0, end: int = 1000, trues: int = 5) -> bool:
    num = randint(start, end)
    for _ in range(trues):
        enter = int(input('enter num: '))
        if num > enter:
            print('больше')
        elif num < enter:
            print('меньше')
        else:
            break
    return enter == num


if __name__ == '__main__':
    arguments = map(int, argv[1:])
    print(game(*arguments))
