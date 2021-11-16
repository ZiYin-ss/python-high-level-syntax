print("Aaa")

class company:
    def __getitem__(self, item):
        pass


    """
        for  i in company:
        其实这个可以for循环
            其实是拿着 iter(company) 去找这个类里面有没有iter方法  没有就退而求其次找getitem
            进一步说明是可迭代对象
    
    """
from collections import UserList
"""
    def __getitem__(self, index):
        raise IndexError

    def __iter__(self):
        i = 0
        try:
            while True:
                v = self[i]
                yield v
                i += 1
        except IndexError:
            return
            
        看到这个地方应该知道生成器怎么用的把 
        其实 流程就是 先yield 1 这个时候停了 然后你再走下一个的时候 就再来 i+=1 再v=self[i] 再走到yield 就这样的  
    
"""
"""

def aa():
    for i in range(0,10):
        yield i
        
aa()  <generator object aa at 0x0140A3A8>

for i in aa():
    print(i)
    
 这个地方想明白怎么走的吗 下面的循环aa() 其实 这个地方就是生成器  你每循环一次 他就执行一次aa 返回一个值 因为aa里面是有yield的啊 
 还记得以前做爬虫的时候 那个老师不就是这样写的把 是吧 

 
"""
"""
    for item in data.get('data'):  
        yield item.get('article_url')  
        为什么用生成器呢? 
            for url in parse_page_index(html):
            生成器不就是每次for都会来执行这个函数  这个函数返回yield
            又因为是for循环 yield一次之后就会返回这个函数 值是yield出去的值              
    
    这个解释其实不算好理解 
        只可意会不可言传 
            首先数据过大 上面也可以添加到一个列表中返回 没有必要
            第二 yield 每次都返回一个数据并保存这次的位置 下次来了继续从这个地方再往前yield一个呗
            所以说循环这个函数 是有返回值的 就是yield再起作用的啊 
            还有就是看上面的next()函数 可以发现 yield 是要给他一个值返回的  不是凭空出来的

"""