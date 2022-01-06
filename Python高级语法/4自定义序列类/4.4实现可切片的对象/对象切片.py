import numbers


class Group:
    def __init__(self, group_name, company_name, staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    def __reversed__(self):
        return self.staffs.reverse()

    def __getitem__(self, item):
        cls = type(self)
        if isinstance(item, slice):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=self.staffs[item])
        elif isinstance(item, numbers.Integral):
            #  整数直接取出来得是值啊  但是接收得是数组
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=[self.staffs[item]])

    def __len__(self):
        return len(self.staffs)

    def __iter__(self):
        return iter(self.staffs)

    #  if xxx in 这个类的实例 就会调用这个方法呢 判断在不在里面
    def __contains__(self, item):
        if item in self.staffs:
            return True
        else:
            return False


staffs = ["bobby1", "imooc", "bobby2", "bobby3", ]

group = Group(company_name='imooc', group_name="user", staffs=staffs)

print(group[:2])
# 这个时候因为实现了getitem 所以说不会报错 可以直接这样用
#  这个item参数是什么  是一个切片 这个地方是切片
#  group[0] 这个地方又是int类型 所以说都得实现


"""
    这个是不可修改的 假如要是可修改的是不是直接修改一下里面的魔法函数 
    也就是说上面实现的是不可修改的序列
    比如django的queryset实现了getitem 可以直接切片啊
    其实由上面可以看出 这些类实现类这个那个方法  其实底层还是调用最基本的方法
    看上面的方法 就是实现对象切片的基本步骤
"""
