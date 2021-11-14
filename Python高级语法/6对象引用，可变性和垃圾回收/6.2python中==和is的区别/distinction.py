a = [1, 2, 3, 4]
b = [1, 2, 3, 4]

print(a is b)  # False
print(a == b)  # True

# 但
a = 1
b = 1
print(id(a) == id(b))  # True



class Person: #全局唯一对象
    pass

person = Person()
if isinstance(person,Person): #true
    print("yes")
if type(person) is Person:  #true
    print("yes")
"""
    为什么可以这样用呢 类本身也是一个对象 全局唯一对象  type的时候指向这个Person
"""

"""
    因为intern机制
    为什么会这样呢 
        因为对于小整数 就把一定范围的小整数保存起来(建立全局唯一对象)
        下次再用的时候 其实是指向之前创建的1
        字符串也是如此 
    但是列表不会
    
    总结
        也就是说 is是用来判断是不是同一个对象的(a=b(地址))  而 == 是用来判断值是不是一样的  
"""
