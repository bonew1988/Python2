class Animal:
    def __init__(self, name, age):
        self.name = name.capitalize()
        self.age = age

    def __str__(self) -> str:
        return f'{self.name} {self.age}'

    def birthday(self):
        self.age += 1


class Dog(Animal):
    def __init__(self,
                 name: str,
                 age: int,
                 color: str,
                 breed: str,
                 is_domestic: bool = True) -> None:
        super().__init__(name, age)

        self.color = color
        self.breed = breed
        self.is_domestic = is_domestic

    def __str__(self):
        if self.is_domestic:
            return f'Dog {self.color} {self.breed} домашняя'
        return f'Dog {self.color} {self.breed} дворняга'


class Kotopes(Animal):
    def __init__(self,
                 age: int,
                 name: str,
                 number_heads: int = 2) -> None:
        super().__init__(name, age)
        self.__number_heads = number_heads

    def __str__(self):
        return f'Kotopes -> number_heads: {self.__number_heads},\
Возраст: {self.age}, не женат '


class Fish(Animal):

    def __init__(self, name, age, aqua, size):
        super().__init__(name, age)
        self.aqua = aqua
        self.size = size

    def __str__(self):
        if self.aqua:
            return f'{self.name} морская'
        else:
            return f'{self.name} пресноводная'


class Factory:
    def __init__(self, animal_class):
        self.animal_class = animal_class

    def create_animal(self, **kwargs):
        return self.animal_class(**kwargs)


if __name__ == "__main__":

    dog_params = {'name': 'Шарик', 'age': 2, 'color': 'черный',
                  'breed': 'овчарка', 'is_domestic': True}
    kotopes_params = {'name': 'Барсик', 'age': 3, 'number_heads': 2}
    fish_params = {'name': 'Немо', 'age': 1, 'aqua': True, 'size': 0.3}

    df = Factory(Dog)
    kf = Factory(Kotopes)
    ff = Factory(Fish)

    dog = df.create_animal(**dog_params)
    kotopes = kf.create_animal(**kotopes_params)
    fish = ff.create_animal(**fish_params)

    print(type(dog), dog)
    print(type(kotopes), kotopes)
    print(type(fish), fish)
