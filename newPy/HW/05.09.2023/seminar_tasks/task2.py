# Задание №2
# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списковархивов
# list-архивы также являются свойствами экземпляра


class Archive:
    """
    Класс Archive реализует шаблон Singleton для архивирования текстовых и числовых данных.

    Позволяет хранить только один экземпляр архива и добавлять в него новые данные с сохранением истории.
    """

    instance = None

    def __new__(cls, text: str, num: int):
        """
        Создает новый экземпляр класса Archive или возвращает существующий.

        Если экземпляр уже существует, добавляет текущие данные в архив.

        Args:
            text (str): Текстовое значение для архивирования.
            num (int): Числовое значение для архивирования.

        Returns:
            Archive: Экземпляр класса Archive.
        """
        if cls.instance:
            cls.instance.old_text.append(cls.instance.text)
            cls.instance.old_int.append(cls.instance.num)
        else:
            cls.instance = super().__new__(cls)
            cls.instance.old_text = []
            cls.instance.old_int = []
        return cls.instance

    def __init__(self, text: str, num: int) -> None:
        """
        Инициализирует новый экземпляр класса Archive.

        Args:
            text (str): Текстовое значение для архивирования.
            num (int): Числовое значение для архивирования.
        """
        self.text = text
        self.num = num

    def print_archive(self):
        """
        Выводит архив данных на печать, включая сохраненные текстовые и числовые значения.
        """
        print("Архив текстовых значений:")
        for text_value in self.old_text:
            print(text_value)
        print("Архив числовых значений:")
        for num_value in self.old_int:
            print(num_value)


if __name__ == '__main__':
    a1 = Archive(text='t', num=5)
    a2 = Archive(text='ti', num=10)
    a3 = Archive(text='tit', num=15)

    a3.print_archive()
