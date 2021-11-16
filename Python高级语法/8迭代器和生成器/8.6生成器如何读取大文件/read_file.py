# 500G, 特殊 一行
def myreadlines(f, newline):
    buf = ""
    while True:
        while newline in buf:  # {|}
            pos = buf.index(newline)  # 找到这个符号 {|}的索引
            yield buf[:pos]  # 返回从0到pos前一个的字符 前面到后不到吗
            buf = buf[pos + len(newline):]
            # 更新buf大小  就是把前面yield那一段删掉了 从pos+{|} 开始不就是第二段了呗 依次循环
            #  假如我读了一个chunk里面有好几个{|} 会都分割完 再继续读取的
        chunk = f.read(4096)

        if not chunk:
            # 说明已经读到了文件结尾
            yield buf  # 经过前面的处理到最后的buf里面是没有{|} 没了直接输出就可以了
            break
        buf += chunk


with open("input.txt") as f:
    for line in myreadlines(f, "{|}"):
        print(line)
