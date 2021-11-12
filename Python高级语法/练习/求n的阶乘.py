n = eval(input("请输入一个数"))

b = 1

for i in range(n+1):
    if i == 0:
        continue
    else:
        b *= i

print(b)