# 这个是python3.3中新增加的 yield from语法 特别不好理解
from itertools import chain

my_list = [1,2,3]
my_dict = {
    "bobby1":"http://projextsedu.com",
    "bobby2":"http://www.imooc.com",
}

for value in chain(my_list,my_dict,range(5,10)):
    print(value)


#  yield from iterable
def my_chain(*args,**kwargs):
    for my in args:
        yield from my
        #  这个和下面的原理一样  直接将my里面的值一个个的yield出来 第一个my里面的值都yield出来后(list) 就yield到dict里面
        #  for value in my:  my不就是list dict range
        #     yield value

for value in my_chain(my_list,my_dict,range(5,10)):
    print(value)




def g1(iterable):
    yield iterable

def g2(iterable):
    yield from iterable

for value in g1(range(10)):  # 只会yield这个可迭代对象
    print(value)
for value in g2(range(10)):  # yield from 会把这个可迭代对象 直接迭代出来
    print(value)


def gen1(gen):
    yield from gen

def main():
    g = gen1(range(10))


main()


"""
    main->调用方   gen1->委托生成器   gen->子生成器
    yield from 的时候 会在调用方(main)与子生成器(gen)之间建立一个双向通道
    子生成器(gen)yield的值 就直接返回到了main()函数yield的值 
    假如给main throw一个错误 也是到了gen里面了
    
    其实 以后
        yield from xxx 全部理解为
        for i in xxx:
            yield i 
        这样不就可以了吗
        
"""
