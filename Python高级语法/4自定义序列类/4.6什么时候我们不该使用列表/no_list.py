import array

my_array = array.array("i")
my_array.append(1)
# my_array.append("abc")  # 这个会报错
print(my_array)
"""
    array和list的区别
        array只能存放指定的数据类型
        array的性能要比list高
    还有就是array的方法和list方法很类似 需要用到可以自己看
"""