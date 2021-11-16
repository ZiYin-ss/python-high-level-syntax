import time
import threading

detail_url_list = []


def get_detail_html(detail_url_list):
    #  爬取详情页
    while True:
        if len(detail_url_list):
            url = detail_url_list.pop()
            print("get detail html started %s" % url)
            time.sleep(2)
            print("get detail html end")


def get_detail_url(detail_url_list):
    #  爬取列表页
    while True:
        print("get detail url started")
        time.sleep(2)
        for i in range(20):
            detail_url_list.append("http%d" % i)
            print(i)
        print("get detail url end")


"""
    线程间的通信方式
        共享变量
            首先说一下 其实真的很乱 但是乱才是对的 因为这个确实是实时共享变量 看了一下流程 没有问题
            这个共享变量其实并不好 因为不太安全 因为太乱了 
            需要加锁 加锁的语句越少越好 
            比如get_detail_url在for的时候加锁
            get_detail_html在pop的时候加锁 
            但是也就那样把 
"""


if __name__ == '__main__':
    thread_detail_url = threading.Thread(target=get_detail_url, args=(detail_url_list,))
    thread_detail_url.start()
    for i in range(5):
        html_threa = threading.Thread(target=get_detail_html, args=(detail_url_list,))
        html_threa.start()
    start_time = time.time()

    # print(time.time() - start_time)

"""
    from chapter11.variables import detail_url_list     
        这个引用方式是有问题的 因为这样引用你是看不见其他线程对这个变量的修改
    from chapter11 import variables   
        variables.detail_url_list 这样可以看见
"""
