import asyncio
import time
from functools import partial


async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)
    print("end get url")
    return "bobby"


def callback(url, future):  # 这个参数就是get_future
    print(url)
    print("赵强很帅")


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    get_future = asyncio.ensure_future(get_html("http://www.imooc.com"))  # 这个会自己添加到循环里面 执行任务
    # task = loop.create_task(get_html("http://www.imooc.com")) 和上一行一样

    get_future.add_done_callback(partial(callback, "http://www.imooc.com"))  # 事件执行完的回调函数
    """
        partial(callback,"http://www.imooc.com")
        callback("http://www.imooc.com",future)
        又因为默认给这里面的函数传递future 会到callback里面 
        这个就是偏函数的应用 我就是提一下  知道怎么用
    """

    """
        假如多个 get_future 是不是都添加到tasks中 然后await(tasks) 
        执行完了 是不是依然get_future.result 取值啊 
    """
    loop.run_until_complete(get_future)  # 等待他执行完成
    # loop.run_until_complete(task)

    print(get_future.result())  # 获取这个任务(函数)的返回值
    # print(task)

"""
    流程
        loop = asyncio.get_event_loop() 先创建
       
        get_future = asyncio.ensure_future(get_html("http://www.imooc.com")) 这个是用来提交此次事件的 后面可以返回值
        
        get_future.add_done_callback(callback)  事件执行完的回调函数
        
        tasks = [get_html("http://www.imooc.com") for i in range(10)] 
        loop.run_until_complete(get_future)   等待他执行完成
        loop.run_until_complete(asyncio.wait(tasks))   
        asyncio.gather(*tasks) 还可以多个 *tasks *tasks1 等待tasks tasks1里面所有的任务完成 
        
        tasks.cancel()取消
        
        print(get_future.result()) # 获取结果
        
    协程 coroutine
"""
