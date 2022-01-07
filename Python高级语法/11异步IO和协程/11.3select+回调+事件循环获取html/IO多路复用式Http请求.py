# IO多路复用实现Http请求
import socket
from urllib.parse import urlparse
# import select   最最原生 不好用 一般不用
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE

"""这个DefaultSelector 在windows下面用select 在Linux中用epoll 会自己选择"""

# 注册全局的select
selector = DefaultSelector()
urls = ["http://www.baidu.com"]
"""为什么加上这个呢 因为当抓取完了一个url会将他删除掉 不删除是不是重复抓取啊 会显示错误 是无效参数 因为这个地方不是阻塞的 会第二次循环"""
stop = False


class Fetcher:
    def connect(self, key):
        #  需要注销掉监控的这个事件 key是默认传过来这个事件的标识
        selector.unregister(key.fd)
        self.client.send(
            "GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(self.path, self.host).encode("utf8"))
        selector.register(self.client.fileno(), EVENT_READ, self.readable)

    def readable(self, key):
        d = self.client.recv(1024)
        if d:
            self.data += d
        else:
            selector.unregister(key.fd)
            data = self.data.decode("utf8")
            html_data = data.split("\r\n\r\n")[1]
            print(html_data)
            self.client.close()
            urls.remove(self.spider_url)
            if not urls:
                global stop
                stop = True

    """
        有个编程技巧 你看self.client设置为实例的属性 如果不设置的话只能在这个一个函数中用 
        那么上面就用不到 也就是说下次在类中 遇到很多函数里面都需要使用的变量还是放到self里面把 
        在一个函数中产生的变量 也可以放到self中的 整个实例对象使用
    """

    def get_url(self, url):
        self.spider_url = url
        url = urlparse(url)
        self.host = url.netloc
        self.path = url.path
        self.data = b""
        if self.path == "":
            self.path = "/"

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setblocking(False)
        try:
            self.client.connect((self.host, 80))
        except BlockingIOError as e:
            pass

        # 将socket注册到select中
        # 有没有觉得这个模式像前端的Axios模式 路径--数据请求回来的回调函数
        """
            windows只能socket采用select  文件的select操作在UNIX和LINUX中才有 
            他们的事件描述符就是fdxxx 用到的时候你搜一下怎么取出来就可以 用法和下面一样  
                参数
                    fileno() 这个就是socket的事件描述符 
                    注册什么事件
                    判断可以执行这个事件后的回调函数
        """
        selector.register(self.client.fileno(), EVENT_WRITE, self.connect)


def loop():
    #  select本身是不支持register模式(只提供句柄和读写标识)  因为selector封装了select的所以我们可以用register
    #  socket状态变化以后的回调是由程序员完成的
    #  这个就是事件循环 不停的请求socket的状态并调用对应的回调函数
    while not stop:
        ready = selector.select()
        for key, mask in ready:
            call_back = key.data  # 我们自己定义的回调函数
            call_back(key)  # 自己执行回调函数

    # 回调+事件循环+select(poll/epoll)


"""
    这个地方解释一下把 selector.select() 存了列表 元素是元组 
    也就是说我们刚刚注册的东西 在这个ready里面
    然后不停的while循环 当那个事件达到了之后 就会往selector.select()里面放东西  然后可以循环了 就是我们自己找到回调函数执行
"""

if __name__ == '__main__':
    fetcher = Fetcher()
    fetcher.get_url("http://www.baidu.com")
    loop()

"""
    解释一下把
        这个模式很牛逼 就是事件加回调 单线程模式 找到那个准备好的
        并发性高
        for循环  这个 
            fetcher = Fetcher()
            fetcher.get_url("http://www.baidu.com")
        每次循环是不是添加一个url 注册 然后执行完之后 loop循环 找准备好的 用selector.select()执行就是了
"""
