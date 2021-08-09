class Road:

    def __init__(self, lenght, width):
        self._length = lenght
        self._width = width
        metr_mass = 25
        height = 5

        mass_x = self._length * self._width * metr_mass * height

        print(
            f'Длина {lenght}м * ширину {width}м * толщину {height}см * массу {metr_mass}кг = {int(mass_x / 1000)}т')


m = Road(5000, 20)
