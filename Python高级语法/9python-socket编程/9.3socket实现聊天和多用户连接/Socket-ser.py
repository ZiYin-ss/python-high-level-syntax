import socket
import threading

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('0.0.0.0',8000))
server.listen()

def hand_sock(sock,addr):
    while True:
        data = sock.recv(1024)
        print(data.decode('utf8'))
        re_data = input()
        sock.send(re_data.encode('utf8'))


"""
    其实这个socket基本使用 真的不难
        服务端(Server)
            先协议->绑定端口->开始监听->创建阻塞(返回sock和addr)->直接拿sock接收发送注意编码问题即可
        客户端(Client)
            先协议->创建连接(端口)->直接拿这个对象去发送接收注意编码问题就可以了
        while True 
            就是为了让他死循环下去 服务器不开着干啥 日后你要死循环 不也while True呗
        多线程这个也好理解
            来一次都会接到不同的sock  拿着这个一直循环运行呗
"""

while True:
    sock, addr = server.accept()

    #  用线程去处理新新接收的连接
    # client_thread = threading.Thread(target=hand_sock,args=(sock,addr))
    # client_thread.start()
    #  这个是多线程的 我就不说了 没什么好说的 就是来一个sock创建一个线程去处理 具体的意思就是
    #  第一个来了 创建了这个函数 一直执行
    #  第二个来了 又创建了一次 然后又一直执行


    data = sock.recv(1024)
    print(data.decode('utf8'))
    re_data = input()
    sock.send(re_data.encode('utf8'))

