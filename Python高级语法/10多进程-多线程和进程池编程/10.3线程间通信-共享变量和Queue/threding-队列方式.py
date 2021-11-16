import time
import threading
from queue import Queue


def get_detail_html(queue):
    #  爬取详情页
    while True:
        print("get detail html started")
        url = queue.get()   # popleft   没有数据就会阻塞 这个地方当时爬虫讲的时候演示过来 会一直等着 其他地方加进来一个 然后这个才会走
        #  这个队列的结构 其实我在python算法里面 有一节介绍队列的 但多说一句也不会死 先进先出 头部出尾部进 就这个意思
        #  确实是这样的
        print(url)
        time.sleep(2)
        print("get detail html end")


def get_detail_url(queue):
    #  爬取列表页
    while True:
        print("get detail url started")
        for i in range(20):
            queue.put("http_%d"%i)  #append
            print(i)
        time.sleep(2)
        print("get detail url end")


"""
    这个是利用队列实现了线程安全 
        因为deque本身就是线程安全的  因为在字节码的级别就达到了安全 为什么呢 你想字节码的过程 dis.dis(a) 想当时这个过程
        这个Queue里面的方法都是线程安全的 可以直接使用
        detail_url_queue.task_done() 完成退出
        detail_url_queue.join() 和Thread.join() 一样
        这个时候就体现出了这个的牛逼 更好的控制多线程了 
         
"""

if __name__ == '__main__':
    detail_url_queue = Queue(maxsize=1000)
    thread_detail_url = threading.Thread(target=get_detail_url,args=(detail_url_queue,))
    thread_detail_url.start()
    for i in range(5):
        html_threa = threading.Thread(target=get_detail_html,args=(detail_url_queue,))
        html_threa.start()
