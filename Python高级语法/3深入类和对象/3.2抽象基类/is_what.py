# coding = "utf-8"
# 动态语言只能在运行的时候才会发现错误
from collections.abc import Sized


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)


com = Company(['con', 'tom', 'bobby'])
print(len(com))
#  判断这个类能否有长度 或者调用len函数  或者叫做判断这个类是否有某一个属性
print(hasattr(com, "__len__"))

isinstance(com, Sized)  # 更喜欢用这种我们更喜欢判断是否是一个类型 而不是用hasattr
#  这个函数 还会找到继承链  假如 A实现B 那么就可以判断 B属于A  更深层次的解释 就是说还是关注鸭子类型 有什么就是什么


"""
    python当中基于鸭子类型来设计的
        这个东西是真的非常非常难理解 就是这个鸭子类型 就是关注类能解决问题就可以了
    抽象基类 其实很抽象
        在这个基础的类当中，我们去设定好一些方法 所有继承这个基类的类 都必须覆盖这个抽象基类的方法
        这个基类是无法进行实例化的
        作用是定义子类应该实现的一组抽象方法
    鸭子类型(补充)
        就是只关注能不能解决问题 只需要实现某个魔法函数 类就具有某种类型的对象
        上面说的只需要实现什么 就是什么类型(事先约定好的) 其实这个不就是协议吗
        所以说这个也叫做协议   编写代码要足够遵守协议  
    可以直接用鸭子类型去设计这个类不就可以了吗 为什么还需要抽象基类呢?
        我们在某些情况之下希望判定某个对象的类型
            isinstance(com,Sized)
        我们需要强制某个子类必须实现某些方法 
            用abstractmethod去标识
            或者举个例子 
                你用某些框架的时候 是不是必须要在某个类里面写了某些必须要写的方法 这个不就是抽象基类吗
                要不些就报错 这个也是约定俗称啊
                            
    抽象基类的示范这个图片里面的程序就是抽象基类
        用abstractmethod去标识 
        instance 只要需要判断的类 或者实例里面 实现了 __len__方法 他就是true 就属于这个类型
            isinstance(com,Sized)
        其他的与这个类似就是了  
        还有就是如果你直接继承这个类 Sized的话 必须重写def __len__方法 要不然报错
    
    总结
        不要看抽象基类说的很高大上 
        其实很简单  
            就是类型判断 必须实现某些方法
            用的很少 不是用来继承的 是用来了解继承关系的  和接口的定义
        不要看鸭子类型 说的很晦涩 
            其实就是只关注这个类实现了什么功能 他就是什么
            这个用的还是很多
"""


#  实现抽象基类
import abc
# class CacheBase:
#     def get(self, key):
#         raise NotImplementedError
#      这个地方也可以实现抽象基类 的功能 你不重新 你调用 就会报错
#     def set(self, key, value):
#         raise NotImplementedError


class CacheBase(metaclass=abc.ABCMeta): # 这个metaclass必须要等于abc.xxx 不这样的话实现不了抽象基类
    @abc.abstractmethod  # 加上了这个 你不重写就会报错
    def get(self, key):
        pass

    @abc.abstractmethod
    def set(self, key, value):
        pass

class RedisCache(CacheBase):
    def set(self, key, value):
        pass


redis_cache = RedisCache()
# redis_cache.set('zz', 123)   # 这个地方只有在调用set的时候才会抛异常 我们想直接抛异常
