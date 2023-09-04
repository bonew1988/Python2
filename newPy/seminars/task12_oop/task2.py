# Задание №3
# Создайте класс-генератор.
# Экземпляр класса должен генерировать факториал числа в
# диапазоне от start до stop с шагом step.
# Если переданы два параметра, считаем step=1.
# Если передан один параметр, также считаем start=1.

class FatorialGenerator:

    def __init__(self, *args) -> None:
        if len(args) == 3:
            self.start, self. stop, self.step = args
        elif len(args) == 2:
            self.start, self.step = args
            self.stop = 1
        elif len(args) == 1:
            self.stop = args[0]
            self.start = 1
            self.step = 1

    def __iter__(self):
        return self

    def __next__(self):
        while self.start < self.stop:
            res = 1
            for i in range(1, self.start + 1):
                res *= i
            self.start += 1
            return res
        raise StopIteration


if __name__ == '__main__':
    a = FatorialGenerator(1, 5, 1)
    for i in a:
        print(i)
