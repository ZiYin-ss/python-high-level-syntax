from threading import Lock, Thread,RLock


total = 0
lock = Lock()


def add():
    global total
    global lock
    for i in range(10000000):
        lock.acquire()  # 获取锁
        total += 1
        lock.release()  # 释放锁


"""
    GIL问题那张图片 问题就在于 当字节码的过程中 不知道什么时候就会释放GIL非常不好
    这个地方 就是说当获取到锁的时候会把这线程锁了 GIL释放也没事
        然后就是total += 1 的时候 不会切换线程 就是不会出现GIL那问题的 
        上面加下面减的时候都不会切换线程  也就是说这个时候可以达到安全的情况
        上面获取到锁的时候 如果下面要获取锁但是获取不到就会阻塞 此时上面加的时候是不是没人干扰啊
        下面同理
    
    但是锁比较慢 影响性能
    锁会引起死锁 -->所以会引出协程
        死锁的情况 其实就是说 看这个代码的执行顺序 acquire之后 假如没有释放 还acquire获取锁 就会死锁
        
    Rlock锁 只能在同一个线程 就是说add或者的desc
        在同一个线程里面 可以连续调用多次acquire  但是release的数量别忘了对应上了

"""




def desc():
    global total
    global lock
    for i in range(10000000):
        lock.acquire()  # 获取锁
        total -= 1
        lock.release()  # 释放锁




thread1 = Thread(target=add)
thread2 = Thread(target=desc)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print(total)
