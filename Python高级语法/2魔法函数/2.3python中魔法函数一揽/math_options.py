class Nums(object):
    def __init__(self, num, num1):
        self.num = num
        self.num1 = num1

    def __abs__(self):
        return abs(self.num)


my_num = Nums(-1, 1)
print(abs(my_num))


class MyVector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        re = MyVector(self.x + other.x, self.y + other.y)
        return re

    def __str__(self):
        return "x:{x},y:{y}".format(x=self.x, y=self.y)


fir = MyVector(1, 2)
sec = MyVector(1, 2)
print(fir + sec)
# 他两相加的时候 就会调用某一个类的 __add__ 另外一个类 的x和y传进来 然后 print 调用的类的 x和y  就可以
