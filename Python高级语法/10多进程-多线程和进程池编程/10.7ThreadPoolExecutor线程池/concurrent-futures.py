from concurrent.futures import ThreadPoolExecutor, as_completed, wait
import time

"""
    为什么要用线程池
        主线程中可以获取某一个线程的状态或者某一个任务的状态,以及返回值
        当一个线程完成的时候我们主线程能立即知道
        futures可以让多线程和多进程编码接口一致
"""


def get_html(times):
    time.sleep(times)
    print("get page {} success".format(times))
    return times


executor = ThreadPoolExecutor(max_workers=2)
#  通过submit函数提交执行的函数到线程池中
task1 = executor.submit(get_html, 3)
task2 = executor.submit(get_html, 2)

#  futures的done方法 用于判断某个任务是否完成
print(task2.done())
print(task1.done())

#  可以得到任务1执行的返回结果 其实就是执行那个函数返回的结果
#  到这我想说一句这个多线程真的很抽象 你看不见摸不着  但是又实际存在  有一句话就是说 线程就是给个函数 他自己去执行
print(task1.result())

print(task2.cancel())  # 取消任务 但是开始了就无法取消了

#  要获取已经成功的task的返回
urls = [3, 4, 2]
all_task = [executor.submit(get_html, url) for url in urls]
for future in as_completed(all_task):
    """
        这个as_completed底层是个生成器 每次会将已经执行了的task返回(返回的是任务) 
        注意返回的是future实例(也就是前文说的task1或者task2)
    """
    data = future.result()  # 因为是实例 得.result拿到结果
    print(data)

# executor获取已经完成的task  原理和上面一样的  map函数就不说了 executor用了多线程 然后直接返回了执行任务的值
for data in executor.map(get_html, urls):
    #  但是这个返回的 和urls里面的顺序一样 假如2秒在3秒后面 还是会先返回3秒再返回2秒
    #  注意上面的是那个执行完了返回那个了
    print(data)

wait(all_task)  # 等这个列表里面的线程执行完

"""
    exec() 将字符串作为python代码执行
"""
