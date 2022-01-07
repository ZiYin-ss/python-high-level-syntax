import threading
import time


class GetDetailHtml(threading.Thread):
    def __init__(self, name):  # 实现多线程用类的方式的时候 最好还是实现一下super() 调用一下父类的init方法
        super().__init__(name=name)

    def run(self):
        print("get detail html started")
        time.sleep(2)
        print("get detail html end\n")


class GetDetailUrl(threading.Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("get detail url started")
        time.sleep(2)
        print("get detail url end\n")


if __name__ == '__main__':
    thread1 = GetDetailHtml("getdetailHtml")
    thread2 = GetDetailUrl("getdetailUrl")
    start_time = time.time()
    thread1.start()
    thread2.start()
    """
        这个地方继承了threading.Thread类 把这个类变成了可以多线程的类
        然后直接 实例.start()就开为多线程了 其实也是一个伪多线程 
        注意必须要重写run方法 相当于开了多线程之后要有他的逻辑 所以说会走run函数实现逻辑(爬虫真正爬取的时候就在这把)
        还可以定义一些方法 然后我们在run中调用 多线程爬虫是不是就是这样写的 
        调用父类的init方法是个好习惯
        继承类 实例.start就可以 run方法
        有没有发现和原来方法一的那种一模一样啊 
            这个就是继承的好处 明明这个类是Get 但和Threaing一样用 这个GET类就是Threaing的子类所以差不多
        线程池用方法一
    """

    print(time.time())
