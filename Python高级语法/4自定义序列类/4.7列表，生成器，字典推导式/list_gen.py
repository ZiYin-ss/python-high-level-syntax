# 列表推导式 列表生成式

print('-----------------------------------------')

"""
    列表推导式
    这个 x是range中的参数 最后的if是条件
    意思是 生成一个列表 x是列表的元素 x范围是0-20 而且x要是奇数
"""
odd_list = [x for x in range(21) if x % 2 == 1]
print(odd_list)

""" 
    复杂的逻辑情况
        定义一个函数  也就是说定义一个函数 然后在列表生成式里面使用这个函数 
        注意 看下面函数的位置 不一定写这个地方 还可以写for里面 if里面
    列表生成式性能高于列表操作  但是真的太复杂了的话 也不用列表生成式
"""


def hadle_item(item):
    return item * item


odd_list = [hadle_item(x) for x in range(21) if x % 2 == 1]
print(odd_list)
print('-----------------------------------------')

"""这个是匿名函数"""
func = lambda x, y: x if x > y else y
fun = lambda x, y, z: x + y + z
print(fun(1, 2, 3))
print('-----------------------------------------')

"""生成器表达式"""
"""
    将列表推导式的这个中括号改为小括号就是生成器表达式了
"""
odd_list = (hadle_item(x) for x in range(21) if x % 2 == 1)
print(type(odd_list))  # <class 'generator'>
print(odd_list)  # <generator object <genexpr> at 0x01E51F08>
for item in odd_list:
    print(item)
odd_lis = list(odd_list)  # 可以直接这样把生成器改为list
print('------------------------------------------')

"""字典推导式 """
"""
    和list很像 
    注意 字典取key value的话 你得字典.items()
"""
my_dict = {"bobby1": 22, "bobby2": 23, 'imooc.com': 5}
reversed_dict = {value: key for key, value in my_dict.items()}
print(reversed_dict)
print('------------------------------------------')

"""集合推导式"""
my_set = {key for key, value in my_dict.items()}
print(type(my_set))
print(my_set)
print('------------------------------------------')
