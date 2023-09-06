# Задание №1
# Создайте класс Моя Строка, где:
# будут доступны все возможности str
# дополнительно хранятся имя автора строки и время создания
# (time.time)

from time import time


class MyStr(str):
    """
    Класс MyStr наследует стандартный тип str и добавляет дополнительные атрибуты, такие как 'name' и 'time_create'.
    """

    def __new__(cls, value: str, name: str):
        """
        Создает новый экземпляр класса MyStr.

        Args:
            value (str): Значение строки.
            name (str): Имя, связанное с строкой.

        Returns:
            MyStr: Новый экземпляр класса MyStr.
        """
        instance = super().__new__(cls, value)
        instance.value = value
        instance.name = name
        instance.time_create = time()
        return instance

    def __repr__(self) -> str:
        """
        Возвращает строковое представление экземпляра класса MyStr.

        Returns:
            str: Строковое представление экземпляра.
        """
        return f'MyStr({self.value=}, {self.name=})'

    def print_info(self):
        """
        Выводит информацию о строке на печать, включая значение, имя и время создания.
        """
        print(f"Значение: {self.value}")
        print(f"Имя: {self.name}")
        print(f"Время создания: {self.time_create}")


if __name__ == '__main__':
    st = MyStr(value='just do it', name='JohnDou')
    print(repr(st))
    st.print_info()
