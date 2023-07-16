# a = 5
# print(isinstance(a, int))
# a = 'hello!'
# print(isinstance(a, str))
# a = 42.0 * 3.141592 / 2.71828
# print(isinstance(a, (int, float, complex)))


# num = 2 + 2 * 2
# digit = 36 / 6
# print(num, digit)
# print(num == digit)
# print(num is digit)

# a = 5
# print(a, id(a))
# a += 1
# print(a, id(a))

# txt = 'hello world'
# print(txt, id(txt))
# txt = txt.replace(' ', '_')
# print(txt, id(txt))

# a = c = 2
# b = 3
# print(a, id(a), b, id(b), c, id(c))
# a = b + c
# print(a, id(a), b, id(b), c, id(c))

# x = 42
# y = 'text'
# z = 3.141592
# print(hash(x), hash(y), hash(z))
# my_list = [x, y, z]
# print(my_list)
# print(hash(my_list))

# user_str = str(input('введите текст: '))
# print(type(user_str), id(user_str), hash(user_str))

# a: float = 42.0
# b: float = float(input('input number '))
# a = a / b
# print(a)

# def my_func(data: list[int, float]) -> float:
#     res = sum(data) / len(data)
#     return res
# print(my_func([2, 5.5, 15, 8.0, 13.74]))

# a: int | float = 42.0
# b: float = float(input('input number '))
# a = a / b
# print(a)

# print(('hello world'.__doc__))
# print(str.__doc__)

# print('hello world'.upper())
# print('hello world'.count('l'))

# print(help(5))
# help()

# x = int('42')
# y = int(3.141592)
# z = int('hello', base=36)
# print(x, y, z, sep='\n')

# import sys

# STEP = 2 **16
# num = 1
# for _ in range(30):
#     print(sys.getsizeof(num), num)
#     num *= STEP

# a = 7_900_753_85_33
# print(a)

# num = 2 ** 16 - 1
# b = bin(num)
# o = oct(num)
# h = hex(num)
# print(b, o, h, sep='\n')

# data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# while data:
#     print(data.pop())

# class MyClass(object):
#     t = """
#     sdafsdfdsfsdfsdfdssdfsdfsd
#     sdfsdfsdfdsfsdsdfsdfsdfsd
#     sdfsdfsdfsdfsdsfd
#     sdfsdfsdfsdfssdfsfsf
#     sdf
#     sdfsdfsdsdfsdsdfsdfsdf
#     """

# LIMIT = 120
# ATTENTION = 'Внимание!'
# name = input('your name? ')
# age = int(input('your age? '))
# text = ATTENTION + 'Хоть тебе и осталось ' + str(100 - age) +\
#     ' до ста лет, но длинна строки не должна превышать ' + \
#     str(LIMIT) + ' символов.'
# print(text)

a = 10
b = 15
print(*divmod(a, b), sep='\n')
