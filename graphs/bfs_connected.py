from sys import stdout


class graph:
    def __init__(self):
        self.dist = 1000000
        self.color = "white"
        self.pred = None


def bfsConnected(l, t, n, k, w , e):
    m = k
    v = t
    if len(l[t]) == 0:
        print(t)
        print()
        return
    s = [graph() for i in range(n)]
    s[v].dist = 0
    s[v].color = "grey"
    q = []
    q.append(t)

    while len(q) > 0:
        u = q.pop(0)
        # print(u, s[u].dist)
        for i in l[u]:
            v = s[i]
            m[i] = -1
            if v.color == "white":
                v.dist = s[u].dist + 1
                v.color = "grey"
                v.pred = s[u]
                q.append(i)
        s[u].color = "black"

    for i in range(len(m)):
        if m[i] == -1:
            w[e][i] = i
    # w[e].sort()
    flag = 1
    for i in range(e):
        if w[e] != w[i]:
            continue
        else:
            flag = 0
            break
    if flag == 1:
        for i in range(len(w[e])):
            if w[e][i] is not None:
                stdout.write(str(w[e][i]) + ' ')
        print()
    return m


n = int(input("Enter the no. of vertices : "))
print("Enter the pair of vertices untill -1 ")
x = 0

matrix = [[0 for x in range(n)] for y in range(n)]
l = [[] for x in range(n)]
while True:
    print("Enter : ")
    x = int(input())
    y = int(input())
    if x < 0 or y < 0:
        break

    # Adjacency Matrix
    matrix[x][y] = 1
    matrix[y][x] = 1

    # Adjacency List
    l[x].append(y)
    l[y].append(x)

k = 0
for i in range(n):
    print(matrix[k])
    k = k + 1
print(l)
q = [x for x in range(n)]
w = [[None] * 15 for x in range(n)]
e = 0
for i in range(len(l)):
    q = [x for x in range(n)]
    if q[i] != -1:
        q = bfsConnected(l, i, n, q, w, e)
        e = e + 1
        # for j in range(len(q)):
        #     if q[j] == -1:
        #         stdout.write(str(j) + ' ')
        # print()
