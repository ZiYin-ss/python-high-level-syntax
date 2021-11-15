
class Person:
   name = "user"

class Student(Person):
    def __init__(self,school_name):
        self.school_name = school_name


user = Student("慕课网")
print(user.__dict__)
print(dir(user))
"""
    自省是通过一定的机制查询到对象的内部结构 这就是自省 没什么高深的说法
    这个__dict__可以获取实例或者类的属性 查看自身的结构 
    user.__dict__["xxx"] = xxx 可以直接修改类中或实例中的某些属性
    dir这个比dict要牛 因为哪怕是一个变量都可以看里面有什么属性 
    
    类的静态函数、类函数、普通函数、全局变量以及一些内置的属性都是放在类__dict__里的
    对象的__dict__中存储了一些self.xxx的一些东西
    
    1） 内置的数据类型没有__dict__属性
　　 2） 每个类有自己的__dict__属性，就算存着继承关系，父类的__dict__ 并不会影响子类的__dict__
　　 3） 对象也有自己的__dict__属性， 存储self.xxx 信息，父子类对象公用__dict__   

    user对象的__dict__放的是self 赋值的值
    这个对象的对应的类 的类变量是放到类的__dict__中的  
"""

