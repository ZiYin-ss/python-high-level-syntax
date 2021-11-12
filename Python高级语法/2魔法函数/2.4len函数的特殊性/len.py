class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]

    def __len__(self):
        return len(self.employee)


company = Company(['tom', 'bob', 'jane'])
len(company)
# 用到 list，dict，set 会非常快 原生数据结构 因为底层是用c语言写的  会有专门的数字 表示长度 所以说不用遍历

"""
注意 len ads 之类的函数 
    是python里面都有的 为什么对对象可以用呢 是因为这个调用的这个类里面 定义了 相对的魔法方法 返回的值
    而你看魔法方法里面 也是return len(xxx)
    从这个地方可以看出一些魔法方法是丰富类的类型 其实就是做一个中间传递器
"""


