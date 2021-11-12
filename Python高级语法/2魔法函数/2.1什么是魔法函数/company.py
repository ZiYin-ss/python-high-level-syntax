class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):  # 双下划线开头和结尾
        return self.employee[item], item
        # 这个返回的值 必须要让他自己调用 出异常 要不然 返回什么 一直打印
        # 还有就是 getitem 序列化 可以 类名['xx']  for xx in 类名  len(类名) 切片 还有很多自己发现


company = Company(['tom', 'bob', 'jane'])
emploee = company
for em in emploee:
    print(em)

"""
    文件夹里面的init文件就是用来标识这个文件夹是python中的一个包(模块)
    丰富类的类型
"""
