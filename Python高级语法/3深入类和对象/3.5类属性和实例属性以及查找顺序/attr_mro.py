class A:
    name = "A"  # 这个地方定义的都是类属性

    def __init__(self):   # 这个就是放到类的实例的属性上面去的值 这个里面定义的是 实例属性
        self.name = "obj"


a = A()


# 这个name 会先去自己的a这个实例里面找 有没有name属性 是有的obj 如果没有才会去找A这个类的类属性
print(a.name)

"""
    多继承的情况呢  那么会去找那个类属性呢   
    mro算法 Method Resolution Order（方法解析顺序）
    这个是遵循算法逻辑的 
    一开始是
        DFS深度优先算法 
            就是先沿着一条线查找到底  但这对于菱形搜索 没法整 看图就知道了吗 
        后来成为了BFS广度优先算法  
            一层一层的搜索 一层搜索完了 再去搜索上一层
            但是 这个子类 和另一个父类方法重名了怎么办呢? 又没法整
    所以从python2.3开始用上了C3算法
        
"""