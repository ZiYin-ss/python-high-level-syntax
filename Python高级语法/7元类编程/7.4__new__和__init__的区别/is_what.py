class User:

    def __new__(cls, *args, **kwargs):
        print('aaa')
        return super().__new__(cls)

    def __init__(self, name):
        self.name = name


"""
    再说一遍 这个__new__是新式类 在python2.2之后才有这个方法的
    多说一下 User是类 user对象 user是User的实例 类也是对象
     
    生成user对象之前加逻辑  在__init__之前
    new是用来控制对象的生成过程 在对象生成之前 
    init是用来完善对象的 
    如果new方法不返回对象 则不会调用init函数
"""

user = User("aa")

"""
    我想说的是 假如这个User继承了某个类 那么User的父类中有__new__方法是不是会先执行他 
    然后执行父类的__init__ 再执行子类的__new__ 在执行子类的__init__   
    __new__在框架中用的多 这个__new__方法会在自定义元类中讲解 
"""
