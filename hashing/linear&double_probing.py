l = [None] * 20
k = 0


def insert(t, n):
    if l[t] is None:
        l[t] = n
    else:
        k = t + 1
        if l[k] is None:
            l[k] = n
        else:
            k = k + (8 - (n % 8))
            insert(k, n)


for i in range(8):
    n = int(input("Enter the number"))
    t = n % 13
    insert(t, n)


print(l)