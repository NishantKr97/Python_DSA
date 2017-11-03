class dfsNode:
    def __init__(self):
        self.color = "white"
        self.dist = 0
        self.pred = None


def dfs(l, n, t):
    s = [dfsNode() for x in range(n)]
    s[t].color = "grey"
    k = []
    k.append(t)
    print(k)
    for i in range(len(l)):
        u = int(k.pop())
        for j in range(len(l[u])):
            if s[l[i][j]].color == "white":
                k.append(l[i][j])
                s[l[i][j]].color = "grey"
                s[l[i][j]].pred = u
                s[l[i][j]].dist = s[u].dist + 1
        print(u, s[u].dist)


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

t = int(input("Enter source vertex : "))
dfs(l, n, t)
