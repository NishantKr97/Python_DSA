class listNode:
    def __init__(self):
        self.value = 0
        self.next = None


class linkedList:
    def __init__(self):
        self.head = listNode()
        self.m = [None] * 13

    def insert(self, x):
        temp = listNode()
        temp.value = x
        temp.next = self.head.next
        self.head.next = temp

    def show(self):
        print("The linked list is :")
        temp = self.head.next
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def removeDuplicates(self):
        temp = self.head.next
        while temp is not None:
            ptr = temp.next
            while ptr is not None:
                if ptr.value is temp.value:
                    temp.next = temp.next.next
                    ptr = temp.next
                else:
                    ptr = ptr.next
            temp = temp.next

    def hash(self):
        temp = self.head.next
        # print(temp.value)
        while temp is not None:
            t = temp.value % 13
            while self.m[t] is not None:
                t = t + 1
            self.m[t] = temp.value
            temp = temp.next

    def remByHash(self):
        i = 0
        while i < 12:
            if self.m[i] is self.m[i + 1]:
                self.m[i] = None
                #print(self.m[i])
            i = i + 1

    def showRem(self):
        i = 0
        print("The list after removing duplicate is : ")
        while i < 12:
            if self.m[i] is not None:
                print(self.m[i])
            i = i + 1

def main():
    l = linkedList()
    l.insert(1)
    l.insert(1)
    l.insert(3)
    l.insert(3)
    l.insert(5)

    # l.show()

    # l.removeDuplicates()
    l.show()
    l.hash()
    l.remByHash()
    l.showRem()


main()
