class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'profit': wage, 'bonus': bonus}


class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_full_profit(self):
        return f'{sum(self._income.values())}'


junior = Position('Paul', 'McCartney','bass player', 150000, 50000)

print(junior.get_full_name())
print(junior.position)
print(junior.get_full_profit())