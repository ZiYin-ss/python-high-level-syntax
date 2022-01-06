class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @staticmethod  # 这个和普通函数一样 只不过要加个Date 这个地方不用加self
    def parse_from_string(data_str):
        year, month, day = tuple(data_str.split("-"))
        return Date(int(year), int(month), int(day))

    @classmethod  # cls 是当前这个类的对象 self是当前实例的对象
    def from_string(cls, data_str):
        year, month, day = tuple(data_str.split("-"))
        return cls(int(year), int(month), int(day))

    def tomorrow(self):
        self.day += 1

    def __str__(self):
        return "{year}/{month}/{day}".format(year=self.year, month=self.month, day=self.day)


new_Day = Date(2018, 12, 31)
new_Day.tomorrow()
print("sss", new_Day)
date_str = "2018-12-31"
new_day = Date.parse_from_string(date_str)
print("sssddddd", new_day)

"""
    python中类的方法有三种 静态方法 类方法 对象方法(实例方法)
        上面的__str__ __init__ 这些都是实例方法 自己定义的方法 也是实例方法 有self 这些大部分都是实例方法 
            因为是对实例进行操作吗
            new_Day.tomorrow() 在底层调用其实是 tomorrow(new_Day) 是这样调用的 这个new_Day里面的day不就是21吗
            self很像js中的this
        上面的parse_from_string(data_str) 是静态方法 用@staticmethod 修饰
            注释写这了 这个函数返回了 一个Date的实例 但是如果你这个Date改为其他的了 你这个硬编码还能行吗 不行了吧
            这个静态方法就是把这个类有关的配置方法 放到里面 然后你去调用返回了什么东西
            有很多地方都是这样做的 Django和Flask中包括Scrapy框架 都有这样的使用 静态方法返回了一个这个类的实例
        针对静态方法的缺陷 出来了类方法 
            上面的from_string(cls,data_str): 就是类方法
            注意类方法不止是这一种使用方式 只要您能想到的方法 遵循规矩 就可以使用
        但有了类方法   为什么还有静态方法
            比如判断一些东西或者直接在里面做一些固定的事或者返回的不是这个类有关的东西 
            是不是就可以用静态 代码也少
        
        这个里面的self和cls 不是固定的 第一个参数就是这个东西  
            
        
        tips
            硬编码软编码不是固定的知道吗  
                就比如
                    Date(int(year), int(month), int(day)) 
                    这个Date就是硬编码  和类名一样
                什么是软编码呢 
                    用一个变量存储实际的值 就比如templates里面是不是经常就写一个BASE_DIR
                    这个BASE_DIR是不是就是一个变量 获取当前根目录 在其他环境里面是不是也可以获取 这个就是软编码 
                    不止是这一种方法
"""
