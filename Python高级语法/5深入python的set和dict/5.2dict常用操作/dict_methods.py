a = {
    "bobby1": {"company": "imooc"},
    "bobby2": {"company": "imooc2"}
}
print(a)
# a.clear()  # 清空全部数据
# print(a)


# copy复制   浅拷贝只是复制对象地址 并不是整个对象给过来 所以说你修改这个new_dict的时候实际上也是修改a 因为这二者指向的地址一样
new_dict = a.copy()
new_dict["bobby1"]["company"] = "imoo3"
print(a)  # {'bobby1': {'company': 'imoo3'}, 'bobby2': {'company': 'imooc2'}}
print(new_dict)  # {'bobby1': {'company': 'imoo3'}, 'bobby2': {'company': 'imooc2'}}

import copy

new_dict2 = copy.deepcopy(a)  # 这个地方就是深拷贝 完全复制这份数据给他 新开辟一个地址存放
new_dict2["bobby1"]["company"] = "imoo4"
print(new_dict2)
print(a)

b = {
    "bobby3": {"company": "imooc3"},
    "bobby4": {"company": "imooc4"}
}

# fromkeys将可迭代对象转换为dict  第一个参数是可迭代对象 作为key 第二个是默认值 会生成字典字典
new_list = ["bobby1", "bobby2"]
new_dict3 = dict.fromkeys(new_list, {"aaa"})
print(new_dict3)


# setdefault 可以取出这个值 如果没有就设置默认值  或者可以直接设置值
# 这个地方是不是就可以用来做 假如有就取值没有就设置值的操作啊
new_dict.setdefault("bobby1","imooc")
print(new_dict)

# update 添加值啊 也可以直接设置的
new_dict.update({"bobby":"imoov"})
print(new_dict)
