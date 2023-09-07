# Задание №3
# Создайте класс с базовым исключением и дочерние классыисключения:
# ○ ошибка уровня,
# ○ ошибка доступа.

# Задание №4
# Вспоминаем задачу из семинара 8 про сериализацию данных,
# где в бесконечном цикле запрашивали имя, личный
# идентификатор и уровень доступа (от 1 до 7) сохраняя
# информацию в JSON файл.
# Напишите класс пользователя, который хранит эти данные в
# свойствах экземпляра.
# Отдельно напишите функцию, которая считывает информацию
# из JSON файла и формирует множество пользователей.


# Задание №5
# Доработаем задачи 3 и 4. Создайте класс проекта, который
# имеет следующие методы:
# загрузка данных (функция из задания 4)
# вход в систему - требует указать имя и id пользователя. Для
# проверки наличия пользователя в множестве используйте
# магический метод проверки на равенство пользователей.
# Если такого пользователя нет, вызывайте исключение
# доступа. А если пользователь есть, получите его уровень из
# множества пользователей.
# добавление пользователя. Если уровень пользователя
# меньше, чем ваш уровень, вызывайте исключение уровня
# доступа.

import json


class MyExc(Exception):
    pass


class LevelExceprtion(MyExc):
    pass


class AccessException(MyExc):
    pass


class User:
    def __init__(self, user_id: int, level: int, user_name: str) -> None:
        self.__user_id = user_id
        self.level = level
        self.user_name = user_name

    def load(self, filename: str):
        with open(f'{filename}.json', "r", encoding='utf-8') as file:
            data = json.load(file)
        users: set = set()
        for one_user in data:
            users.add(User(*one_user.values()))
        return users

    def __eq__(self, other) -> bool:
        return self.user_name == other.user_name and self.__user_id == other.__user_id
    
    def __hash__(self) -> int:
        return int(self.__user_id)

    def __repr__(self):
        return f'Имя:{self.user_name} id:{self.__user_id} Уровень доступа: {self.level}'


class Project:
    def __init__(self) -> None:
        self.users = User(level=7, user_id=10,
                          user_name="Alex").load('test111')
        self.entered_user = None

    def relolad_users(self):
        self.users = User(level=7, user_id=10,
                          user_name="Alex").load('test111')

    def enter(self, id: int, name: str):
        that_user = User(user_id=id, level=None, user_name=name)
        if that_user not in self.users:
            raise AccessException
        for i in self.users:
            if i == that_user:
                self.entered_user = i

    def add_user(self, id, level, name):
        if self.entered_user.level < level:
            raise LevelExceprtion
        self.users.add(User(id, level, name))


if __name__ == "__main__":
    proj = Project()
    proj.enter(id=123456, name="Vlad")
    
    proj.add_user(id=159366, level=4, name='Asat')
    print(proj.users)
    
