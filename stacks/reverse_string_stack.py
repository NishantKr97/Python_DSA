l = input("Enter the string")
a = l.split(" ")
print(a)
b = []
k = len(a) - 1
for i in range(k, 1):
    print(a[k])
    b.append(a[i])

print(b)