# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex используйте для проверки своего результата.


TRANSLATE_DICT = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7',
                  8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
DIVIDER = 16

# num = int(input('Введите целое число: '))
num = 255
temp = num
hex_string = ''
if num < 0:
    num = abs(num)

while temp > 0:
    hex_string += TRANSLATE_DICT.get(temp % DIVIDER, str(temp % DIVIDER))
    temp //= DIVIDER
hex_string = hex_string[::-1]
print(f"""
      Введенное число: {num}\n
      Результат: {hex_string}\n
      Проверка: {hex(num)}
      """)
