class Dushnila:
    def __init__(self, dushnila):
        self.dushnila = dushnila

    def talk(self):
        if 3389 in self.dushnila:
            print('А как же константы выводить отдельно? if 3389 in open_ports:')
        else:
            print('Порт 3389 не найден в списке open_ports.')


# Создаем экземпляр класса с передачей списка open_ports
open_ports = [80, 443, 22]
dima = Dushnila(open_ports)
dima.talk()
