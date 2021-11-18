from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE


def gen_func():
    yield 1
    return "bobby"

"""
    生成器是可以暂停的
        GEN_SUSPENDED
"""

#1. 用同步的方式编写异步的代码， 在适当的时候暂停函数并在适当的时候启动函数
import socket
def get_socket_data():
    yield "bobby"

def downloader(url):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setblocking(False)

    try:
        client.connect((host, 80))  # 阻塞不会消耗cpu
    except BlockingIOError as e:
        pass

    selector.register(self.client.fileno(), EVENT_WRITE, self.connected)
    source = yield from get_socket_data()  # 这个地方会暂停 等待这个地方读取数据
    data = source.decode("utf8")
    html_data = data.split("\r\n\r\n")[1]
    print(html_data)

def download_html(html):
    html = yield from downloader()

if __name__ == "__main__":
    #协程的调度依然是 事件循环+协程模式 ，协程是单线程模式
    pass
