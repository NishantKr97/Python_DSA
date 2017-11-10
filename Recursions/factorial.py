def factorial(n):
    if n==1:
        return 1
    return n * factorial(n-1)




def main():
    x = int(input("enter the number"))
    y = factorial(x)
    print(y)





main()