pass

"""
    C10K
        如何在一颗1Ghz CPU 2g内存 1gbps网络环境下 让单台服务器同时为一万个客户端提供FTP服务
    阻塞式IO中 
        CPU是空闲的
    非阻塞式的IO
        client.setblocking(False) 这个是建立socket的时候不管他建立好连接没 就直接返回
        不停的询问连接是否建立好 需要while循环不停的去检查状态
        可以做计算任务或再次发起其他的连接请求            
        耗CPU
    IO多路复用
        最大的优点就是说 你看图
            也是一个阻塞的方法 没有一个socket或者文件句柄准备好的话 也是阻塞式的
            监听多个文件句柄和socket 可以放一个list存放这所有的socket 有一个状态发生变化就会返回 监听多个
            假如发起一百个非阻塞式的client请求  用select去监视他 确实牛逼 
            有一个返回了就可以处理业务逻辑了
        看图 从电脑到应用那一段时间还是无法省略
        select poll和epoll 
    其实你看异步IO
        就是直接省略了把文件发送到应用那难度确实大
    那个select-poll-epoll图片中
        监视多个就不说了
        为什么读写是同步阻塞呢 因为这个时候就是从电脑写到应用空间的 所以是这样的
        挺牛逼呢
    select到poll到epoll是依次递进的 但各有优缺点
    epoll只能在LINUX中使用
    
    1. epoll并不代表一定比select好
    在并发高的情况下，连接活跃度不是很高， epoll比select  网页浏览
    并发性不高，同时连接很活跃， select比epoll好  游戏连接
"""