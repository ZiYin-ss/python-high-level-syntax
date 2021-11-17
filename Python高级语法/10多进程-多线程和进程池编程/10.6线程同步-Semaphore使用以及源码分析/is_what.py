import threading
import time


class HtmlSpider(threading.Thread):
    def __init__(self, url, sem):
        super(HtmlSpider, self).__init__()
        self.url = url
        self.sem = sem

    def run(self):
        time.sleep(2)
        print("get html text success")
        self.sem.release()


class UrlProducer(threading.Thread):
    def __init__(self, sem):
        super(UrlProducer, self).__init__()
        self.sem = sem

    def run(self) -> None:
        for i in range(20):  # 也就是这个地方 同时开了20个这个线程 去运行 也就是说一次进来20个线程
            self.sem.acquire()  # 有获取就有删除
            html_thread = HtmlSpider("aaaa", self.sem)
            html_thread.start()


if __name__ == '__main__':
    sem = threading.Semaphore(3)
    a = UrlProducer(sem)
    a.start()

"""
    Semaphore 是用于控制进入数量的锁
        文件的读写 写一般只用一个线程写(互斥锁) 读可以又多个
        sem = threading.Semaphore(3) 类似与创建3锁
        self.sem.acquire() 这个地方获取了一把锁(sem会减一) 然后进入了类中 在类中逻辑执行完成就会释放一把(sem会加一)
        当for循环了三下之后 是不是sem没有了 就会在这里面阻塞这 当执行的类逻辑执行完了之后会释放一把锁 sem就有了 就会继续执行
        注意这个底层也是用了 Condition的 怎么体现呢 没了wait 执行完了之后释放不就是notify呗 只不过多了点呗
"""

"""
    我有一个点一直没说 就是这个同步 并不是我们理解的那样 一起开始一起走
    而是说在一条线上面 一步一步走完 
    具体的就是说 这个地方拿到的数据 必须要是最新的数据 是上个线程更新完了的数据 
    这就要用锁 GIL因为释放了 所以要锁 线程 保证更新的变量实时更新 这个就是同步
"""