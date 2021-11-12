
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
"""

