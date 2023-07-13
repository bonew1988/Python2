# ----------------------------------------------------------------
# name = "Alex"
# age = None
# a = 42
# a = "Hello World!"
# a = 3.14 / 3
# # print(a)
# print(name, age, a, 456, 'test', sep=' (=^.^=) ', end='#')
# print("any text")

# res = input('print your text: ')
# print('Ты написал: ')
# print(res)

# ADULT = 18
# age = int(input("сколько тебе лет?"))
# how_old = - age + ADULT
# print(how_old, 'осталось до совершеннолетия')
# ----------------------------------------------------------------
# pwd = 'text'
# res = input('input password: ')
# if res == pwd:
#     print('access accept')
#     print('warning')
# else:
#     print('access denied')
# print('jobs done!')

# ----------------------------------------------------------------
# color = input('твой любимый цвет: ')
# if color == 'красный':
#     print('Любитель яркого?')
# elif color == 'зеленый':
#     print('ты не охотник?')
# elif color == 'синий':
#     print('Ха, классика!')
# else:
#     print('Тебя не понять')

# ----------------------------------------------------------------
# color = input('твой любимый цвет: ')
# match color:
#     case 'красный' | 'оранжевый':
#         print('Любитель яркого?')
#     case 'зеленый':
#         print('ты не охотник?')
#     case 'синий':
#         print('Ха, классика!')
#     case _:
#         print('Тебя не понять')
# ----------------------------------------------------------------
# year = int(input('введите год в формате ХХХХ: '))
# if year % 4 != 0:
#     print('Обычный')
# elif year % 100 == 0:
#     if year % 400 == 0:
#         print('високосный')
#     else:
#         print('Обычный')
# else:
#     print('високосный')
# ----------------------------------------------------------------
# data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
# num = int(input('insert number: '))
# if num not in data:
#     print('not a fibi')

# ----------------------------------------------------------------
# my_match = int(input('2 + 2 = '))
# print('Верно!' if 2 + 2 == my_match else 'Вы уверены?')

print(*[i for i in range(1, 10, 1)], sep='\n')
print('Hello', 'how are you?')
x = ('apple', 'banana', 'cherry')
print(x)
print('Hello', 'how are you?', sep=' ---')
