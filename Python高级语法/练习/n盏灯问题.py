n = eval(input("请输入n栈灯:"))
k = eval(input("请输入k个人:"))

list = [0 for _ in range(1,1001)]

for i in range(1,k+1):
    for j in range(1,n+1):
        if j % i == 0:
            list[j-1] = not list[j-1]

for i in range(0,len(list)-1):
    if list[i]:
        print(i+1)


