import threading

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
print(total)