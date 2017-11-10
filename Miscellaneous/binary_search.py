def binary_search(l, low, high, key):
    if low > high:
        print("False")
        return None

    mid = int((low + high) / 2)
    if key < l[mid]:
        high = mid - 1
        return binary_search(l, low, high, key)
    elif key > l[mid]:
        low = mid + 1
        return binary_search(l, low, high, key)
    else:
        print("True")
        return mid


l = [None] * 35
k = 0
for i in range(0, 100, 3):
    l[k] = i
    k = k + 1
print(l)
low = 0
high = len(l) - 1
key = int(input("Enter the element to be found\n"))
y = binary_search(l, low, high, key)
