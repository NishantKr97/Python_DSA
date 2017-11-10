class stacks:
    def __init__(self):
        self.l = []

    def push(self, k):
        self.l.append(k)

    def pop(self):
        return self.l.pop()

    def show(self):
        print(self.l)

    def length(self):
        return len(self.l)

    def sh(self, i):
        print(self.l[i])


def main():
    l = stacks()
    k = stacks()
    for i in range(0, 12, 2):
        l.push(i)
    l.show()
    l.pop()
    l.show()

    t = l.length()
    print(t)

    for i in range(t):
        k.push(l.pop())

    for i in range(t):
        print(k.pop())

        # k.show()


main()

