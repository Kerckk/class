class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start (self):
        print("Машина начала движение")

    def stop (self):
        print("Машина остановилась")

    def year_of_car(self, year):
        self.year = year

    def type_of_car(self, type):
        self.type = type

    def cvet_of_car(self, color):
        self.color = color

class Bus(Car):
    def __init__(self, color, type, year, weight):
        super().__init__(color,type, year)
        self.weight = weight

    def year_of_Bus(self, year):
        self.year = year
        print('Год автобуса:',input('Ввидите год автобуса:'))
class Moto(Bus):
    def __init__(self,color='blue', type='Yamaha', year="2008",weight="105"):
        super().__init__(color, type, year,weight)
    def parking(self):
        print('Мотоцикл припоркавался')
    def refueled(self):
        print("Мотоцикл заправили")
    def repair(self):
        print("Мотоцикл отремонтировали")

car = Car("Green", "LADA", 2012)
bus = Bus("black", "FORD", "2014", "1000 kg")
moto = Moto('blue','Yamaha','2008', '105')
moto.parking()
moto.refueled()
moto.repair()
bus.year_of_Bus(2014)
car.start()
car.stop()
car.year_of_car(2012)
car.type_of_car("LADA")
car.cvet_of_car("Green")




