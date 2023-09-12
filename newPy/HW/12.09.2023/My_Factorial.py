import json


class InvalidValueError(Exception):
    def __init__(self, value, message="Недопустимое значение"):
        self.value = value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.message}: {self.value}"


class Factorial:

    def __init__(self, k):
        if k <= 0:
            raise InvalidValueError(
                k, "Количество значений k должно быть положительным.")
        self.k = k
        self.values = []

    def __call__(self, num):
        if num < 0:
            raise InvalidValueError(
                num, "Значение num должно быть неотрицательным.")
        res = 1
        for i in range(1, num + 1):
            res *= i
        if len(self.values) >= self.k:
            self.values.pop(0)
        self.values.append({num: res})
        return res

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            with open('/home/bonew/Рабочий стол/newPY/Python2/newPy/zoo.json', 'w', encoding='utf-8') as f:
                json.dump(self.values, f)


if __name__ == '__main__':
    try:
        f = Factorial(4)

        print(f.values)
        with f as copy_:
            print(copy_(3))
            print(copy_(4))
            print(copy_(5))
            print(copy_(6))
            print(copy_(7))
            print(copy_(-8))
    except InvalidValueError as e:
        print(f"Ошибка: {e}")
