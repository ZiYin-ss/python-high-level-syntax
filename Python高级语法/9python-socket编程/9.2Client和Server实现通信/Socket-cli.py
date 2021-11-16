import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1',8000))
client.send("赵强".encode('utf8'))
data = client.recv(1024)
print(data.decode('utf-8'))
client.close()


"""
    这个里面还有一个问题 就是说编码问题 其实你看像我这样写 "赵强".encode('utf8) 是没有问题
    但是你要其他那样写是会有问题的 所以以后编码还是 直接data.encode('utf8)
"""