print("aa")
from collections import Iterable,Iterator

"""
    所谓迭代协议
        主要就是实现__iter__方法  可迭代对象
        __next__ 是迭代器实现
        
    什么是迭代器
        迭代器是什么 
        迭代器是访问集合内元素的一种方式 一般用来遍历数据
        迭代器和以下标的访问方式不一样  迭代器不能返回的
        迭代器提供了一种惰性访问数据的方式
    list是一个可迭代类型 并不是迭代器
    Iterator 迭代器
    Iterable 可迭代类型
"""
