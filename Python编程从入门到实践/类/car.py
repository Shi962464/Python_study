# class Car():
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.odometer_reading = 100
#
#     def get_descriptive(self):
#         long_name = f'{self.year} {self.make} {self.model}'
#         return long_name.title()
#
#     def read_odometer(self):
#         print(f'this car has {self.odometer_reading} miles on it!')
#
#     def update_odometer(self, mileage):
#         if mileage >= self.odometer_reading:
#             self.odometer_reading = mileage
#         else:
#             print('Error!!!!!')
#
#     def increment_odometer(self, miles):
#         self.odometer_reading += miles
#
#
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


class Restaurant:
    # 初始化方法，设置餐厅名称、菜系和人数
    def __init__(self, name, cuisine):
        self.name = name  # 餐厅名称
        self.cuisine = cuisine  # 菜系
        self.number = 0  # 初始人数为0

    # 打印餐厅的名称和菜系
    def describe_restaurant(self):
        print(f"Welcome to {self.name}!")
        print(f"Our specialty is {self.cuisine} cuisine.")

    # 打印餐厅正在营业的消息
    def open_restaurant(self):
        print(f"{self.name} is now open for business!")

    # 增加就餐人数并打印
    def add_customer(self):
        self.number += 1
        print(f"Currently, {self.number} customer(s) are dining at {self.name}.")


# 创建一个实例
result = Restaurant("Sunshine Bistro", "Italian")

# 打印餐厅信息
result.describe_restaurant()

# 打印餐厅正在营业的信息
result.open_restaurant()

# 增加顾客并打印人数
result.add_customer()  # 第一次增加顾客




