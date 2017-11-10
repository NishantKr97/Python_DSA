def main():
    s = input("Enter an expression: \n")
    t = len(s)
    a = []
    b = []
    i = 0
    while i < t:
        if s[i] == '(':
            a.append(s[i])
            i = i + 1
            continue
        if s[i] == ')':
            while True:
                if a[len(a)-1] is not '(' and (len(a)) > 0:
                    b.append(a.pop())
                    i = i + 1
                else:
                    a.pop()
                    break
            continue
        if s[i] == '+' or s[i] == '-':
            while True:
                if ((len(a)) > 0) and (a[len(a)-1] is '*' or a[len(a)-1] is '/' or a[len(a)-1] is '+' or a[len(a)-1] is '-'):
                    b.append(a.pop())
                else:
                    a.append(s[i])
                    i = i + 1
                    break
        elif s[i] == '*' or s[i] == '/':
            a.append(s[i])
            i = i + 1
        else:
            b.append(s[i])
            i = i + 1

    while len(a):
        if a[len(a)-1] is not '(':
            b.append(a.pop())
        else:
            a.pop()



    print(b)





main()
