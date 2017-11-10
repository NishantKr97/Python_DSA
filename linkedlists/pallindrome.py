'''Done in No Auxillary space'''
class listNode:
    def __init__(self):
        self.value = 0
        self.next = None

class linkedList():
    def __init__(self):
        self.head = listNode()

    def insert(self, x):
        temp = listNode()
        temp.value = x
        temp.next = self.head.next
        self.head.next = temp

def __reversed__(self):