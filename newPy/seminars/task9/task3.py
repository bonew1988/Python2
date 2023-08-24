# Задание №4
# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой
# функции.


def param(count: int):
    def decor(func):
        my_list = []

        def wrapper(*args, **kwargs):
            for i in range(count):
                result = func(*args, **kwargs)
                my_list.append(result)
            return my_list
        return wrapper
    return decor


@param(3)
def sum_digit(a, b):
    return a + b


print(sum_digit(5, 6))
