"""
首先不建议继承dict和list

"""


class Mydict(dict):
    def __setitem__(self, key, value):
        #  这个是调用父类的 setitem方法 这个setitem 不就是设置字典的呗
        super().__setitem__(key, value * 2)


my_dict = Mydict(one=1)
print(my_dict)  # {'one': 1}  这个地方就是压根没有调用我们覆盖的方法 直接执行父类的setitem
my_dict["one"] = 1
print(my_dict)  # {'one': 2}

"""
    有时候不会调用我们覆盖的方法
"""

from collections import UserDict


class Mydict1(UserDict):
    def __setitem__(self, key, value):
        #  这个是调用父类的 setitem方法 这个setitem 不就是设置字典的呗
        super().__setitem__(key, value * 2)


"""
    这个可以覆盖父类的方法 类似于重写了 dict类
"""

"""
    defaultDict()
    其实底层重写了__missing__方法 设置默认值呢

"""


