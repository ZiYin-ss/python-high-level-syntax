pass

"""
    python3.5以前协程一直都是用的都是生成器
    python 3.5 以后出来了  为了将语义变得更加明确 用async和await定义原生的协程
    js中的async和await
        await存在的话 在他个外层函数中要包裹一个async 这个await test() await会拿到test()异步方法的返回值
"""
async def downloader(url):
    return "bobby"

async def download_url(url):
    html = await downloader(url)  # 有没有发现和js中的是一样的 downloader是一个异步方法获取html啊 但是这个异步方法 前面还是要加async
    """
        await 对比与 yield from
        
        有没有发现这个协程就是和js中的一样啊 
        异步非阻塞 
        协程的调度依然是    事件循环+协程模式
        协程是单线程模式 
        其实可以理解了 单线程  yield出去 执行 这个就是协程
        其实也没啥 
            你看yield暂停一下执行耗时的操作 然后返回回来  同时select事件监听 那个好了返回那个 
    """
    return html

if __name__ == '__main__':
    coro = download_url("sasdadas")
    coro.send(None)