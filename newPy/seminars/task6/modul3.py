# Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.

__all__ = ['valid_day']

# проверка на високосность


def is_leap(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# проверка существования дня


def valid_day(date: str) -> bool:
    try:
        day, month, year = map(int, date.split('.'))
        if 1 <= month <= 12 and 1 <= day <= 31 and 1 <= year <= 9999:
            days_in_month = [
                31, 28 + is_leap(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            return day <= days_in_month[month - 1]
        else:
            return False
    except ValueError:
        return False


if __name__ == '__main__':
    print(valid_day('31.03.2023'))
    print(valid_day('31.13.2023'))
