import time
from concurrent.futures._base import as_completed
from concurrent.futures.process import ProcessPoolExecutor
from concurrent.futures.thread import ThreadPoolExecutor

pass
"""
    多线程是假的多线程 因为GIL锁
    多进程才是真的多核处理   
        就是切换代价高于多线程
        耗cpu的操作 用多进程编程
        对于IO操作来说使用多线程编程
    对于耗费CPU的操作 多进程优于多线程 
    对于IO操作来说 多线程优于多进程
"""
# 1. 对于耗费cpu的操作，多进程由于多线程
def fib(n):
    if n<=2:
        return 1
    return fib(n-1)+fib(n-2)

if __name__ == "__main__":
    with ThreadPoolExecutor(3) as executor:
        all_task = [executor.submit(fib, (num)) for num in range(25,40)]
        start_time = time.time()
        for future in as_completed(all_task):
            data = future.result()
            print("exe result: {}".format(data))

        print("last time is: {}".format(time.time()-start_time))


#2. 对于io操作来说，多线程优于多进程
def random_sleep(n):
    time.sleep(n)
    return n

if __name__ == "__main__":
    with ProcessPoolExecutor(3) as executor:
        all_task = [executor.submit(random_sleep, (num)) for num in [2]*30]
        start_time = time.time()
        for future in as_completed(all_task):
            data = future.result()
            print("exe result: {}".format(data))

        print("last time is: {}".format(time.time()-start_time))


"""
    注意这个在windows下面 ProcessPoolExecutor 包括multiprocessing中的进程池 
        都得写在if __name__ == "__main__": 这个下面 Linux下不用
    
    
    为什么这个进程池和线程池这么像呢 
        记得在学线程池得时候就说了 Futures这个类实现了接口编码一致 
         futures可以让多线程和多进程编码接口一致
    
    注意
        多线程多进程 我们在什么时候用什么其实说明白了 
        进程不见得比线程好 线程不见得比进程差 
        进程切换代价大 线程GIL的锁
        进程CPU 线程IO
    
    
"""