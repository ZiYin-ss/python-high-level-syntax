def b(n):
    a = dict()
    a[0] = 1
    a[1] = 1
    for i in range(n):
        if i < 2:
            continue
        else:
            a[i] = a[i - 1] + a[i - 2]
    print(a[n - 1])


b(3)


def c(n):
    a = 1
    b = 1
    for i in range(n - 2):
        a, b = b, a + b
    print(b)


c(3)
