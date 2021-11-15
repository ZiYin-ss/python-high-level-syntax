#  这个对应于Django model的功能  Model是可以指定数据库表的字段的 要是不写默认和属性名一致
#  我们就很少写 因为直接创建表呗 一样就一样呗 但是要知道有这个功能
import numbers


class Field:
    pass


class CharField(Field):
    def __init__(self, db_column, max_length=None):
        self.__value = None
        self.de_column = db_column
        self.max_length = max_length

        if max_length is None:
            raise ValueError("这是一个必填项 为啥不写呢")

    def __get__(self, instance, owner):
        return self.__value

    def __set__(self, instance, value):
        if not isinstance(value, str):
            raise ValueError("类型不对")
        if len(value) > self.max_length:
            raise ValueError("我的最大长度要求在{}你传递了什么呢".format(self.max_length))
        self.__value = value


class IntField(Field):

    def __init__(self, db_column, min_value=None, max_value=None):
        self.__value = None
        self.min_value = min_value
        self.max_value = max_value
        self.de_column = db_column

        #  最大值和最小值为什么不一起写呢 谁又只会判断一个呢
        if min_value is not None and max_value is not None:
            if not isinstance(max_value, numbers.Integral) or not isinstance(min_value, numbers.Integral):
                raise ValueError("参数必须是整形")
            elif max_value < 0 or min_value < 0:
                raise ValueError("参数必须大于零")
            elif min_value > max_value:
                raise ValueError("最大值比最小值小怎么写")

    def __get__(self, instance, owner):
        return self.__value

    def __set__(self, instance, value):
        #  这个是判断设置值的时候 参数是不是正确 上面是检查其他属性的类型检查
        if not isinstance(value, numbers.Integral):
            raise ValueError("类型不对")
        if value > self.max_value or value < self.min_value:
            raise ValueError("我的值要求在{}-{}你传递了什么呢".format(self.min_value, self.max_value))
        self.__value = value


class ModelMetaClass(type):
    def __new__(cls, name, bases, attrs, **kwargs):
        # 将*arg拆包就是这三个东西  name是类名 bases基类 attrs是这个类里面的属性值
        # attrs在这个地方对应的就是User这个类里面的每一个属性值(字段值)
        fields = {}
        for key, value in attrs.items():
            if isinstance(value, Field):  # 为什么要做这次判断 主要是判断属性是不是数据库中的字段 可能有其他字段呢
                fields[key] = value
        attrs_meta = attrs.get("Meta", None)  # Class Meta是不是也是一个属性啊 只不过这个属性是类呗
        _meta = {}
        db_table = name.lower
        if attrs_meta is not None:
            #  这个getattr彻底会了吧 第一个是类名或实例名 第二个是属性名 第三个是默认值 当然 attrs_meta.db_table也可以的 但是没有呢
            table = getattr(attrs_meta, "db_table", None)
            if table is not None:
                db_table = table
        _meta["db_table"] = db_table
        attrs["_meta"] = _meta
        attrs["fields"] = fields
        del attrs["Meta"]
        return super().__new__(cls, name, bases, attrs, **kwargs)

"""
    https://www.cnblogs.com/tkqasn/p/6524879.html 
    这里面也介绍了__init__ 和 __new__
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
class BaseModel(metaclass=ModelMetaClass):
    def __init__(self,*args,**kwargs):
        for key,value in kwargs.items():
            setattr(self,key,value)
        return super(BaseModel, self).__init__()

    def save(self):
        pass
        # 这里面做的就是sql语句的拼接 原生插入数据库的事情


class User(BaseModel):
    # 这个地方一定得知道 就是把__init__这个方法放到父类了  这个和django实现ORM类似
    name = CharField(db_column="", max_length=10)
    age = IntField(db_column="", min_value=0, max_value=100)

    class Meta:
        db_table = "user"  # 默认采用class User 中User的小写


if __name__ == '__main__':
    user = User()
    user.name = "赵强"
    user.age = 20
    print(user.name, end=' ')
    print(user.age)

"""
    这个练习确实不错 
        最大的感受其实就是 
            一切都原生 比如带你写了这个模型类  你发现就是数据的处理限制和一些其他的操作 
            并没有啥  别人处理的方式还是牛逼 
            还有就是上次 虚拟节点生成真实DOM的时候 不还是调用原生的呗 
                只是别人的数据处理确实很牛逼好把 
        __new__和__init__ 差不多了 
        牛

"""