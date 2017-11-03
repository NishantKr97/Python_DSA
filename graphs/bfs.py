class graph:
    def __init__(self):
        self.dist = 1000000
        self.color = "white"
        self.pred = None


def bfs(l, t, n):
    s = [graph() for i in range(n)]
    s[t].dist = 0
    s[t].color = "grey"
    q = []
    q.append(t)

    while (len(q) > 0):
        u = q.pop(0)
        print(u, s[u].dist)

        for i in l[u]:
            v = s[i]
            if v.color == "white":
                v.dist = s[u].dist + 1
                v.color = "grey"
                v.pred = s[u]
                q.append(i)
        s[u].color = "black"


n = int(input("Enter the no. of vertices : "))
print("Enter the pair of vertices untill -1 ")
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

print("Enter the source vertex no.")
t = int(input())
bfs(l, t, n)
