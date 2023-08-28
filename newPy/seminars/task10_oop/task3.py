# Задание №3
# Напишите класс для хранения информации о человеке:
# ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения
# возраста на год, full_name для вывода полного ФИО и т.п. на
# ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого
# изменения, но есть возможность получить текущий возраст.

# Задание №4
# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# ○ шестизначный идентификационный номер
# ○ уровень доступа вычисляемый как остаток от деления
# суммы цифр id на семь

from random import randint


def sumdigit(source: int):
    source = str(source)
    sum_digit = 0
    for i in source:
        sum_digit += int(i)
    return sum_digit % 7


class Person:

    def __init__(self, surname, name, patronymic, age):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.__age = age

    def get_age(self):
        return self.__age

    def birthday(self):
        self.__age += 1

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'


class Employee(Person):
    def __init__(self, surname, name, patronymic, age):
        super().__init__(surname, name, patronymic, age)
        self.id = randint(100000, 999999)
        self.level = sumdigit(self.id)


if __name__ == '__main__':
    # p1 = Person("Ivanov", 'Ivan', 'Ivanovich', 25)
    # print(p1.__age)
    # print(p1.get_age())
    # print(p1.name)
    # print(p1)

    e1 = Employee('Petrov', 'Petr', 'Petrovitch', 25)
    print(e1.name, e1.id, e1.level)
