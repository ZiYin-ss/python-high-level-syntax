import socket

""" 
    AF_INET IPV4网络 AF_INET6 IPV6网络 
    Tcp中 支持SOCK_STREAM这个协议 
    Udp中 支持SOCK_DGRAM这个协议  
        socket.AF_INET,socket.SOCK_DGRAM 这个是UDP中的写法
    
    下面严格遵守这个文件夹下面那个图片写的 
"""
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # 这个地方主要就是确定协议
server.bind(('0.0.0.0',8000))  # 绑定地址
server.listen()
sock,addr = server.accept()

#  获取从客户端发送的数据
data = sock.recv(1024)
print(data.decode('utf8'))
sock.send("hello {}".format(data.decode('utf8')).encode('utf8'))
server.close()
sock.close()




"""
    Django的框架是不提供Socket  是Server端编程 
        runserver只是提供一个非常简单的Socket 
        真正实现网络通信的依靠的是WSGI这个组件的 组件是组件 框架是框架 框架本身不提供
        
    其实爬虫就是Cli端编程
        我们发送请求获取数据
"""