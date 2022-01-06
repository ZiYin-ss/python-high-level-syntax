def ask(name="boby"):
    print(name)


class Person:
    def __init__(self):
        print('bobby')


my_func = ask
my_func('赵强')
my_class = Person
my_class()

"""
    对象可以赋值给一个变量
        my_func=ask
        my_class = Person
    也可以放进一个数组,也可以添加到集合中 
        obj_list.append(ask)
        obj_list.append(Person)
    还可以作为函数的返回值
        def decorator_func():
            print("desc")
            return ask
        ma = decorator_func()
        ma()
"""

obj_list = []
obj_list.append(ask)
obj_list.append(Person)
for item in obj_list:
    print(item())  # 函数没有返回值 所以说打印函数就会返回none值 但和执行函数不一样的


def decorator_func():
    print("desc")
    return ask


ma = decorator_func()
ma()
