class TreeNode:
    def __init__(self, val):
        self.key = val
        self.parent = None
        self.right_child = None
        self.left_child = None


class ParseTree:
    def __init__(self):
        self.root = TreeNode('')

    def eval(self, lis):
        current = self.root
        for i in lis:
            if i == '(':
                t = TreeNode('')
                current.left_child = t
                t.parent = current
                current = t
            elif i == ')':
                current = current.parent
            elif i in "0123456789":
                current.key = i
                current = current.parent
            else:
                current.key = i
                t = TreeNode('')
                current.right_child = t
                t.parent = current
                current = t

    def preFix(self, temp):
        if temp is None:
            return
        else:
            print(temp.key),
            if temp.left_child is not None:
                self.preFix(temp.left_child)
            if temp.right_child is not None:
                self.preFix(temp.right_child)

    def postFix(self, temp):
        if temp is None:
            return
        else:
            if temp.left_child is not None:
                self.postFix(temp.left_child)
            if temp.right_child is not None:
                self.postFix(temp.right_child)
            print(temp.key),

    def inFix(self, temp):
        if temp is None:
            return
        else:
            if temp.left_child is not None:
                self.inFix(temp.left_child)
            print(temp.key),
            if temp.right_child is not None:
                self.inFix(temp.right_child)

    def evaluate(self, temp, lis):
        if temp is None:
            return lis
        else:
            if temp.left_child is not None:
                self.evaluate(temp.left_child, lis)
            if temp.right_child is not None:
                self.evaluate(temp.right_child, lis)
            lis.append(temp.key)
            return lis

    def level(self, temp):
        if temp is None:
            return
        else:
            print(temp.key),
            if temp.left_child is not None:
                print(self.inFix(temp.left_child))
            if temp.right_child is not None:
                print(self.inFix(temp.right_child))


def calc(x, y, opr):
    if opr == '+':
        return (int(x) + int(y))
    elif opr == '-':
        return (int(y) - int(x))
    elif opr == '*':
        return (int(x) * int(y))
    else:
        return (int(y) / int(x))


def value(lis):
    val = []
    for i in lis:
        if i in "0123456789":
            val.append(i)
        else:
            x = val.pop()
            y = val.pop()
            num = calc(x, y, i)
            val.append(num)
    return val.pop()


P = ParseTree()
expr = input("Enter expression:\n")
lis = list(expr)
l = len(lis)
P.eval(lis)
print("Prefix:")
#P.preFix(P.root)
print("\nPostFix:")
#P.postFix(P.root)
print("\nInfix:")
#P.inFix(P.root)
#lis1 = P.evaluate(P.root, [])
print("\nValue of the expression is: ")
#print(value(lis1))

P.level(P.root)
