import asyncio
import time


async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)  # 阻塞代码不应该写进来
    print("end get url")


if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()  # 创建事件循环 这样创建就可以了

    tasks = [get_html("http://www.imooc.com") for i in range(10)]  # 多任务放到列表中了

    # loop.run_until_complete(get_html("http://www.imooc.com"))  执行单个任务
    loop.run_until_complete(asyncio.wait(tasks)) # 把多任务放到这个事件循环中  用wait
    # 这个会等到函数执行之后才会print 类似与 线程的join方法执行完成

    print(time.time() - start_time)

"""
    asyncio
        是python用于解决异步IO并发编程的一整套解决方案
        这个地方分为两个理解 异步IO 并发(同一时间段内有多少个程序运行)编程
        https://www.cnblogs.com/lucktomato/p/15154693.html
        这个网址中有websocket和channels(Django的增强框架支持websocket)的介绍 
    
    协程编码模式必须是
        事件循环->回调(驱动生成器)->IO多路复用
    
    事件循环
        loop = asyncio.get_event_loop()  
"""

"""
start get url
start get url
start get url
start get url
start get url
start get url
start get url
start get url
start get url
start get url
end get url
end get url
end get url
end get url
end get url
end get url
end get url
end get url
end get url
end get url
2.0153238773345947

这个地方应该知道什么原理把
假如这个sleep操作是我们自己的网络IO操作 
不就会同时开始吗(是因为第一个执行完了会耗时 然后执行其他的是这个意思) 
然后会先返回一个最先准备好的把 
这个地方和当时的select+事件循环其实是一样的

这个是协程 所谓的开销 其实我们这看不见的 因为本来就很简单
要是大了就知道了 对cpu-时间-效率是有很大影响的 

"""
