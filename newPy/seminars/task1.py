# Работа в консоли в режиме интерпретатора Python. 
# Решите квадратное уравнение 5x2-10x-400=0 последовательно 
# сохраняя переменные a, b, c, d, x1 и x2.
# *Попробуйте решить уравнения с другими значениями a, b, c.

#-------------------------------------------------------------------

# Работа в консоли в режиме интерпретатора Python. 
# Посчитайте сумму чётных элементов от 1 до n исключая кратные e. 
# Используйте while и if. 
# Попробуйте разные значения e и n.

# n = 10
# e = 5
# sum_n = 0

# i = 1
# while i <= n:
#     if i % 2 == 0 and i % e != 0:
#         sum_n += i
#     i += 1

# print("Сумма четных чисел от 1 до", n, "исключая числа, кратные", e, ":", sum_n)

#-------------------------------------------------------------------

# Задача 6
# Напишите программу, которая запрашивает год и проверяет его на високосность.
# Распишите все возможные проверки в цепочке elif
# Откажитесь от магических чисел
# Обязательно учтите год ввода Григорианского календаря
# В коде должны быть один input и один print

# year = int(input('введите год в формате хххх: '))
# MULTIPLES = 4
# CHEK1 = 100
# CHEK2 = 400

# if year % MULTIPLES == 0 and year % CHEK1 != 0 or year % CHEK2 == 0:
#     print('год високосный')
# else:
#     print('обычный')

# Пользователь вводит число от 1 до 999. Используя операции с числами 
# сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print

# num  = int(input('введите число от 1 до 999: '))

# if 1 <= num <= 9:
#     result = num ** 2
# elif 10 <= num <= 99:
#     digit1 = num // 10
#     digit2 = num % 10
#     result = digit1 * digit2
# elif 100 <= num <= 999:
#     digit1 = num // 100
#     digit2 = (num % 100) // 10
#     digit3 = num % 10
#     result = digit3 * 100 + digit2 * 10 + digit1
# else:
#     print('некорректный ввод')
# print(result)

#-----------------------
# Ёлочка

# rows = int(input('Введите количество рядов: '))
# for i in range(1, rows + 1):
#     spaces  = rows - i
#     stars = 2 * i -1
#     print(" " * spaces + '*' * stars)
    
#------------------------------------------------

# Таблица умножения
# for i in range(2, 10):
#     for j in range(2, 11):
#         result = i * j
#         print(f"{i} x {j} = {result}")
#     print()