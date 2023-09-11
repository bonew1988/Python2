class Rectangle:
    #экономим память:
    #__slots__ = ['__length', '__width']

    def __init__(self,
                 length_cm: float,
                 width_cm: float = None) -> None:
        self.__length = length_cm
        if width_cm:
            self.__width = width_cm
        else:
            self.__width = length_cm

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        if value < 0:
            text: str = "не может быть меньше нуля"
            raise ValueError(text)
        self.__length = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value < 0:
            text: str = "не может быть меньше нуля"
            raise ValueError(text)
        self.__width = value

    def __eq__(self, other):
        return self.__length == other.__length \
            and self.__width == other.__width

    def __repr__(self):
        return f'Rectangle(length_cm={self.length}, ' \
               f'width_cm={self.width})'

    def __str__(self):
        return f'Длинна: {self.length}, ' \
               f'Ширина: {self.width}.'


if __name__ == '__main__':
    r1 = Rectangle(length_cm=2,
                   width_cm=3)
    print(r1.length)
    print(r1.width)
    r1.length = 4
    print(r1.length)
    print(r1.width)
    #r1.length = -1
    print(r1.length)
    print(r1.width)
    #print(r1.__dict__)