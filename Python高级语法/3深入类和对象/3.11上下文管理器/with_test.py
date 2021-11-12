try:
    f_read = open('aaa.txt')
    print("code started")
except KeyError as e:
    print('key error')
else:
    print('other error')
finally:
    print('finally')
    f_read.close()


class Sample():
    def __enter__(self):
        #  获取资源
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        #  释放资源
        print("exit")

    def do_something(self):
        #  做什么
        print("doing something")


with Sample() as sample:  # 定义好这个类 就可以直接使用
    sample.do_something()

"""
    这个 try----finally  其实这个finally就是一般做一些释放资源的事情
    with语句就是为了简化try----finally的  上下文管理器
        遵循上下文管理器协议
        上面类的执行是  __enter__  do_something  __exit__
        可以直接用with语句可以执行   打开文件 with xx 是不是也是自己内部写了 exit
   上下文管理器用的就是 __enter__和__exit__ 这内置两个方法
"""