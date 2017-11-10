class listNode():
    def __init__(self):
        self.value = 0
        self.prev = None
        self.next = None


class linkedList():
    def __init__(self):
        self.head = listNode()

    def insert(self, x):
        temp = listNode()
        temp.next = self.head.next
        self.head.next = temp
        temp.value = x
        temp.prev = self.head
        #print(temp.value)

    def show(self):
        print("The linked list is :")
        temp = self.head.next
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def qwe(self):
        print("hi")

    def delete(self, k):
        temp = self.head.next
        i = 1
        while i is not k:
            temp = temp.next
            i = i + 1

        temp.next = temp.next.next
        temp.next.next.prev = temp

    def swap(self,a,b):
        ptr1 = listNode()
        ptr2 = listNode()
        ptr3 = listNode()
        ptr4 = listNode()
        ptr5 = listNode()
        ptr6 = listNode()
        temp = listNode()







def main():
    l = linkedList()
    l.insert(3)
    l.insert(4)
    l.insert(5)
    l.insert(6)
    l.insert(7)
    l.insert(8)
    l.insert(9)
    l.show()
    #l.qwe()
    print("The list after the deletion is : ")
    l.delete(1)
    l.show()


main()
