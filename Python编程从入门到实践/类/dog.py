# class Dog():
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         print(f'{self.name} is now sitting')
#
#     def roll(self):
#         print(f'{self.name} roll over')
#
#
# aa = Dog('aa', '15')
# aa.sit()
# aa.roll()
# print(f'name is :{aa.name}')
# print(f'age is {aa.age}')


# class Rest():
#     def __init__(self,name,type):
#         self.name=name
#         self.type=type
#     def describe(self):
#         print(f'{self.name}')
#         print(f'{self.type}')
#     def open(self):
#         print('This is open')
# aa=Rest('pizaa','hot')
# aa.describe()
# aa.open()
#


class User():
    def __init__(self, f_name, l_name, age, gender):
        self.f_name = f_name
        self.l_name = l_name
        self.age = age
        self.gender = gender

    def user_info(self):
        self.age += 10
        self.gender = '男'
        print(f'{self.f_name}{self.l_name}--{self.age}--{self.gender}')

    def greet_user(self):
        print(f'Hello {self.f_name}{self.l_name}')


alice = User('ali', 'ce', 10, '女')
alice.greet_user()
alice.user_info()
