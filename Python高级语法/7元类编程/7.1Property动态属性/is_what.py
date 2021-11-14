from datetime import date, datetime


class User:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self.__age = 0  # 双下划线会重命名 这样才会达到内部私有的 外部不能直接修改
        # self._age = 0 这样不会报错的 约定为私有方法 但是外部可以访问的 没有太大意义 但是双下划线不可以 外部无法访问 我们只能函数修改

    def get_age(self):
        #  datetime.now() 也是year-month-day  所以说日期是可以做加减的 我就是说一下 没用过
        return datetime.now().year - self.birthday.year

    @property
    #  self.age = 0 如果此时 init还有age就会报错
    #  这个叫计算属性 也就是说 实例.age 就是访问这个函数 打印的值就是这个函数的返回值
    #  也就是说通过属性 达到调用函数的目的 让别人觉得 也就是调用属性的
    #  其实在Vue和React中是不是也有计算属性啊 也是一样把 调用函数名就可以 相当于执行了
    def age(self):
        # return datetime.now().year - self.birthday.year
        return self.__age

    @age.setter
    def age(self, value):
        self.__age = value

    """
        也就是说 这个property这个使用来装饰这个函数为计算属性 通过 实例.age 调用
        而age.setter 这个方法是设置age的 这个地方注意一下 其实这个age是对应被property装饰的函数名的
            并不是对应__age 通过 user.age = 10 调用
        这两个函数 
            里面我们就可以读取内部变量 内部想暴露的 
            设置内部的变量之类的操作 
    """


if __name__ == '__main__':
    #  这个date就是时间 year-month-day
    user = User("bobby", date(year=1987, month=1, day=1))
    user.age = 10
    print(user.age)
