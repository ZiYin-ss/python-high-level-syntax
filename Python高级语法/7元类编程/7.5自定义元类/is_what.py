def create_class(name):
    if name == "user":
        class User:
            def __str__(self):
                return "user"

        return User
    elif name == "commpany":
        class Company:
            def __str__(self):
                return "company"

        return Company


class BaseClass:
    def answer(self):
        return "你好"


class Metaclass(type):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)


class User(metaclass=Metaclass):
    pass


"""
    我不是说这个metaclass有什么用吗
        metaclass=Metaclass
        第一点创建类的类(Metaclass继承type类) 然后这个类就是元类可以用来创建类
        第二点是用来控制User类(那个类的metaclass指向那个类)的实例化的过程
           user = User() 说的是这个时候 
            
    python中类的实例化的过程 会首先寻找metaclass 通过metaclass去创建user类
        type去创建类对象 
    
    如果继承类的metaclass有指向 和自己类的metaclass有指向 会先找自己的 如果自己没有就找父类 再没有找父类 最后才用type
    
    __init__ 方法负责将该实例对象进行初始化，在对象被创建之后调用该方法，
    在__new__方法创建出一个实例后对实例属性进行初始化。__init__方法可以没有返回值。
    
    首先:对象=类()这时候就调用了call(调用类)方法
    也就是说先执行继承类的new，init，call，在执行自己的new，init
    但是这个metaclass里面的new是不是就是创建类的啊 创建类的时候执行 
    那么我能不能把User(假如创建的类是User)里面的__new__ 移到metaclass里面去做 让他去调用User的父类啊 
           def __new__(cls, name,bases,attrs,**kwargs):
                pass   这个bases就是基类
    可以
    当然还可以做其他工作
    

"""


def say(self):
    return self.name


if __name__ == '__main__':
    # myClass = create_class("user")
    # my_obj = myClass()
    # print(type(my_obj))

    #  type 动态创建类  实际中肯定用 metaclass == xxxx
    User = type("User", (BaseClass,), {"name": "user", "say": say})
    my_obj = User()
    print(my_obj.name)
    print(my_obj.say())
    print(my_obj.answer())

"""
    什么是元类
        元类是创建类的类
        为什么会这样说呢 因为类他也是个对象 创建对象是不是也需要个东西
        注意哦类 有一个继承 有一个元类 注意是不影响的 
"""


"""
    经过研究可知
        type是在创建类的时候调用 
        这个创建类你得理解 user = User()  是这个时候创建类 而不是什么写出来创建类 除了这个时候你能创建类 你还咋创建类啊 
        那么 明白这个 明白__new__和__init__ 方法不就不难了吗 
        用元类创建类(主要做的就是产生几个属性) ModelMetaClass 这个__new__方法接收到得参数不就是你User(xxxx) 
        这里面得xxxx吗 这个有返回值或者调用父类才可以走到__init__   
        __new__创建这个类 主要是一些前置操作 
        __init__这个里面做的是初始化 
        这个是元类的流程 走通了 
        
        假如自己是子类 调用__new__方法 是什么原理呢 
            其实这个地方就很好理解了 因为这个地方和元类那走的是差不多的
            也是提前做一些  前置操作  
            然后调用父类的__new__不是固定操作吗 自己__new__之后 搞父类的 主要是为了打通这个流程 
            这个地方 return 也是可以的啊  
        
        就这了 
        彻底懂了
"""