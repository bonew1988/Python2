# ✔ Пользователь вводит строку из четырёх
# или более целых чисел, разделённых символом “/”.
# Сформируйте словарь, где:
# ✔второе и третье число являются ключами.
# ✔первое число является значением для первого ключа.
# ✔четвертое и все возможные последующие числа
# хранятся в кортеже как значения второго ключа.

# def get_dict(data: str) -> dict[int:int]:
#     first, second, third, *other = (int(i) for i in data.split('/'))
#     return {second: first, third: tuple(other)}


# data_input = '1/2/3/4/5/6/7/8'

# print(get_dict(data_input))

# -------------------------------------------------------------------------

# ✔ Самостоятельно сохраните в переменной строку текста.
# ✔ Создайте из строки словарь, где ключ — буква, а значение — код буквы.
# ✔ Напишите преобразование в одну строку.

# ✔ Продолжаем развивать задачу 2.
# ✔ Возьмите словарь, который вы получили.
# Сохраните его итераторатор.
# ✔ Далее выведите первые 5 пар ключ-значение,
# обращаясь к итератору, а не к словарю.

# NUM = 5

# def get_dict(data: str) -> dict[str:int]:
#     return {i: ord(i) for i in data.replace(' ', '')}

# def get_iter(input_dict: dict):
#     iter_dict = iter(input_dict.items())
#     for i in range(NUM):
#         print(*next(iter_dict))

# data_str = 'Самостоятельно сохраните в переменной строку текста.'
# res_dict = get_dict(data_str)
# get_iter(res_dict)

# -------------------------------------------------------------------------

# ✔ Создайте генератор чётных чисел от нуля до 100.
# ✔ Из последовательности исключите
# числа, сумма цифр которых равна 8.
# ✔ Решение в одну строку.

# generator = (num for num in range(
#     0, 101) if num % 2 == 0 and sum(int(digit) for digit in str(num)) != 8)
# for number in generator:
#     print(number)

# -------------------------------------------------------------------------

# ✔ Напишите программу, которая выводит
# на экран числа от 1 до 100.
# ✔ При этом вместо чисел, кратных трем,
# программа должна выводить слово «Fizz»
# ✔ Вместо чисел, кратных пяти — слово «Buzz».
# ✔ Если число кратно и 3, и 5, то программа
# должна выводить слово «FizzBuzz».
# ✔ *Превратите решение в генераторное выражение.

# print(*("FizzBuzz" if num % 3 == 0 and num % 5 == 0
#         else "Fizz" if num % 3 == 0
#         else "Buzz" if num % 5 == 0
#         else num
#         for num in range(1, 101)))

# -------------------------------------------------------------------------

# ✔ Выведите в консоль таблицу умножения
# от 2х2 до 9х10 как на школьной тетрадке.
# ✔ Таблицу создайте в виде однострочного
# генератора, где каждый элемент генератора —
# отдельный пример таблицы умножения.
# ✔ Для вывода результата используйте «принт»
# без перехода на новую строку.

# print("\n\n".join(["\n".join([f"{j:2} * {i:^2} = {i * j:2}\t\t{j + 1:2} * {i:^2} = {i * (j + 1):2}\t\t{j + 2:2} * {i:^2} = {i * (j + 2):2}\t\t{j + 3:2} * {i:^2} = {i * (j + 3):2}" 
#                               for i in range(2, 11)]) 
#                    for j in range(2, 10, 4)]))


# -------------------------------------------------------------------------

# Создайте функцию-генератор.
# ✔ Функция генерирует N простых чисел,
# начиная с числа 2.
# ✔ Для проверки числа на простоту используйте
# правило: «число является простым, если делится
# нацело только на единицу и на себя».

# def prime_number_generator(n):
#     for i in range(2, n+1):
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             yield i
# print(*prime_number_generator(100))