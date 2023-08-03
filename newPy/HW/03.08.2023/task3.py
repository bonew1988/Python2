# Создайте функцию генератор чисел Фибоначчи (см. Википедию)


def fibonacci_generator() -> None:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


fib = fibonacci_generator()
for _ in range(10):
    print(next(fib))
