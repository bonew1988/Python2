# Задание №1
# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании
# экземпляра.
# У класса должно быть два метода, возвращающие длину
# окружности и её площадь.


import math


class Circle:
    _pi = math.pi

    def __init__(self, radius) -> None:
        self.radius = radius

    def calc_len(self):
        return self._pi * self.radius * 2

    def calc_area(self):
        return self._pi * self. radius ** 2
