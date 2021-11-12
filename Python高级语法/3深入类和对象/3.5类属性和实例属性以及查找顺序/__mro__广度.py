#  python2中object不写 就不会继承这个类
#  但是python3不写的话 也会继承 这个东西叫做新式类
class D:
    pass


class C(D):
    pass


class B(D):
    pass


class A(B, C):
    pass


# (<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>, <class 'object'>)
print(A.__mro__)  # 这个继承顺序
