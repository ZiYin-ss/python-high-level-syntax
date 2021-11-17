# 通过非阻塞IO实现http请求
import socket
from urllib.parse import urlparse


def get_url(url):
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"


    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.setblocking(False)
    """
        这个地方这样写就是不会等待连接成功返回 是立即返回 也就是说发送和接收的时候都是立即的 不考虑连接
        这样所谓的非阻塞我们利用的是while True 不断尝试 遇到问题 try except 继续执行
            这个过程就是前面说的不断执行的过程 消耗cpu
            然后这个非阻塞式使用的还是说接下来要执行的操作是计算或者IO操作的还是比较好的
            这个是真的理解了 要是不写一遍代码怎么能知道呢
            
    """
    try:
        client.connect((host, 80))
    except BlockingIOError as e:
        pass
    while True:
        try:
            client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))
            break
        except OSError as e:
            pass

    data = b""
    while True:
        try:
            d = client.recv(1024)
        except BlockingIOError as e:
            continue
        if d:
            data += d
        else:
            break

    data = data.decode("utf8")
    html_data = data.split("\r\n\r\n")[1]
    print(html_data)
    client.close()

if __name__ == "__main__":
    import time
    start_time = time.time()
    for url in range(20):
        url = "http://shop.projectsedu.com/goods/{}/".format(url)
        get_url(url)
    print(time.time()-start_time)

"""
    python中常见的IO操作
        1) 键盘输入函数
        2) 文件句柄(file)对像(文件操作)
        3) stringio，python在内存中开辟一块文本模式的buffer
        4) byteio，python在内存中开辟一款bytes类型(二进制格式)的buffer
        5) 类文件对象，file-like obj
        网络操作、文件操作、终端操作等均属于IO操作
"""