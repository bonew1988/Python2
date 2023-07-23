# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей.
# Для проверки своего кода используйте модуль fractions.

from fractions import Fraction


def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a


def simplify_fraction(num: int, denom: int) -> tuple:
    greatest_common_divisor = gcd(num, denom)
    return num // greatest_common_divisor, denom // greatest_common_divisor


def add_fractions(fraction1: str, fraction2: str) -> tuple:
    num1, denom1 = map(int, fraction1.split('/'))
    num2, denom2 = map(int, fraction2.split('/'))

    common_denom = denom1 * denom2
    new_num1 = num1 * denom2
    new_num2 = num2 * denom1
    sum_num = new_num1 + new_num2

    return simplify_fraction(sum_num, common_denom)


def multiply_fractions(fraction1: str, fraction2: str) -> tuple:
    num1, denom1 = map(int, fraction1.split('/'))
    num2, denom2 = map(int, fraction2.split('/'))

    product_num = num1 * num2
    product_denom = denom1 * denom2

    return simplify_fraction(product_num, product_denom)


try:
    fraction1 = input("Введите первую дробь (в формате a/b): ")
    fraction2 = input("Введите вторую дробь (в формате a/b): ")

    sum_result = add_fractions(fraction1, fraction2)
    product_result = multiply_fractions(fraction1, fraction2)

    print(f"""
              Введенные дроби: {fraction1} , {fraction2}
              Проверка встроенным методом Fraction: {Fraction(fraction1)} , {Fraction(fraction2)}
              """)

    print("Сумма дробей:", f"{sum_result[0]}/{sum_result[1]}")
    print("Произведение дробей:",
          f"{product_result[0]}/{product_result[1]}")

except ValueError:
    print("Ошибка! Введите корректные дроби в формате a/b.")
