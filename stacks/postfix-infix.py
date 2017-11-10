l = ['a','-','b','*','c','/','d','+','e']
a = []
x = ''
p = len(l)
i = 0
while i < p-1:
    if (l[i] is '+') or (l[i] is '-'):
       a.append(x)
       x = l[i]

    if (l[i] is '*') or (l[i] is '/'):
        a.append(l[i+1])
        a.append(l[i])
        i = i + 1

    if (l[i] is not '+') and (l[i] is not '-') and (l[i] is not '*') and (l[i] is not '/'):
        #print(l[i])
        a.append(l[i])

    i = i + 1
a.append(x)
print(a)
print(l)

