# import logging

# # Настройка логирования в файл
# logging.basicConfig(filename='error_log.txt', level=logging.ERROR,
#                     format='%(asctime)s - %(levelname)s: %(message)s')

# try:
#     # Попытка деления на ноль
#     result = 10 / 0
# except ZeroDivisionError as e:
#     # Логирование ошибки деления на ноль
#     logging.error(f'Error occurred: {e}')

# print('Программа завершила выполнение')


# Задание №1
# Напишите программу, которая использует модуль logging для
# вывода сообщения об ошибке в файл.
# Например отлавливаем ошибку деления на ноль.

import logging

logging.basicConfig(filename="log.log",
                    encoding='utf-8',
                    level=logging.ERROR)

logger = logging.getLogger(__name__)


def div(a, b):
    try:
        res = a/b
        return res
    except ZeroDivisionError:
        logger.error(f'b = {b}')
        # return None


if __name__ == '__main__':
    div(1, 0)
