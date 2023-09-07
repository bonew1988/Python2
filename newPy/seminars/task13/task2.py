# Задание №2
# Создайте функцию аналог get для словаря.
# Помимо самого словаря функция принимает ключ и
# значение по умолчанию.
# При обращении к несуществующему ключу функция должна
# возвращать дефолтное значение.
# Реализуйте работу через обработку исключений

class MyDict(dict):

    def my_get(self, key_, value_=None):
        try:
            return self[key_]
        except KeyError:
            return value_


if __name__ == '__main__':
    mg = MyDict({'one': 1, 'two': 2})
    print(mg)
    print(mg.my_get('one', 'john'))
    print(mg)
