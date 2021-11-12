class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]

    def __len__(self):  # print(len(company))
        return 2


company = Company(['tom', 'bob', 'jane'])
emploee = company
for em in emploee:
    print(em)

company1 = company[:1]  # 使用了 getitem还可以进行切片操作 序列类型
for em in company1:
    print(em)

# len(类名) 这个会去找类里面的__len__方法 调用它 看返回值是多少 没有就会找getitem
# 因为getitem变为了序列类型 就会统计 getitem里面返回的数据的长度
print(len(company))


"""
    这个魔法函数就是数据模型的一个概念而已
    会识别这个对象或自定义类里面的魔法函数 
    这个魔法函数的调用 不是显示的调用 而是隐式的调用 每个类都可以存在
    加入这些魔法方法 会增加我们自定义类的类型 比如自定义类 可以丰富为迭代类型，序列类型 
    就是变得很神奇 直接影响语法本身
    company1=company[:1]
"""
