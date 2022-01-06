class D:
    pass


class E:
    pass


class C(E):
    pass


class B(D):
    pass


class A(B, C):
    pass


# (<class '__main__.A'>, <class '__main__.B'>, <class '__main__.D'>,
# <class '__main__.C'>, <class '__main__.E'>, <class 'object'>)
#  这个是深度优先的 其实你也看出来的 这个和前面广度优先的话 也很类似 因为都继承了object 所以说还是使用了C3算法
print(A.__mro__)
