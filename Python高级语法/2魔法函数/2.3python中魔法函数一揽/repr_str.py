class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __str__(self):  # 打印实例会调用这个方法
        return ",".join(self.employee)

    # def __str__(self):
    #   return u'Clazz:%s' % self.cname
    #   这个就是django模型类里面 你写str方法的原理 不是为了让他生成一个你看不懂的这个器 那个器
    #   Django中模型类定义这个 就是为了让你看到当前实例对象(模型类的实例)里面的数据 方便理解
    #   因为模型类查询就会用这个方法 打印实例的数据

    def __repr__(self):
        return 'a'  # 不会打印


#  还有一个就是数学运算的魔法函数 做数据处理用的比较多

# __str__方法
company = Company(['tom', 'bob', 'jane'])
print(company)
# __repr__ 方法
company  # 开发模式会直接调用company  repr方法  在这个解释器是不会做输出的  ipython notebook里面可以用的上
