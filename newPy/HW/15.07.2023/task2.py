# Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу 
# и на себя”. Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

while True:
    number = input("Введите число (от 2 до 100000): ")
    try:
        number = int(number)
    except ValueError:
        print("Некорректный ввод. Пожалуйста, введите целое число.")
        continue
    if number < 2 or number > 100000:
        print("Число должно быть от 2 до 100000. Попробуйте еще раз.")
        continue
    is_prime = True
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            is_prime = False
            break
    if is_prime:
        print(f"{number} - простое число.")
    else:
        print(f"{number} - составное число.")
    break
