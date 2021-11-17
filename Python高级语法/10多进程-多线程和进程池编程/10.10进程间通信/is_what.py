import time
from multiprocessing import Process, Queue, Pool, Manager, Pipe
import queue
"""
    Queue 
        普通的queue用不了 
        用multiprocessing的Queue 就可以了
        这个接口和普通的queue一样
    
    共享全局变量通信
        共享全局变量不能适用于多进程编程，可以适用于多线程
    
    multiprocessing中的queue不能用于pool进程池
        pool中的进程间通信需要使用manager中的queue
        queue = Manager().Queue(10)
        用法同上
    
    通过pipe实现进程间通信
        pipe的性能高于queue
        pipe只能适用于两个进程
    
    共享内存
        progress_dict = Manager().dict()
    
    整个python中有三个queue
        import queue
        from multiprocessing import Queue,
        queue = Manager().Queue(10)  
        还有一个deque 在集合模块中

"""


"""
def producer(queue):
    queue.put("a")
    time.sleep(2)

def consumer(queue):
    time.sleep(2)
    data = queue.get()
    print(data)

if __name__ == "__main__":
    queue = Manager().Queue(10)
    pool = Pool(2)

    pool.apply_async(producer, args=(queue,))
    pool.apply_async(consumer, args=(queue,))

    pool.close()
    pool.join()
"""


"""
def producer(pipe):
    pipe.send("bobby")

def consumer(pipe):
    print(pipe.recv())

if __name__ == "__main__":
    recevie_pipe, send_pipe = Pipe()
    pipe只能适用于两个进程
    my_producer= Process(target=producer, args=(send_pipe, ))
    my_consumer = Process(target=consumer, args=(recevie_pipe,))
    
    注意pipe的用法 send recv
    my_producer.start()
    my_consumer.start()
    my_producer.join()
    my_consumer.join()
"""

def add_data(p_dict, key, value):
    p_dict[key] = value

if __name__ == "__main__":
    progress_dict = Manager().dict()
    from queue import PriorityQueue

    first_progress = Process(target=add_data, args=(progress_dict, "bobby1", 22))
    second_progress = Process(target=add_data, args=(progress_dict, "bobby2", 23))

    first_progress.start()
    second_progress.start()
    first_progress.join()
    second_progress.join()

    print(progress_dict)
