class listNode():
    def __init__(self):
        self.value = 0
        self.next = None


class linkedList():
    def __init__(self):
        self.head = listNode()
        self.head1 = listNode()

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

    def insertAtIndex(self, x, i):
        temp = self.head
        link = listNode()
        flag = 1
        while (i - 1):
            if temp.next is not None:
                temp = temp.next
                i = i - 1
            else:
                print("Give Correct Index Number")
                flag = 0
                break

        if flag is not 0:
            link.value = x
            link.next = temp.next
            temp.next = link

    def search(self, x):
        temp = self.head
        while (temp is not None):
            if temp.value == x:
                # print("found")
                return True
            temp = temp.next
        return False

    def swap(self, x, y):
        temp = self.head.next

        if temp.value is x and temp.next.value is y:
            ptr = self.head
            ptr1 = temp
            ptr2 = temp.next
            ptr3 = temp.next.next

            ptr.next = ptr2
            ptr1.next = ptr3
            ptr2.next = ptr1

            return True

        while temp.next.value is not x:
            temp = temp.next
        ptr1 = temp
        ptr2 = temp.next
        ptr3 = temp.next.next

        while temp.next.value is not y:
            temp = temp.next
        ptr4 = temp
        ptr5 = temp.next
        ptr6 = temp.next.next

        ptr1.next = ptr5
        ptr2.next = ptr6
        ptr5.next = ptr3
        ptr4.next = ptr2

        return True

    def node(self, x):
        i = 0
        temp = self.head.next
        while temp.value is not x:
            i = i + 1
            temp = temp.next

        return i

    def middle(self):
        temp1 = self.head.next
        temp2 = self.head.next

        while temp2 is not None:
            temp1 = temp1.next
            temp2 = temp2.next.next

        return temp1.value

    def showFromBack(self, k):
        temp = self.head.next
        l = 0
        while temp is not None:
            l = l + 1
            temp = temp.next

        j = 0
        a = l - k
        temp = self.head.next
        while j is not a:
            j = j + 1
            temp = temp.next

        print(temp.value)

    def reverse(self):
        temp = self.head.next
        prev = None
        current = temp

        if current is None:
            print("Not Possible")
        while current.next is not None:
            ptr = current.next
            current.next = prev
            prev = current
            current = ptr

        current.next = prev
        self.head.next = current

        print("The reversed linked list is :")
        temp = self.head.next
        while temp is not None:
            print(temp.value)
            temp = temp.next


            # def loopMake(self):
            # self.head.next.next.next.next = self.head.next

    def loopDetect(self):
        ptr1 = self.head.next
        ptr2 = self.head.next

        while ptr1 and ptr2 and ptr2.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next.next
            if ptr1 is ptr2:
                return True

        return False

    def merge(self, l, k):
        ptr1 = l.head.next
        ptr2 = k.head.next
        ptr = self.head
        imp = self.head
        temp = listNode()
        while ptr1 is not None or ptr2 is not None:
            if ptr1.value < ptr2.value:
                temp.value = ptr1.value
                ptr.next = temp
                ptr = temp
                ptr1 = ptr1.next
            else:
                temp.value = ptr2.value
                ptr.next = temp
                ptr = temp
                ptr2 = ptr2.next

    def mergeShow(self):
        temp = self.head.next
        while temp is not None:
            print(temp.value)
            temp = temp.next


def main():
    l = linkedList()
    # l.insert(2)
    # l.show(l.head)
    # l.insert(3)
    # l.show(l.head)
    # l.insert(4)
    # l.show()
    l.insertAtIndex(11, 1)
    l.insertAtIndex(9, 1)
    l.insertAtIndex(7, 1)
    l.insertAtIndex(5, 1)
    l.insertAtIndex(3, 1)
    l.insertAtIndex(1, 1)

    # print("The list is")
    # l.show()
    # print("Middle element is " + str(l.middle()))
    # p = l.swap(3, 7)
    print("The list is")
    l.show()
    # print("Node is present at " + str(l.node(2)))
    # print("Middle element is " + str(l.middle()))
    # print("The element from back is")
    # l.showFromBack(4)
    # print("Loop present : " + str(l.loopDetect()))

    print(" ")

    k = linkedList()
    k.insertAtIndex(12, 1)
    k.insertAtIndex(10, 1)
    k.insertAtIndex(8, 1)
    k.insertAtIndex(6, 1)
    k.insertAtIndex(4, 1)
    k.insertAtIndex(2, 1)
    k.show()
    print(" ")
    #l.reverse()
    # l.show()
    m = linkedList()
    m.merge(l, k)
    m.mergeShow()


main()
