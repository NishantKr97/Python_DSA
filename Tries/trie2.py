class triesDS:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False


class tries:
    def __init__(self):
        self.node = triesDS()

    def insert(self, k):
        p = k
        temp = self.node
        t = 0
        for i in range(len(p)):
            m = ord(p[t]) - ord('a')
            if temp.children[m] is None:
                temp.children[m] = triesDS()
                temp = temp.children[m]
                t = t + 1
            else:
                temp = temp.children[m]
                t = t + 1
        temp.isEnd = True

    def search(self, key):
        p = key
        temp = self.node
        t = 0
        for i in range(len(key)):
            m = ord(p[t]) - ord('a')
            if temp.children[m] is not None:
                temp = temp.children[m]
                t = t + 1
            else:
                return False
        if temp.isEnd == True:
            return True
        else:
            return False


def main():
    l = tries()
    f = open('ispell.dict', 'r')
    d = f.readlines()
    for i in range(0,len(d)):
        a = d[i][:-1]
        l.insert(a)
    print(l.search("abdu"))


main()
