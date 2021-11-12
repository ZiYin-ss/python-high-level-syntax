# frozenset 不可变集合  无序 不重复 也就是说常用来去重

s = set("abcdeeff")  # {'f', 'd', 'e', 'b', 'c', 'a'}
print(s)

a = {"a", "b"}  # 这个也是集合 不要认为是字典
a.add('c')  # 集合也是可以变的 不可变集合才不可以变
print(a)
print(type(a))

b = frozenset("abcde")  # frozenset可以作为dict的key 因为不可变吗
print(b)


c = set("def")
d = set("abc")
d.update(c)  # 将两个集合连接在一起
print(d)


e = {'a','b','c'}
f = set("cef")
re = e.difference(f)
rs = e - f   # 差集
rd = e & f   # 交集
rc = e | f  # 并集
print(re)

"""
    注意 
        集合中有 add clear update remove pop 很多很多 
        difference 差集
            re = e.difference(f) 
            显示e中有而f中没有的数据 单方面差集 
            这个集合也是交并补的 有对应的函数
        set 去重性能很高
"""