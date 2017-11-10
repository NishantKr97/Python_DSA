def fibo(x):
    if x is 0:
        return 0
    if x is 1:
        return 1
    return fibo(x-1) + fibo(x-2)




def main():
    x = int(input("enter\n"))
    print(fibo(x-1))



main()