import logging

# Настройка логирования в файл
logging.basicConfig(filename='error_log.txt', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s: %(message)s')

try:
    # Попытка деления на ноль
    result = 10 / 0
except ZeroDivisionError as e:
    # Логирование ошибки деления на ноль
    logging.error(f'Error occurred: {e}')

print('Программа завершила выполнение')
