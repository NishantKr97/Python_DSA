class binaryheap:
    def __init__(self):
        self.A = []
        self.i = -1

    # self.A.append(0)
    def insert(self, x):
        self.i = self.i + 1
        self.A.append(x)
        n = self.i
        while n != 0:
            if self.A[int((n - 1) / 2)] > x:
                t = self.A[int((n - 1) / 2)]
                self.A[int((n - 1) / 2)] = self.A[n]
                self.A[n] = t
                n = int((n - 1) / 2)
            else:
                break
        return True

    def PrintArray(self):
        for j in range(len(self.A)):
            print(self.A[j], end=' ')
        print('')

    def Heapify(self, j):
        if (2 * j + 2) > self.i:
            return True

        if self.A[2 * j + 1] > self.A[2 * j + 2]:
            t = 2 * j + 1
        else:
            t = 2 * j + 2
        if self.A[j] > self.A[t]:
            m = self.A[j]
            self.A[j] = self.A[t]
            self.A[t] = m
            self.Heapify(t)
        else:
            return True

    def minimum(self):
        return self.A[0]

    def ExtractMin(self):  # Extract MAx made for hipsort
        n = self.A[0]
        self.A[0] = self.A[self.i]
        self.A[self.i] = None
        self.i = self.i - 1
        self.Heapify(0)
        # self.i=self.i+1
        return n

    def ExtractMinN(self):  # NOrmal Extract Max
        n = self.A[0]
        self.A[0] = self.A[self.i]
        self.A[self.i] = None
        self.Heapify(0)
        return n

    def Search(self, n):
        for j in range(self.i):
            if n == self.A[j]:
                return True
        return False

    def return_array(self):
        return self.A


def heap_build(A):
    P = binaryheap()
    for i in range(len(A)):
        P.insert(A[i])
    A = P.return_array()
    return A


import random


def main():
    S = binaryheap()

    for i in range(20):
        S.insert(random.randint(-100, 100))
    S.PrintArray()


if __name__ == '__main__':
    main()