n = eval(input("请输入整数:"))

for i in range(n):
    for j in range(n):
        if j == 5:
            break
        else:
            print(j, end=' ')
    print('\n')
