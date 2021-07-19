class Car:
    speed = 0
    color = None
    name = None
    is_police = False

    def __init__(self, *args: tuple):
        Car.speed, Car.color, Car.name, Car.is_police = args

    def go(self):
        print(f'{Car.color} {Car.name} поехал')

    def stop(self):
        print(f'{Car.color} {Car.name} остановился')

    def turn(self, direction: str):
        print(f'{Car.color} {Car.name} повернул {direction}')

    def show_speed(self):
        print(f'Скорость {Car.color} {Car.name}: {Car.speed}')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f'{self.color} {self.name} превысил скорость')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f'{self.color} {self.name} превысил скорость')


class PoliceCar(Car):
    pass


ford = TownCar(50, 'Красный', 'форд', False)
ford.show_speed()
ford.turn('направо')

print()

toyota = TownCar(70, 'Желтая', 'тойота', False)
toyota.show_speed()
toyota.stop()

print()

truck = WorkCar(20, 'Серый', 'грузовик', False)
truck.show_speed()
truck.go()

print()

taxi = WorkCar(45, 'Зеленое', 'такси', False)
taxi.show_speed()
taxi.stop()

print()

lamborghini = SportCar(100, 'Красный', 'ламборгини', False)
lamborghini.go()
lamborghini.show_speed()

print()

police_car = PoliceCar(80, 'Синяя', 'полицейская машина', True)
police_car.turn('налево')
police_car.show_speed()

