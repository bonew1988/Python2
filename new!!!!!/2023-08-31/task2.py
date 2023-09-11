# Задание №2
# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списковархивов
# list-архивы также являются свойствами экземпляра

class Archive:
    instance = None

    def __new__(cls, text: str, num: int):
        if cls.instance:
            cls.instance.old_text.append(cls.instance.text)
            cls.instance.old_int.append(cls.instance.num)
        else:
            cls.instance = super().__new__(cls)
            cls.instance.old_text = []
            cls.instance.old_int = []
        return cls.instance

    def __init__(self, text: str, num: int) -> None:
        self.text = text
        self.num = num


if __name__ == '__main__':
    a1 = Archive(text='t', num=5)
    a2 = Archive(text='ti', num=10)
    a3 = Archive(text='tit', num=15)

    print(a3.instance.old_text)
    print(a3.instance.old_int)
