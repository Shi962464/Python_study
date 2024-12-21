def func(x, y):
    print(x, y)


func(1, 3)
func(x=11, y=22)

# 下述的使用类型也是可以的
func(*[11, 33])
func(**{'x': 11, 'y': 22})

def fun(name=None):
    if not name:
        name = '石磊'
    def inner():
        print(name)
        return 'shieli'
    return inner
v1 = fun('aaa')()
# 由于fun函数返回的是inner，inner在fun函数里面是存在的，
# 故在fun('aaa')后面加上()就等于再次调用inner函数
# 所以就将shilei赋值给了v1
v2 = fun()()
# 这里是因为没有传入参数，所以默认赋值为 石磊
print(v1)
print(v2)