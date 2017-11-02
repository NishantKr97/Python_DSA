class binaryNode:
    def __init__(self):
        self.left = None
        self.right = None
        self.value = None

class binaryTree:
    root = binaryNode()
    def __init__(self):
        self.node = binaryNode()

    def preOrder(self):


    def inOrder(self):


    def postOrder(self):

    def insert(self,k):
        if self.node.value is None:
            self.node.value = k
            temp = self.node
        else:
            if k < temp.value:




def main():
    b = binaryTree()
    b.insert(1)