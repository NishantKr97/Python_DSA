class binaryHeap:
    def __init__(self):
        self.l = [None] * 20

    def swap(self, a, b):
        temp = a
        a = b
        b = temp

    def insert(self, k, t):
        # print(self.l[t])
        self.l[t] = k
        p = t
        while True:
            q = p // 2
            if q == 0:
                break
            if self.l[p] > self.l[q]:
                temp = self.l[p]
                self.l[p] = self.l[q]
                self.l[q] = temp
                p = p // 2
            else:
                break

    def show(self):
        print("The priority queue is : ")
        t = 1
        while True:
            if self.l[t] is not None:
                print(self.l[t]),
                t = t + 1
            else:
                print("")
                break

    def heapify(self, k):
        t = k
        while True:
            a = (2 * t)
            b = (2 * t) + 1
            if self.l[a] is not None and self.l[b] is not None:
                if self.l[t] < self.l[a] and self.l[t] < self.l[b]:
                    if self.l[a] > self.l[b]:
                        temp = self.l[a]
                        self.l[a] = self.l[t]
                        self.l[t] = temp
                        t = a
                    else:
                        temp = self.l[b]
                        self.l[b] = self.l[t]
                        self.l[t] = temp
                        t = b
                elif self.l[t] < self.l[a] and self.l[t] > self.l[b]:
                    print("hi")
                    temp = self.l[a]
                    self.l[a] = self.l[t]
                    self.l[t] = temp
                    t = a
                elif self.l[t] > self.l[a] and self.l[t] < self.l[b]:
                    temp = self.l[b]
                    self.l[b] = self.l[t]
                    self.l[t] = temp
                    t = b
                else:
                    break
            else:
                break

    def max(self):
        print("Max element is : " + str(self.l[1]))

    def extractMax(self):
        t = 1
        k = 0
        while True:
            if self.l[t] is not None:
                k = k + 1
                t = t + 1
            else:
                break
        print("The max element extracted is " + str(self.l[1]))
        m = self.l[1]
        self.l[1] = self.l[k]
        self.l[k] = None
        # print(self.l)
        self.heapify(1)
        return m


    def insertQ(self, k, t):
        self.l[t] = k

    def buildHeap(self, l):
        p = len(l) + 1
        print(p)
        m = [None] * p
        a = 0
        for i in range(1, p):
            b = a + 1
            m[b] = l[a]
            a = a + 1

        # t = 1
        # for i in range(1,p):
        #     print(m[t])
        #     t = t + 1
        j = a
        for i in range(a):
            p = j
            print(a)
            while True:
                b = p // 2
                if b != 0:
                    # print(m[b], m[p])
                    if m[b] < m[p]:
                        temp = m[b]
                        m[b] = m[p]
                        m[p] = temp
                        p = b
                        if b == 1:
                            j = j + 1
                    else:
                        break
                else:
                    break
            j = j - 1

            print(m)


    def heapSort(self,n):
        t = n
        while t:
            self.l[n] = self.extractMax()
            t = t - 1


    def extractHeapMax(self):
        t = 1
        k = 0
        while True:
            if self.l[t] is not None:
                k = k + 1
                t = t + 1
            else:
                break
        print("The max element extracted is " + str(self.l[1]))
        m = self.l[1]
        self.l[1] = self.l[k]
        self.l[k] = None
        # print(self.l)
        self.heapifySort(1)
        return m

    def heapifySort(self):
        t = 1
        k = 0
        while True:
            if self.l[t] is not None:
                k = k + 1
            else:
                break
        


def main():
    pq = binaryHeap()
    n = int(input("size of the queue : "))
    t = 1
    for i in range(n):
        k = int(input("enter : "))
        pq.insert(k, t)
        t = t + 1
    # #
    # # pq.show()
    # # pq.max()
    # # pq.extractMax()
    # # pq.show()
    # # pq.extractMax()
    # # pq.show()
    #
    # # bh = binaryHeap()
    # t = 1
    # l = [1, 2, 3, 4, 5, 6]
    # pq.buildHeap(l)
    # # for i in range(n):
    # #     pq.insertQ(t,t)
    # #     t = t + 1
    # # pq.show()
    # # pq.heapify(1)
    # pq.show()



    pq.heapSort(n)
    pq.show()

main()
