import sys
from collections import defaultdict
import msvcrt


class graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, v, w):
        self.graph[v].append(w)  # Add w to v_s list
        self.graph[w].append(v)

    def isCyclicUtil(self, v, visited, parent):

        visited[v] = True

        for i in self.graph[v]:
            if visited[i] == False:
                if (self.isCyclicUtil(i, visited, v)):
                    return True
            elif parent != i:
                return True

        return False

    def isCyclic(self):
        visited = [False] * (self.V)
        for i in range(self.V):
            if visited[i] == False:
                if (self.isCyclicUtil(i, visited, -1)) == True:
                    return True

        return False


n = int(input())
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    g = graph(a)
    arr = [int(k) for k in input().split()]
    c = 0
    d = 1
    for j in range(b):
        g.addEdge(arr[c], arr[d])
        c = c + 2
        d = d + 2
    if g.isCyclic():
        print("1")
        continue
    else:
        print("0")
        continue
