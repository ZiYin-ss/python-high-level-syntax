import time
from concurrent.futures import ProcessPoolExecutor  # pro = ProcessPoolExecutor(2) -->task = ex.sub(xxx,xxx)
#  用法和线程池一样  上面是用下面的multiprocessing
#  其实可以看出 ThreadPoolExecutor里面应该也用了threading
import multiprocessing

"""
import os
fork只能用于linux/unix中
pid = os.fork()
print("bobby")
if pid == 0:
  print('子进程 {} ，父进程是： {}.' .format(os.getpid(), os.getppid()))
else:
  print('我是父进程：{}.'.format(pid))
这个会运行两遍 
sleep的话 父进程没有退出子进程会直接执行完 然后这个时候会关闭子进程
但是没有sleep的话 父进程会退出 但子进程依然存在没法退出会直接执行 这个是不会关闭的
"""

"""
    进程池语法
        https://www.cnblogs.com/kaituorensheng/p/4465768.html
        multiprocessing.pool 
        这个是用multiprocessing.pool实现进程池
            语法我就不说了 其实没什么好说的  
            就是pool(xxx)  
            然后pool.async_apply(目标函数,arg参数) 
            多进程的使用就是经常用的就是for循环 然后把进程添加到进程池里面去了
            爬虫也是这样用的 还记得吗
            for i in xrange(3):
                msg = "hello %d" %(i)
                pool.append(pool.apply_async(func, (msg, )))
                就这
            
        当然前面写线程池的时候ThreadPoolExecutor这个改为ProcessPoolExecutor也是可以实现进程池的
            这个语法和线程池一样的 
    
"""


def get_html(n):
    time.sleep(n)
    print("sub_progress success")
    return n


if __name__ == "__main__":
    # progress = multiprocessing.Process(target=get_html, args=(2,))
    """这个多进程也是可以通过继承类的方式实现多进程的 用法和继承多线程一样的"""
    # print(progress.pid)  没start的时候是没有pid的
    # progress.start() 只有start之后才会开始运行多进程和多线程
    # print(progress.pid)  start之后才会有pid 注意进程是有进程ID的而多线程是get_ident线程的唯一标识
    # progress.join()
    # print("main progress end")

    # 使用进程池
    pool = multiprocessing.Pool(multiprocessing.cpu_count())  # 最好是和cpu数一样性能最高
    result = pool.apply_async(get_html, args=(3,))

    # 等待所有任务完成
    pool.close()  # 调用join之前 必须要把线程池关闭 让他不再接收新的 因为都等待完成了你还接收有什么意思呢
    pool.join()  # 等待任务完成

    print(result.get())  # 任务执行完之后返回结果呢

    # imap
    for result in pool.imap(get_html, [1, 5, 3]):  # 完成的顺序和添加的是一样的 和map一样啊
        print("{} sleep success".format(result))

    for result in pool.imap_unordered(get_html, [1, 5, 3]):  #
        print("{} sleep success".format(result))

"""
    多说一句
        进程池可以 multiprocessing.Pool ProcessPoolExecutor 这个是两种方式
        线程池可以 threadpool.ThreadPool  ThreadPoolExecutor 这个也是两种方式
        
        进程池的 multiprocessing 是通过pool.apply_async
        线程池的 threadpool是通过pool.putRuquest提交到线程的
        其实这个
            threadpool没有用过 不过用法和multiprocessing一样的 

"""

"""
    多进程用爬虫例子
        是不是把页码给函数 开多进程抓取啊 
"""
