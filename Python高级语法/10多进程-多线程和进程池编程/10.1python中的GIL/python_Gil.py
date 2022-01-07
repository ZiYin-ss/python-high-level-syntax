import dis
import threading


def adda(a):
    a = a + 1


"""
    gil global interpreter lock (cpython)
        全局解释器锁
    python中一个线程对应于c语言中的一个线程 
    gil使得同一个时刻只有一个线程在一个cpu上执行字节码 无法将多个线程映射到多个cpu上执行
        这个把锁真的很烦 导致无法利用多核优势
    不过gil这个锁也会释放 只有在IO操作的时候
"""

total = 0


def add():
    global total
    for i in range(10000000):
        total += 1


def desc():
    global total
    for i in range(10000000):
        total -= 1


thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=add)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print(total)  # 12637559

"""
    这个GIL是会释放的 而且这个total还是一个不稳定的值 
    按理说加多少和减多少 到最后会是零把 但是不是 
    也就说明 他不会等待这个线程执行完再执行另外一个线程
    而是在适当的时候释放的  
    
    说个细的
        就是说就算不是一起执行的那加1000和减一千到最后不还是0吗  那为什么不是0呢 
        这个地方就是说这个时候这个GIL会释放
        然后其他核不就会继续减呗 但是此时也在加的
         
    这个GIL会在两个情况下释放GIL锁
        gil会根据执行的字节码行数以及时间片释放gil 主动释放
        io操作的时候  主动释放 也就是说这个多线程在IO操作频繁的时候非常实用
    
    总结一下啥意思呢
        GIL是说会导致一个线程只会在一个时刻运行 但是也不是必须的 IO或着时间片的时候轮转 
        释放GIL这个时候会是真正的多线程(多核处理呗)
                
"""
