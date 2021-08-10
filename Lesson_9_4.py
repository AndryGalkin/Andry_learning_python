class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_polise = is_police
        print(f'{self.name}, color: {color}')

    def go(self):
        print('Car started')

    def stop(self):
        print('Car stops')

    def turn(self, direct):
        print(f'{self.name} turn left' if direct < 0 else f'{self.name} turn right')


class TownCar(Car):
    """Town car"""
    def show_speed(self):
        return f'{self.name} speed: {self.speed}. Speed over!' \
        if self.speed > 60 else f'{self.name} speed: {self.speed}'

class SportCar(Car):
    """Sport car"""
    def show_speed(self):
        return f'{self.name} speed: {self.speed}'
class WorkCar(Car):
    """Hard truck"""
    def show_speed(self):
        return f'{self.name} speed: {self.speed}. Speed over!' \
        if self.speed > 40 else f'{self.name} speed: {self.speed}'

class PoliceCar(Car):
    """Police car"""
    def __init__(self, speed, color, name, is_police=True):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        return f'{self.name} speed: {self.speed}'


w_c = WorkCar(65, 'White', 'Man 500')
w_c.go()
w_c.turn(-1)
print(w_c.show_speed())
w_c.turn(1)
w_c.stop()
print()

s_c = SportCar(165, 'Red', 'Aston Martin')
s_c.go()
s_c.turn(-1)
print(s_c.show_speed())
s_c.turn(1)
s_c.stop()
print()

t_c = TownCar(65, 'Gray', 'Hyundai')
t_c.go()
t_c.turn(-1)
print(t_c.show_speed())
t_c.turn(1)
t_c.stop()
print()


p_c = PoliceCar(65, 'White', 'Ford')
p_c.go()
p_c.turn(-1)
print(p_c.show_speed())
p_c.turn(1)
p_c.stop()
print()