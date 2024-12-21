# def greet_name(name):
#     print(f'hello \n' +name.title())
#     return name
# ipt_name=input(":-:-:--++:")
# greet_name(ipt_name)


# def des_per(animal_type, pet_name):
#     print("i have a {}".format(animal_type))
#     print("My {} name is {}".format(animal_type, pet_name.title()))
#
#
# des_per(pet_name='alice',animal_type='dog')

# 默认参数
# def get_name(f_name, l_name, middle_name=' '):
#     if middle_name:
#         full_name = f"{f_name} {l_name} {middle_name}"
#     else:
#         full_anme = f"{f_name} {l_name}"
#     # full_name='{} {}'.format(f_name,l_name)
#     return full_name.title()
#
#
# mess = get_name('jimi', 'alice', 'lee')
# print(mess)
# mess = get_name('jimi', 'alice')
# print(mess)


# 返回字典
# def get_person(f_name, l_name):
#     person = {"first": f_name, "last": l_name}
#     return person
#
#
# result = get_person('jimi', 'alice')
# print(result)
# for x, y in result.items():
#     print(f'key:{x}')
#     print(f'value:{y}')


# def get_person(f_name, l_name):
#     person = {"first": f_name, "last": l_name}
#     return person
#
#
# print('name is :')
# f_name = input('f_name:')
# l_name = input('l_name:')
# result = get_person(f_name, l_name)
# print(result)


# 传递列表
# def get_uesr(names):
#     for i in names:
#         mess=f'Hello {i.title()}'
#         print(mess)
# username=['king','jimi','alice']
# get_uesr(username)

# 修改列表
# a = ['11', '22', '33', '44']
# b = []
# while a:
#     c = a.pop()
#     print(c)
#     b.append(c)
# for i in b:
#     print(i)


# def make_pizza(*args, **kwargs):
#     for i in args:
#         print(i)
#     # for a, b in kwargs.items():
#     #     print('{}:{}'.format(a.title(), b.title()))
#     print(kwargs)
#
# make_pizza('mush', 'green', 'extra', name='s', f_name='shi', l_name='lei')


# def build(f, l, **kwargs):
#     kwargs['f_name'] = f
#     kwargs['l_name'] = l
#     return kwargs
#
#
# user_name = build('shi', 'lei', a='1', b='2', c='3')
# print(user_name)


# 结合pizza.py使用
import pizaa

pizaa.make_pizaa('16', 'peppar', 'king', 'alice', 'alce')

from pizaa import make_pizaa

make_pizaa('16', 'a', 'b')

from pizaa import make_pizaa as make

make('111', 'bbb', 'aa')

from pizaa import *

make_pizaa('99', 'eeeee', 'bbbb')
