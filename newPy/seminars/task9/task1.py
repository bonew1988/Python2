# Создайте функцию-замыкание, которая запрашивает два целых
# числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток.

from random import randint


def game(num2guess: int, tryes: int):
    def guessing_game():
        for _ in range(tryes):
            if num2guess == int(input('введите число: ')):
                return True
        return False
    return guessing_game


def gaming(func):
    def wrapper(num2guess: int, tryes: int):
        if 100 >= num2guess >= 1:
            num2guess = randint(100, 1)
        if 100 >= tryes >= 1:
            tryes = randint(1, 10)
        return func(num2guess, tryes)
    return wrapper


@gaming
def guess_num(num2guess: int, tryes: int):
    for _ in range(tryes):
        if num2guess == int(input('введите число: ')):
            return True
    return False


if __name__ == '__main__':
    print(guess_num(101, 11))
