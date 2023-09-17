import doctest


class FatorialGenerator:

    def __init__(self, *args) -> None:
        """
        Инициализирует генератор факториалов.

        Принимает 1, 2 или 3 аргумента:
        - Если передан 1 аргумент, то он интерпретируется как `stop`, и старт и шаг устанавливаются по умолчанию на 1.
        - Если передано 2 аргумента, то они интерпретируются как `start` и `step`, и `stop` устанавливается на 1.
        - Если передано 3 аргумента, то они интерпретируются как `start`, `stop` и `step` соответственно.

        Примеры:
        >>> a = FatorialGenerator(5)
        >>> list(a)
        [1, 2, 6, 24, 120]

        >>> b = FatorialGenerator(1, 5)
        >>> list(b)
        [1, 2, 6, 24, 120]

        >>> c = FatorialGenerator(1, 5, 2)
        >>> list(c)
        [1, 6, 120]

        >>> d = FatorialGenerator()
        >>> list(d)
        []

        >>> e = FatorialGenerator(0)
        >>> list(e)
        []

        >>> f = FatorialGenerator(3, 3, 2)
        >>> list(f)
        []
        """
        if len(args) == 3:
            self.start, self.stop, self.step = args
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
        """
        Возвращает следующий факториал в последовательности.

        Если `start` меньше чем `stop`, то возвращает факториал числа `start` и увеличивает `start` на `step`.
        Если `start` больше или равно `stop`, то вызывает StopIteration.

        Примеры:
        >>> a = FatorialGenerator(1, 5, 1)
        >>> next(a)
        1
        >>> next(a)
        2
        >>> next(a)
        6
        >>> next(a)
        24
        >>> next(a)
        120
        >>> next(a)
        Traceback (most recent call last):
            ...
        StopIteration

        >>> b = FatorialGenerator(1, 3, 2)
        >>> next(b)
        1
        >>> next(b)
        6
        >>> next(b)
        Traceback (most recent call last):
            ...
        StopIteration

        >>> c = FatorialGenerator(5)
        >>> next(c)
        1
        >>> next(c)
        2
        >>> next(c)
        6
        >>> next(c)
        24
        >>> next(c)
        120
        >>> next(c)
        Traceback (most recent call last):
            ...
        StopIteration
        """
        while self.start < self.stop:
            res = 1
            for i in range(1, self.start + 1):
                res *= i
            self.start += self.step
            return res
        raise StopIteration


if __name__ == '__main__':
    a = FatorialGenerator(1, 5, 1)
    for i in a:
        print(i)
    doctest.testmod(verbose=True)