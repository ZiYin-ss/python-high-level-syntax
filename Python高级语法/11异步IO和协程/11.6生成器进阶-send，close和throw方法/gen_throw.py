def gen_func():
    try:
        yield "http://projectsedu.com"
    except Exception as e:
        pass
    try:
        yield 2
    except Exception as e:
        pass
    try:
        yield 3
    except Exception as e:
        pass
    return "bobby"

if __name__ == "__main__":
    gen = gen_func()
    print(next(gen))  # 网址
    gen.throw(Exception, "download error")
    # 扔进去一个异常  同时这个时候 会next一个出去 把2 next出去了 此时程序走到了yield2后面
    print(next(gen)) #3
    gen.throw(Exception, "download error")