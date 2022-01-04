
from collections import abc
"""
    Sequence 不可变序列类型中的一个
        魔法函数构成序列协议 满足这样那样的魔法函数
    MutableSequence 可变序列类型 
        就是有setitem getitem 等等一些魔法方法

    就是哪些魔法函数构成了序列协议 
        可变的有可变序列的魔法函数 不可变的有不可变序列的魔法函数 
        这个就叫序列协议 

    其实有时候就是说你调用这个类 比如str.split 之类的这种方法 其实还是这个序列 
    有什么方法 然后你调用了

"""