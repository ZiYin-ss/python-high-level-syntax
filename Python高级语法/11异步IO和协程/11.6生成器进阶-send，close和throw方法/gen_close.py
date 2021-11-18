def gen_func():
    try:
        yield "http://projectsedu.com"
    except GeneratorExit:
        pass
    yield 2
    yield 3
    return "bobby"

if __name__ == '__main__':
    gen = gen_func()
    print(next(gen))
    gen.close()  # 结束生成器 假如还有next就会抛异常
    next(gen)  # 没有yield的话 就StopIteration


"""
    注意上面try--except为什么捕获不了异常了 
        以前假如有这个异常是会捕获到的  显示我们自定义数据
    GeneratorExit 继承自BaseException(比Except还基础)
"""

