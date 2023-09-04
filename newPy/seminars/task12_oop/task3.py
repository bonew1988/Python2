# Задание №4
# Доработайте класс прямоугольник из прошлых семинаров.
# Добавьте возможность изменять длину и ширину
# прямоугольника и встройте контроль недопустимых значений
# (отрицательных).
# Используйте декораторы свойств.


# Изменяем класс прямоугольника. Заменяем пару декораторов проверяющих длину и ширину на дескриптор с валидацией размера.

class Side:

    def __init__(self, min_length, max_length):
        self.max_length = max_length
        self.min_length = min_length

    def __set_name__(self, owner, name):
        self._param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self._param_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self._param_name, value)

    def validate(self, value):
        if not self.min_length < value < self.max_length:
            raise ValueError(f'Значение выходит за пределы заданных параметров.'
                             f' От {self.min_length} до {self.max_length}')


class Rectangle:

    __width = Side(0, 7)
    __length = Side(2, 10)

    def __init__(self,
                 length_cm: float,
                 width_cm: float = None) -> None:
        self.__length = length_cm
        if width_cm:
            self.__width = width_cm
        else:
            self.__width = length_cm

    def __repr__(self):
        return f'Rectangle(length_cm={self.__length}, ' \
               f'width_cm={self.__width})'

    def __str__(self):
        return f'Длинна: {self.__length}, ' \
               f'Ширина: {self.__width}.'


if __name__ == '__main__':
    r1 = Rectangle(length_cm=4,
                   width_cm=8)
    print(r1)
    print(r1._Rectangle__length)
