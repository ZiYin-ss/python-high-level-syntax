final_result = {}


def sales_sum(pro_name):
    total = 0
    nums = []
    while True:
        x = yield  # 这个地方直接接收值啊
        print(pro_name + "销量: ", x)
        if not x:
            break
        total += x
        nums.append(x)
    return total, nums


def middle(key):
    while True:
        final_result[key] = yield from sales_sum(key)
        print(key + "销量统计完成！！.")


def main():
    data_sets = {
        "bobby牌面膜": [1200, 1500, 3000],
        "bobby牌手机": [28, 55, 98, 108],
        "bobby牌大衣": [280, 560, 778, 70],
    }
    for key, data_set in data_sets.items():
        m = middle(key)
        m.send(None)  # 预激middle协程  此时middle中的子生成器 sales_sum和main函数创建双向通道
        for value in data_set:
            m.send(value)  # 给协程传递每一组的值  给到子生成器里面了 x=yield
        m.send(None)
    print("final_result:", final_result)


if __name__ == '__main__':
    main()

if __name__ == "__main__":
    my_gen = sales_sum("bobby牌手机")
    my_gen.send(None)
    my_gen.send(1200)
    my_gen.send(1500)
    my_gen.send(3000)
    try:
        my_gen.send(None)
    except StopIteration as e:  # 这个地方是yield的特色  因为产生了异常 没有yield值了 就是Stop异常就会收到返回值 e.value出来
        # 如果抛出了 `StopIteration` 异常，那么就将异常对象的(函数) `value` 属性保存到_r，这是最简单的情况的返回值；
        result = e.value
        #  其实这个地方的处理 返回到了 yield from 这个地方呢
        #  也就是我说为什么key能有值呢
        #  _r：yield from 表达式最终的值
        print(result)
