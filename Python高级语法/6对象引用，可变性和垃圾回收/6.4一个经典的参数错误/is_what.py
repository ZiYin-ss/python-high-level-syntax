def add(a, b):
    a += b
    return a


class Company:
    def __init__(self, name, staffs=[]):
        self.name = name
        self.staffs = staffs

    def add(self, staff_name):
        self.staffs.append(staff_name)

    def remove(self, staff_name):
        self.staffs.remove(staff_name)


if __name__ == '__main__':
    com1 = Company("aaa")
    com1.add("bobby")

    com2 = Company("bbb")
    com2.add("bobby5")
    print(com1.staffs)  # ['bobby', 'bobby5']
    print(com2.staffs)  # ['bobby', 'bobby5']
    """
        上面是同一个对象 --- 下面的第二个情况 第二个两个列表 发现到最后自己的值改变了 
            上面都同时使用了默认的list(都没有传递list) list本身又可变 所以共用了同一个对象
            com1 -> init里面的self.staffs 指向的是 Company.__init__.__defaults__ 是默认的里面的列表对象
            com2也是指向这个地方 
            假如传递进去了话 就会变
            
        下面的
             print(c)  # [1, 2, 3, 4]
             print(a, b)  # [1, 2, 3, 4] [3, 4]    
            
             这个地方c执行了add函数 是不是改变了 a的值 又因为a是可变的 所以在外面还是改变了啊 
             你看变量和元组就不会变 元组不会变可以理解 为什么变量不会变呢  
                不可变（immutable）: int、字符串(string)、float、（数值型number）、元组（tuple)
                可变（mutable）: 字典型(dictionary)、列表型(list)
            那为什么函数里面可以改呢 那是改为局部了 懂?
    """

    aa = 1
    ab = 2
    ac = add(aa, ab)
    print(ac)  # 3
    print(aa, ab)  # 1 2

    a = [1, 2]
    b = [3, 4]
    c = add(a, b)
    print(c)  # [1, 2, 3, 4]
    print(a, b)  # [1, 2, 3, 4] [3, 4]

    d = (1, 2)
    e = (3, 4)
    f = add(d, e)
    print(f)  # (1, 2, 3, 4)
    print(d, e)  # (1, 2) (3, 4)
