class A:
    pass


class B(A):
    pass


b = B()

print(isinstance(b, B))  # true
print(isinstance(b, A))  # true

print(type(b) is B)  # true
print(type(b) is A)  # false

#  注意 is和"=="   is是看二者的地址是否一样
#  所以说你看这个地方 就知道 type(b)其实是A的一个类 所以说有误差拉 ==是看值是否相等
#  使用isinstance  用type会有误差
