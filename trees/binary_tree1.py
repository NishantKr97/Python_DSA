class bt:
    def __init__(self):
        self.left = None
        self.right = None
        self.value = 0


class trees:
    def __init__(self):
        self.root = bt()
    def insert(self):
        self.root = 1
        self.root.left = 2
        self.root.right = 3
        self.root.left.left = 4
        self.root.left.right = 5
        self.root.right.left = 6
        self.root.right.right = 7

    def show(self,k):
        print(self.show(self.left))
        print(self.show(self.left))


#l = trees()
#l.insert()
#l.show(l.left)

l = []
l.append(2)
l.append(3)
l.append(4)
l.append(5)
l.append(6)
l.append(7)

print(l)
l.pop()
print(l)
print(l[len(l)-1])
