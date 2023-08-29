# Задание №1
# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании
# экземпляра.
# У класса должно быть два метода, возвращающие длину
# окружности и её площадь.


from math import pi


class Circle:
    _pi = pi

    def __init__(self, radius) -> None:
        self.radius = radius

    def calc_len(self):
        return self._pi * self.radius * 2

    def calc_area(self):
        return self._pi * self. radius ** 2


if __name__ == '__main__':
    c1 = Circle(radius=15)
    print(f'{c1.calc_len()} {c1.calc_area()}')
