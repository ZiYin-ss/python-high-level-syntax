class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @staticmethod
    def parse_from_string(data_str):
        year, month, day = tuple(data_str.split("-"))
        return Date(int(year), int(month), int(day))

    @classmethod
    def from_string(cls, data_str):
        year, month, day = tuple(data_str.split("-"))
        return cls(int(year), int(month), int(day))

    def tomorrow(self):
        self.day += 1

    def __str__(self):
        return "{year}/{month}/{day}".format(year=self.year, month=self.month, day=self.day)


class User:
    def __init__(self, birthday):
        self._User__birthday = None
        self.__birthday = birthday

    def get_age(self):  # 假如这个birthday是日期形式 2018/11/11 birthday.year就是2018
        return 2018 - self.__birthday.year
        # 双下划线 这样你就访问不到birthday了 无法通过实例访问 子类也不行 这个就是私有属性
        # 函数前面双下划线 是私有方法
        # 这些私有属性和方法 并不是真的私有了  只是把他们的名字改为了 _classname__函数名(或者变量名) 通过这个还是可以调用
        #        数据封装没有说 只是 这个私有属性体现的就是数据封装


user = User(Date(1990, 2, 1))
print(user._User__birthday)
print(user.get_age())
