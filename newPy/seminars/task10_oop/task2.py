# Задание №2
# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании
# экземпляра.
# У класса должно быть два метода, возвращающие периметр
# и площадь.
# Если при создании экземпляра передаётся только одна
# сторона, считаем что у нас квадрат.


class Rectangle:
    def __init__(self, len, width=None) -> None:
        self.len = len
        if width:
            self.width = width
        else:
            self.width = len

    def calc_len(self):
        return (self.len + self.width) * 2

    def calc_S(self):
        return self.len * self.width


if __name__ == '__main__':
    r1 = Rectangle(len=2, width=4)

    print(f'{r1.calc_len()=}')
    print(f'{r1.calc_S()=}')

    r2 = Rectangle(len=4)

    print(f'{r2.calc_len()=}')
    print(f'{r2.calc_S()=}')
