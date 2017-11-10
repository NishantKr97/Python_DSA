from sys import maxsize


def createStack():
    stack = []
    return stack


def pop(stack):
    return stack.pop()


def push(stack, k):
    stack.append(k)


def main():
    push(5)
    push(7)
    print(pop())


main()
