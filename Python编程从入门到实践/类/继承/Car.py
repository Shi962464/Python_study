class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 100

    def get_descriptive(self):
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()

    def read_odometer(self):
        print(f'this car has {self.odometer_reading} miles on it!')

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('Error!!!!!')

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battry():
    def __init__(self, battry_size=100):
        self.battry_size = battry_size

    def des_battry(self):
        print(f'This car has a {self.battry_size} Kwh battry')

    def get_range(self):
        if self.battry_size == 75:
            range = 260
        elif self.battry_size == 100:
            range = 315
        else:
            range = 0
            print('Error-----')
        print(f'This car can go about {range} miles!')


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 75
        self.battry = Battry()

    def describe_battry(self):
        print(f'This car has a {self.battery_size} Kwh battry!')


my_tesla = ElectricCar('tesla', 'model S', '2024')
print(my_tesla.get_descriptive())
my_tesla.describe_battry()

my_tesla.battry.des_battry()
my_tesla.battry.get_range()
# my_car = Car('audi', 'A4', '2019')
# print(my_car.get_descriptive())
# my_car.read_odometer()
# my_car.odometer_reading += 100
# my_car.read_odometer()
# my_car.update_odometer(199)
# my_car.read_odometer()
#
# my_car.update_odometer(20000)
# my_car.read_odometer()
# my_car.increment_odometer(9000)
# my_car.read_odometer()
