# Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая” и т.п.
# Преобразуйте его в дату в текущем году. Логируйте ошибки, если текст не соответсвует формату.
import datetime
from datetime import date, timedelta
import logging
from functools import wraps
import argparse

logging.basicConfig(filename="log_for_tast2.log",
                    encoding='utf-8',
                    level=logging.ERROR,
                    filemode='a')

logger = logging.getLogger(__name__)


def deco(func: callable):

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as message_errors:
            logger.error(f'Функция {func.__name__} '
                         f'с аргументами {args = }, '
                         f'{kwargs =} выдвала ошибку: '
                         f'{message_errors = }')
            return None
    return wrapper


MONTHS = ('   ', 'янв', 'фев', 'мар', 'апр', 'мая',
          'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек')
WEEKDAYS = ('пон', 'вто', 'сре', 'чет', 'пят', 'суб', 'вос')


@deco
def creat_data(strig: str):
    data = date.today().year
    day_, week_, month_ = strig.split()
    day_ = int(day_[0])
    week_ = WEEKDAYS.index(week_[:3])
    month_ = MONTHS.index(month_[:3])

    start_data = date(year=data, month=month_, day=1)
    count = 0
    for _ in range(32):
        if start_data.weekday() == week_:
            count += 1
            if day_ == count:
                return start_data
        start_data += timedelta(days=1)
    raise ValueError


def pars():
    parser = argparse.ArgumentParser(description='My first argument parser')
    parser.add_argument('-d', '--day', type=str)
    parser.add_argument('-w', '--weekday', type=str)
    parser.add_argument('-m', '--month', type=str)
    args = parser.parse_args()
    return creat_data(f'{args.day} {args.weekday} {args.month}')


if __name__ == '__main__':
    # text = '3-я среда мая'
    # print(creat_data(text))
    print(pars())
