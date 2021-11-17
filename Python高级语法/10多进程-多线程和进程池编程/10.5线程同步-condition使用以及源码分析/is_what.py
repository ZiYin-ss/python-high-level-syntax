import threading


# 条件变量， 用于复杂的线程间同步
# class XiaoAi(threading.Thread):
#     def __init__(self, lock):
#         super().__init__(name="小爱")
#         self.lock = lock
#
#     def run(self):
#         self.lock.acquire()
#         print("{} : 在 ".format(self.name))
#         self.lock.release()
#
#         self.lock.acquire()
#         print("{} : 好啊 ".format(self.name))
#         self.lock.release()
#
# class TianMao(threading.Thread):
#     def __init__(self, lock):
#         super().__init__(name="天猫精灵")
#         self.lock = lock
#
#     def run(self):
#
#         self.lock.acquire()
#         print("{} : 小爱同学 ".format(self.name))
#         self.lock.release()
#
#         self.lock.acquire()
#         print("{} : 我们来对古诗吧 ".format(self.name))
#         self.lock.release()

print("----")
# 通过condition完成协同读诗

class XiaoAi(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="小爱")
        self.cond = cond

    def run(self):
        with self.cond:
            self.cond.wait()  # 等待
            print("{} : 在 ".format(self.name))
            self.cond.notify()  # 通知

            self.cond.wait()
            print("{} : 好啊 ".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{} : 君住长江尾 ".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{} : 共饮长江水 ".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{} : 此恨何时已 ".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{} : 定不负相思意 ".format(self.name))
            self.cond.notify()


class TianMao(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="天猫精灵")
        self.cond = cond

    def run(self):
        with self.cond:
            # self.conf.acquire方法也可以 但是必须要self.conf.release释放锁
            #  还记得这个with吗 上下文 确实很方便 就是with打开 不用的时候就会关闭 文本打开 with 就不用close了
            # 这个notify wait必须要放在with self.cond下面的  要不然无法执行
            print("{} : 小爱同学 ".format(self.name))
            self.cond.notify()   # 先通知
            self.cond.wait()  # 再等待

            print("{} : 我们来对古诗吧 ".format(self.name))
            self.cond.notify()
            self.cond.wait()

            print("{} : 我住长江头 ".format(self.name))
            self.cond.notify()
            self.cond.wait()

            print("{} : 日日思君不见君 ".format(self.name))
            self.cond.notify()
            self.cond.wait()

            print("{} : 此水几时休 ".format(self.name))
            self.cond.notify()
            self.cond.wait()

            print("{} : 只愿君心似我心 ".format(self.name))
            self.cond.notify()
            self.cond.wait()


if __name__ == "__main__":
    from concurrent import futures

    cond = threading.Condition()
    xiaoai = XiaoAi(cond)
    tianmao = TianMao(cond)
    print(xiaoai)
    # 启动顺序很重要
    # 在调用with cond之后才能调用wait或者notify方法
    # condition有两层锁， 一把底层锁会在线程调用了wait方法的时候释放， 上面的锁会在每次调用wait的时候分配一把并放入到cond的等待队列中，等到notify方法的唤醒
    xiaoai.start()
    tianmao.start()
"""
    这个过程是天猫先说 那为什么小爱先开始呢 因为小爱先做的是wait() 而天猫先notify() 
    而wait方法是需要通过notify唤醒的 假如notify先开始 那么wait会一直等待 等待notify的到来
    condition有两层锁， 一把底层锁会在线程调用了wait方法的时候释放， 
    上面的锁会在每次调用wait的时候分配一把并放入到cond的等待队列中，等到notify方法的唤醒
    这个地方是啥意思呢 
        就是一开始获取锁 然后wait释放了这个锁在这个的同时会放一把锁到等待队列中(这个地方你先放这)
        此时这个锁不是到第二个线程里面去了吗 print 
        然后notify唤醒 上一个线程wait方法的时候放进去的那把锁 但是还要wait才会执行 wait释放锁呗
        此时又回到了最开始的线程继续执行 而第二个线程又把自己的锁放进去了 但还没有使用 等待第一个线程去notify唤醒    

    他的使用
        cond = threading.Condition() 传入
            with cond
            notify wait 
                 
        
"""

"""
    条件变量 
        用于复杂的线程间同步
        其实是一个复杂的锁
"""
