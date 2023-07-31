# 📌 Создайте модуль с функцией внутри.
# 📌 Функция получает на вход загадку, список с возможными
# вариантами отгадок и количество попыток на угадывание.
# 📌 Программа возвращает номер попытки, с которой была')
# отгадана загадка или ноль, если попытки исчерпаны.

from random import randint
from typing import List, Dict

__all__ = ['game_guess_two']

def game_guess_two(riddle_namber: int,
                   variants: List[int],
                   number_of_attempts: int) -> int:

    for attempt_number in range(1, number_of_attempts+1):
        rnd_namber: int = randint(0, len(variants)-1)
        if riddle_namber == variants[rnd_namber]:
            return attempt_number
    return 0


VAR_DICT: Dict = {1: [1, 2, 3, 4], 3: [2, 3, 4, 5]}

_res: Dict = {}


def all_var():
    for key, value in VAR_DICT.items():
        _res[str(value)] = game_guess_two(riddle_namber=key,
                                          variants=value,
                                          number_of_attempts=10)

        print(_res[str(value)])


if __name__ == "__main__":
    all_var()
    print(_res)
