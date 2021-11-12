import math

shui = eval(input("请输入一个三位数:"))

g = shui % 10
s = int(shui/10)%10
b = int(shui/100)
shuishui = g**2+s**2+b**2
print(shuishui)


shui1 = input("请输入一个三位数:")
c = eval(shui1[0:1])
b = eval(shui1[1:2])
a = eval(shui1[2::])

print(c**2+b**2+a**2)