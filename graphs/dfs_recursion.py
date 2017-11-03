class dfsNode:
    def __init__(self):
        self.dist = 0
        self.color = "white"
        self.pred = None


def dfs(l, x, n, t):
    x[t].color = "grey"
    for i in range(n):
        for j in range(len(l[i])):
            if x[l[i][j]].color == "white":
                x[l[i][j]].color = "grey"
                x[l[i][j]].dist = x[t].dist + 1
                dfs(l, x, n, l[i][j])
    print(t, x[t].dist)


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
x = [dfsNode() for x in range(n)]
dfs(l, x, n, t)
