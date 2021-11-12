a = 1
b = "abc"
print(type(1))  # <class 'int'>
print(type(int))  # <class 'type'>
print(type(b))  # <class 'str'>
print(type(str))  # <class 'type'>
print(type(type))
"""
    type->int->1
    type->class(str类型)->obj(b="abc" 这个b就是obj)
"""


class Student:
    pass


stu = Student()
print(type(stu))  # <class '__main__.Student'>
print(type(Student))  # <class 'type'>
"""
    由此也可以看出 type->class(Student)->obj(stu)
    type(类对象)用来生成类的 
        自定义type类 Flask中分析wtform源码的时候 看过 继承自type metaclass=xxx  meta方法
        也就是说自定义类包括内建的类 都是由type类生成的对象
        type类本身也是由type生成的
    先明确一个概念 我们通常说的 obj是指 这个a=xxx 这个a代表的对象 object是指所有类都继承的那个类
    object类 最顶层的类
        如果自定义类不写继承关系 默认继承object类 
        就算继承了其他类 其他类走到最后还是继承object类  用 类名.__bases__  查看
        object的基类是空
    type和object的关系
        type类的基类是object  object类是由type生成的
        和TM js的Function和Object相似 虽然我都不知道
    
    为什么要这样设计呢 因为想设计为 都是对象模式 方便修改
"""