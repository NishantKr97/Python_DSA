class listnode:
    def __init__(self):
        self.value = 0
        self.next = None


class queue:
    def __init__(self):
        self.head = listnode()

    def enqueue(self, i):
        temp = self.head.next
        temp1 = self.head
        while temp is not None:
            temp1 = temp
            temp = temp.next

        ptr = listnode()
        ptr.value = i
        ptr.next = None
        temp1.next = ptr

    def show(self):
        temp = self.head.next
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def dequeue(self):
        temp = self.head.next
        prev = self.head
        while temp.next is not None:
            prev = temp
            temp = temp.next

        y = temp.value
        prev.next = temp.next

        return y




def main():
    l = queue()
    for i in range(5):
        l.enqueue(i)
    l.show()

    p = l.dequeue()
    print(p)
    l.show()

main()