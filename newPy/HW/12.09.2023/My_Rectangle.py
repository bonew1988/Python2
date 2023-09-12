class InvalidRectangleError(Exception):
    def __init__(self, message):
        super().__init__(message)


class Rectangle:
    def __init__(self, length_cm: float, width_cm: float = None) -> None:
        if length_cm <= 0 or (width_cm is not None and width_cm <= 0):
            raise InvalidRectangleError(
                "Длина и ширина должны быть положительными числами.")

        self.length = length_cm
        if width_cm:
            self.width = width_cm
        else:
            self.width = length_cm

    def calc_len(self):
        return (self.width + self.length) * 2

    def calc_square(self):
        return self.width * self.length

    def __add__(self, other):
        return Rectangle(length_cm=(self.length + other.length), width_cm=self.width)

    def __sub__(self, other):
        return Rectangle(length_cm=abs(self.length - other.length), width_cm=self.width)

    def __eq__(self, other: "Rectangle"):
        return self.calc_square() == other.calc_square()

    def __lt__(self, other: "Rectangle"):
        return self.calc_square() < other.calc_square()

    def __gt__(self, other: "Rectangle"):
        return self.calc_square() > other.calc_square()

    def __ge__(self, other: "Rectangle"):
        return self.calc_square() >= other.calc_square()

    def __le__(self, other: "Rectangle"):
        return self.calc_square() <= other.calc_square()


if __name__ == '__main__':
    try:
        r1 = Rectangle(length_cm=-2, width_cm=2)
        print(f'{r1.calc_len() = }')
        print(f'{r1.calc_square() = }')
        print('---')

        r2 = Rectangle(length_cm=3)
        print(f'{r2.calc_len() = }')
        print(f'{r2.calc_square() = }')

        r3 = r2 + r1

        print('---')
        print(f'{r3.calc_len() = }')
        print(f'{r3.calc_square() = }')

        print(r1 == r2)
        print(r1 <= r2)
        print(r1 >= r2)
    except InvalidRectangleError as e:
        print(f"Ошибка при создании прямоугольника: {e}")
