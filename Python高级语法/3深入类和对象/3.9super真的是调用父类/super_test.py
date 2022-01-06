class A:
    def __init__(self):
        print("A")


class B(A):
    def __init__(self):
        print("B")
        super().__init__()


class C(A):
    def __init__(self):
        print("C")
        super().__init__()


class D(B, C):
    def __init__(self):
        print("D")
        super(D, self).__init__()
        # 会先调用前面B的父类 的构造函数 在调用后面C的构造函数  在调用b的父类 和a的父类的
        #  这个是不是很像mro


b = D()

"""
    我们都重写了B的构造函数 为什么还要去调用super呢?
    super().__init__(name=name) 这个写法能看懂把 
    上面这个是调用父类的构造函数 并传递参数进去 所以说 很灵活   
    这个地方 还是提高代码的重用
    
    super函数调用的顺序其实就是mro的顺序 
    其实并不是父类
    而是mro这个顺序里面后一个类的构造函数
    
    
    
"""
