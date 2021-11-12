from collections.abc import Mapping, MutableMapping

a = {}
#  a实现这个协议(MutableMapping)定义的魔法函数 所以可以直接判断
#  我想说的是这个isinstance实例并不是说判断a是不是继承了MutableMapping 而是判断a里面有没有遵守这个协议(MutableMapping)
#  从而返回false或者true 是这个意思 注意哦
print(isinstance(a, MutableMapping))

"""
    字典是Mapping类型 其实dict和list很多是一样的 其实都是继承了Collection类
    然后再添加了自己的方法

"""
