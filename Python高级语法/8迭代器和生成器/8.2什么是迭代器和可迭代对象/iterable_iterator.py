from collections.abc import Iterator


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __iter__(self):
        return MyIterator(self.employee)


"""
 为什么不在自己这个类里面写呢(编程规范) 将这个类型 返回一个迭代器 
"""


# def __getitem__(self, item): 这个变成一个可迭代对象
#     return self.employee[item]


class MyIterator(Iterator):
    def __init__(self, employee_list):
        self.iter_list = employee_list
        self.index = 0

    def __next__(self):
        # 真正返回迭代值的逻辑
        try:
            word = self.iter_list[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word


if __name__ == "__main__":
    company = Company(["tom", "bob", "jane"])
    my_itor = iter(company)  # 内部要是没写 __iter__的话就会找到getitem
    # while True:               这个地方其实是走的是下面for循环里面的的逻辑
    #     try:
    #         print (next(my_itor))
    #     except StopIteration:
    #         pass

    # next(my_itor)
    for item in company:
        print(item)
"""
    什么是迭代器 
        实现了__next__方法
    什么是可迭代对象的  
        实现了__iter__方法
        
    如果要让一个对象变成一个迭代器 需要让一个迭代器正常工作也需要实现这两个方法的 
     那么这两个方法都要实现 
    
"""