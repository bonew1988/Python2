
# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников
# по площади
# Должны работать все шесть
# операций сравнения


class Rectangle:
    """
    Класс Rectangle представляет прямоугольник с заданными длиной и шириной.

    Методы:
    - calc_len(): Вычисляет периметр прямоугольника.
    - calc_square(): Вычисляет площадь прямоугольника.
    """

    def __init__(self, length_cm: float, width_cm: float = None) -> None:
        """
        Инициализирует новый экземпляр класса Rectangle.

        Args:
            length_cm (float): Длина прямоугольника в сантиметрах.
            width_cm (float): Ширина прямоугольника в сантиметрах. Если не указана, то прямоугольник будет квадратом.
        """
        self.length = length_cm
        if width_cm:
            self.width = width_cm
        else:
            self.width = length_cm

    def calc_len(self) -> float:
        """
        Вычисляет периметр прямоугольника.

        Returns:
            float: Значение периметра.
        """
        return (self.width + self.length) * 2

    def calc_square(self) -> float:
        """
        Вычисляет площадь прямоугольника.

        Returns:
            float: Значение площади.
        """
        return self.width * self.length

    def __add__(self, other: 'Rectangle') -> 'Rectangle':
        """
        Выполняет сложение двух прямоугольников.

        Args:
            other (Rectangle): Другой прямоугольник, который будет сложен с текущим.

        Returns:
            Rectangle: Новый прямоугольник, результат сложения.
        """
        return Rectangle(length_cm=(self.length + other.length), width_cm=self.width)

    def __sub__(self, other: 'Rectangle') -> 'Rectangle':
        """
        Выполняет вычитание одного прямоугольника из другого.

        Args:
            other (Rectangle): Прямоугольник, который будет вычитаться из текущего.

        Returns:
            Rectangle: Новый прямоугольник, результат вычитания.
        """
        return Rectangle(length_cm=abs(self.length - other.length), width_cm=self.width)

    def __eq__(self, other: 'Rectangle') -> bool:
        """
        Проверяет, равны ли площади двух прямоугольников.

        Args:
            other (Rectangle): Другой прямоугольник для сравнения.

        Returns:
            bool: True, если площади равны, иначе False.
        """
        return self.calc_square() == other.calc_square()

    def __lt__(self, other: 'Rectangle') -> bool:
        """
        Проверяет, является ли площадь текущего прямоугольника меньше площади другого.

        Args:
            other (Rectangle): Другой прямоугольник для сравнения.

        Returns:
            bool: True, если площадь меньше, иначе False.
        """
        return self.calc_square() < other.calc_square()

    def __gt__(self, other: 'Rectangle') -> bool:
        """
        Проверяет, является ли площадь текущего прямоугольника больше площади другого.

        Args:
            other (Rectangle): Другой прямоугольник для сравнения.

        Returns:
            bool: True, если площадь больше, иначе False.
        """
        return self.calc_square() > other.calc_square()

    def __ge__(self, other: 'Rectangle') -> bool:
        """
        Проверяет, является ли площадь текущего прямоугольника больше или равной площади другого.

        Args:
            other (Rectangle): Другой прямоугольник для сравнения.

        Returns:
            bool: True, если площадь больше или равна, иначе False.
        """
        return self.calc_square() >= other.calc_square()

    def __le__(self, other: 'Rectangle') -> bool:
        """
        Проверяет, является ли площадь текущего прямоугольника меньше или равной площади другого.

        Args:
            other (Rectangle): Другой прямоугольник для сравнения.

        Returns:
            bool: True, если площадь меньше или равна, иначе False.
        """


if __name__ == '__main__':
    r1 = Rectangle(length_cm=2, width_cm=2)
    print(f'Периметр r1: {r1.calc_len()}')
    print(f'Площадь r1: {r1.calc_square()}')
    print('---')

    r2 = Rectangle(length_cm=3)
    print(f'Периметр r2: {r2.calc_len()}')
    print(f'Площадь r2: {r2.calc_square()}')

    r3 = r2 + r1

    print('---')
    print(f'Периметр r3: {r3.calc_len()}')
    print(f'Площадь r3: {r3.calc_square()}')

    print(f'r1 == r2: {r1 == r2}')
    print(f'r1 <= r2: {r1 <= r2}')
    print(f'r1 >= r2: {r1 >= r2}')
