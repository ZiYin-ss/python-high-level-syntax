import time
import threading


def get_detail_html(url):
    print("get detail html started")
    time.sleep(2)
    print("get detail html end\n")


def get_detail_url(url):
    print("get detail url started")
    time.sleep(2)
    print("get detail url end")


if __name__ == '__main__':
    thread1 = threading.Thread(target=get_detail_html, args=("",))
    thread2 = threading.Thread(target=get_detail_url, args=("",))
    start_time = time.time()
    thread1.setDaemon(True)
    thread2.setDaemon(True)
    #   设置为守护线程 就是主线程退出后会直接将着两个子线程关掉
    #   假如这两个线程线程1不开 线程2开了的话 就会等待线程1执行完就会关闭主线程 这个时候线程2也会强制关掉

    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()  # 等待线程完成

    #  当主线程退出的时候 子线程kill掉
    print(time.time() - start_time)

"""
    这个地方是方式一实现多线程的  没什么好说的  threading.Thread 还是个伪多线程
        适用于简单的逻辑 复杂了就要继承 threading.Thread 看第二个文件
        还有就是GIL的问题
            1.设置GIL。
            2.切换到一个线程去执行。
            3.运行。
            4.把线程设置为睡眠状态。
            5.解锁GIL。
            6.再次重复以上步骤。
        这个也是我一直想知道的 就是GIL的问题 是在sleep的时候 换线程的 
        还有就是爬虫使用多线程为什么 因为有IO操作 这个read或者其他的或者时间片轮转 这个时候就会切换线程 所以可以
"""


"""
    对于IO操作来说 多线程和多进程性能差别不大 就是多线程轻量级
    多线程爬虫你知道是什么意思吗
        你可是学过爬虫的哦
        就是第一个线程爬取到的url存到全局或者队列中
        另外一个线程去这个队列中取出来url去爬取 这个意思 懂吗    
"""

