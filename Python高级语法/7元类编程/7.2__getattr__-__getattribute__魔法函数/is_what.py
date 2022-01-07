from datetime import date


class User:
    def __init__(self, name, birthday, info={}):
        self.name = name
        self.birthday = birthday
        self.info = info

    def __getattr__(self, item):
        return self.info[item]

    def __getattribute__(self, item):
        return item


if __name__ == '__main__':
    user = User("bobby", date(year=1987, month=1, day=1), info={"com": "imooc"})
    print(user.com)
    print(user.__dict__)

"""
    __getattr__  
        在查找不到属性的时候调用
        print(user.age) 查找不到的时候会调用自己重载的__getattr__ 添加逻辑
        看这个地方的用法
            user = User("bobby",date(year=1987,month=1,day=1),info={"com":"imooc"})
            print(user.com)
        
             def __getattr__(self, item):
                return self.info[item]
        查找不到就会调用自己重载的__getattr__有值就会返回 如果没有写 就会报错
            
    __getattribute__
        最开始执行 就是查找属性的时候 会最先调用这个
        用法
            user = User("bobby",date(year=1987,month=1,day=1),info={"com":"imooc"})
            print(user.com)
            
            def __getattribute__(self, item):
                return item
        这个你看 我user.com 打印的是com 会在查找属性的时候 最先调用这个 return就不会往下执行了 
        为什么说这个呢 就是直到这个数据的出口和入口在哪 可以做一些东西
        当然肯定很少用这个的 框架用控制实例
    
    https://www.cnblogs.com/nickchen121/p/10990781.html
    这个网站介绍了 getattr setattr hasattr这个几个魔法函数的作用 
    我就不说了 可以去看一下
        hasattr：判断一个方法是否存在与这个类中
        getattr：根据字符串去获取obj对象里的对应的方法的内存地址，加"()"括号即可执行
        setattr：通过setattr将外部的一个函数绑定到实例中
        delattr：删除一个实例或者类中的方法
        getattr(obj, name[, default]) : 访问对象的属性。
        hasattr(obj,name) : 检查是否存在一个属性。
        setattr(obj,name,value) : 设置一个属性。如果属性不存在，会创建一个新属性。
        delattr(obj, name) : 删除属性。
"""
