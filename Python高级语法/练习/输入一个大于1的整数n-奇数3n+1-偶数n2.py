n = eval(input("请输入整数n:"))

count = 0
while n > 1:
    if n % 2 == 0:
        n = n / 2
        count += 1
    else:
        n = 3 * n + 1
        count += 1
    print(n)


print(count)
