#  什么是生成器函数 函数里只要有yield关键字就是生成器函数
def gen_func():
    yield 1


#   惰性求值 延迟求值提供了可能
#  为什么这样说呢 因为只有计算值的时候才会产生值 意思和当年自己看生成器时候说的一句话很像 保存产生值的表达式也可以保存值


def gen_fib(index):
    re_list = []
    n, a, b = 0, 0, 1
    while n < index:
        yield b
        a, b = b, a + b
        n += 1


def func():
    return 1


"""
    可迭代对象内部实现了__iter__
    迭代器内部实现__iter__和__next__
    生成器的内部也实现__iter__和__next__
"""

if __name__ == '__main__':
    gen = gen_func()  # 返回的是生成器对象 python编译字节码的时候就产生的
    print(gen)  # <generator object gen_func at 0x020AD6B8>
    for va in gen:
        print(va)

    fun = func()
    print(fun)  # 1
