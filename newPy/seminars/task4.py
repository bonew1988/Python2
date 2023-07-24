# Напишите функцию, которая принимает строку текста.
# Вывести функцией каждое слово с новой строки.
# Строки нумеруются начиная с единицы.
# Слова выводятся отсортированными согласно кодировки Unicode.
# Текст выравнивается по правому краю так, чтобы у самого
# длинного слова был один пробел между ним и номером строки.

# def sort_by_unicod(text: str):
#     lst_sorted = sorted(text.split())
#     max_word = len(max(lst_sorted, key=len))
#     for i, element in enumerate(lst_sorted, start=1):
#         print(f"{i} {element:>{max_word}}")


# text = "У нас все хорошо! А будет еще лучше!"
# sort_by_unicod(text)

# ----------------------------------------------------------------------------------------------------

# Напишите функцию, которая принимает строку текста.
# Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.

# def list_sim(str_input):
#     return [ord(i) for i in sorted(list(str_input.replace(" ", '')), reverse=True)]


# def list_sim2(str_input):
#     return map(ord,
#                sorted(list(str_input.replace(" ", '')),
#                       reverse=True))


# str_data = 'Напишите функцию, которая принимает строку текста'
# list2 = []
# for i in sorted(list(str_data.replace(" ", '')), reverse=True):
#     list2.append(ord(i))
# print(list_sim(str_data))
# print(*list_sim2(str_data))

# ----------------------------------------------------------------------------------------------------

# Функция получает на вход строку из двух чисел через пробел.
# Сформируйте словарь, где ключом будет
# символ из Unicode, а значением —  целое число.
# Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до наибольшего включительно.

# def str_to_dict(string: str) -> dict[str, int]:
#     result = {}
#     start, end = sorted(map(int, string.split()))
#     for i in range(start, end + 1):
#         result[chr(i)] = i
#     return result


# print(str_to_dict("2 9"))


# ----------------------------------------------------------------------------------------------------

# Функция получает на вход список чисел.
# Отсортируйте его элементы in place без использования встроенных в язык сортировок.
# Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии.

# from typing import List


# def sort_namber(nambers: List[int]) -> None:
#     for i in range(len(nambers)):
#         for j in range(i, len(nambers)):
#             if nambers[i] > nambers[j]:
#                 nambers[i], nambers[j] = nambers[j], nambers[i]


# namber: List[int] = [7, 954, 91, 37, 7, 1, -4, 6]

# print(namber)

# sort_namber(namber)

# print(namber)

# ----------------------------------------------------------------------------------------------------

# ✔ Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии.

# def calc_bonus(names: list[str], rate: list[int], bonus: list[str]) -> dict[str, float]:
#     result = {}
#     temp = zip(names, rate, bonus)
#     for n, r, b in temp:
#         result[n] = float(b.strip('%')) * r / 100
#     return result


# names = ['Федор', 'Михаил', 'Владимир', 'Алексей']
# rates = [15000, 20000, 25000, 30000]
# bonuses = ['10.15%', '13.15%', '15.15%', '19.15%']
# print(calc_bonus(names, rates, bonuses))

# ----------------------------------------------------------------------------------------------------

# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.

# def sum_in_range(nums: list[int], start: int, end: int) -> int:
#     if start > end:
#         start, end = end, start
#     if start < 0:
#         start = 0
#     if end > len(nums)-1:
#         end = len(nums)-1
#     return sum(nums[start: end])


# nums = list(range(10))
# print(nums)
# print(sum_in_range(nums, 10, -1))

# ----------------------------------------------------------------------------------------------------

# Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения.
# ✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
# прибыльные, верните истину, а если хотя бы одна убыточная — ложь.

# def calculate_profit(companies):
#     all_profitable = True
#     result = {}
#     for company, transactions in companies.items():
#         total = sum(transactions)
#         result[company] = total
#         if total < 0:
#             all_profitable = False
#     return result, all_profitable

# companies = {
#     "Company1": [1000, -500, 200, -300,-2500],
#     "Company2": [2000, -1000, 500, -500],
#     "Company3": [1500, -700, 300, -200, -800,]
# }

# print(calculate_profit(companies))

# ----------------------------------------------------------------------------------------------------

# ✔ Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

tests = "test value"
variables = "another test value"
s = "single letter variable"
check = "this variable does not end with s"


def replace_s_variables():
    variables_dict = globals()
    for var_name in list(variables_dict.keys()):
        if var_name.endswith('s') and var_name != 's':
            new_var_name = var_name[:-1]
            variables_dict[new_var_name] = variables_dict[var_name]
            variables_dict[var_name] = None


print(f'ГЛОБАЛОЧКИ:  {globals()}')
