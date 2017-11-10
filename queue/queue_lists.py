class queue:
    def __init__(self):
        self.q = [None] * 10

    def enqueue(self,i):
        k = self.q.append(i)

    def dequeue(self):
        y = self.q[0]
        self.q.remove(self.q[0])
        return y

    def front(self):
        return self.q[0]

    def isEmpty(self):
        if(len(self.q)==0):
            return True
        else:
            return False

    def size(self):
        return len(self.q)

    def show(self):
        print(self.q)

def main():
    l = [None] * 10
    a = 10
    for i in range(6,10):
        k = 6
        l[i] = i

    print(l)
    x = 7
    for i in range(7):
        if l[i] is  None:
            l[i] = i
            y = i

    print(l)
    show(k,a,y,l)


def show(k,a,b,l):
    print(l[6])


main()