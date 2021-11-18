def gen_func():
    yield 1
    yield 2
    yield 3
    return "bobby"


# 生成器不止可以产出值 还可以接收值
def gen_func1():
    #  这个地方先产出值  再接收值
    html = yield "http://projectsedu.com"
    print(html)
    yield 2
    yield 3
    return "bobby"


if __name__ == '__main__':
    """
        gen = gen_func()
        print(next(gen))
            这个地方 就是gen是生成器(生成器函数生成的吗) 所以可以next一下 让他yield一个值 再next的话又是下一个yield值
            当然 for循环也是可以的 每for一次就可以yield一次
        print(next(gen))
        print(next(gen))
        print(next(gen))
    """

    gen1 = gen_func1()  # 生成器一开始的时候只能send None
    #  再send发送非none值之前 必须启动一次生成器 next send(None)
    url = next(gen1)
    print(url)
    html = "bobby"  # 这个会传到 里面html = yield 变量那 因为yield可以接收的吗 就是yield=html(传进来的) 后来给了里面的html
    gen1.send(html)  # send方法可以传递值进入生成器内部 同时还可以重启生成器执行到下一个yield
