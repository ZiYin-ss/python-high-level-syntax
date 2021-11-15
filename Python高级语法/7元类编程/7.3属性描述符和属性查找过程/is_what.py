from datetime import date, datetime
import numbers


class IntField(object):

    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError("类型不对")
        self.value = value

    def __delete__(self, instance):
        pass


class NonDataIntField:
    #  非数据属性描述符
    def __get__(self, instance, value, owner):
        return self.value


"""
    实现这三个中的任何一个方法就是属性描述符 其实用property和计算属性.setter也可以限制 但是会非常多 
    
    属性描述符就是用来限制属性的
        age = IntField() 
        当外部 user.age = 30时 实际上就是调用IntField()里面set方法 但是值还没有给age 
         def __get__(self, instance, owner):
            return self.value     #直接user.age就会出来
    
         def __set__(self, instance, value):
            if not isinstance(value,numbers.Integral):
                raise ValueError("类型不对")
            self.value = value
            
        怎么理解呢 
            你看上面三个魔法函数的参数 可以理解为 instance是user对象  30就是value
            调用user.age =xx的时候 因为user.age=IntField 
            所以说设置值的时候就是调用IntField这个类的set
            如果这个逻辑处理完 你还user.age 那还走这 所以说直接保存值就可以了 
            user.age调用的就是get方法了 
            不同的属性对应不同的实例 所以说可以达到设置值 读取值 而用户还觉得就是简单的设置读取呢
            
    SQLAlchemy和DJANGO的模型类是不是就是这样做的啊    
"""


class User:
    age = IntField()


if __name__ == '__main__':
    user = User()
    user.age = 30
    print(user.age)

'''
    如果user是某个类的实例，那么user.age（以及等价的getattr(user,’age’)）
    首先调用__getattribute__。如果类定义了__getattr__方法，
    那么在__getattribute__抛出 AttributeError 的时候就会调用到__getattr__，
        ---这个地方的意思是说 
        就是getattribute没有定义的时候 又因为找属性会先调用 肯定报错啊 然后跳到getattr来了
    
    而对于描述符(__get__）的调用，则是发生在__getattribute__内部的。
    user = User(), 那么user.age 顺序如下：
    
    （1）如果“age”是出现在User或其基类的__dict__中， 且age是data descriptor， 那么调用其__get__方法, 否则
    
    （2）如果“age”出现在user的__dict__中， 那么直接返回 obj.__dict__[‘age’]， 否则
    
    （3）如果“age”出现在User或其基类的__dict__中
    
    （3.1）如果age是non-data descriptor，那么调用其__get__方法， 否则
    
    （3.2）返回 __dict__[‘age’]
    
    （4）如果User有__getattr__方法，调用__getattr__方法，否则
    
    （5）抛出AttributeError

'''
