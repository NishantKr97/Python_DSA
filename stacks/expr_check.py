def check(a):
    l = []
    i = 0
    while i < len(a):
        if (a[i] is '(') or (a[i] is '[') or (a[i] is '{'):
            l.append(a[i]);

        if (a[i] is ')') or (a[i] is ']') or (a[i] is '}'):
            if a[i] is ')':
                if l[len(l) - 1] is '(':
                    l.pop()
                else:
                    return False
            if a[i] is ']':
                if l[len(l) - 1] is '[':
                    l.pop()
                else:
                    return False
            if a[i] is '}':
                if l[len(l) - 1] is '{':
                    l.pop()
                else:
                    return False

        i = i + 1

    if l:
        return False

    return True


y = check('[ (a + b) + { c / [d - e] } ] ')
print("The expression is Correct : " + str(y))
