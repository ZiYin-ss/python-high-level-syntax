import bisect

#  用来处理已排序的序列  用来维持一个已排序的序列 升序
#  不止list 就是只要是序列就可以

inter_list = []
bisect.insort(inter_list, 3)
bisect.insort(inter_list, 1)
bisect.insort(inter_list, 5)
bisect.insort(inter_list, 2)
bisect.insort(inter_list, 6)
bisect.insort(inter_list, 4)
print(bisect.bisect(inter_list, 3))
print(inter_list)

"""
    这个地方也就是说 插入的时候 就像上面那样插入  不用管位置 就给你维护好排序了
        bisect=bisect_right
        bisect_left
        这连个是插入 是重复元素的右边或者左边 如果打印就是再列表中的索引
        比如改优先级
    python编程技巧中我已经写过了这个库 以及一些函数的作用
"""

