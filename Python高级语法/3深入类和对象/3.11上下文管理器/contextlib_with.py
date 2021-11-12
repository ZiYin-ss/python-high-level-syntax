import contextlib

@contextlib.contextmanager
# 可以将函数变成上下文管理器 必须是生成器形式  利用了生成器的形式
def fille_open(file_name):
    print("file_open")  #enter
    yield {}
    print("file_end")   #exit


with fille_open("aa.txt") as f_opened:
    print("file")
    #  运行结果
    # file_open
    # file
    # file_end