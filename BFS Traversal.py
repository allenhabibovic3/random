from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, src):
        visited = [False] * len(self.graph)
        queue = []

        queue.append(src)
        visited[src] = True

        while queue:
            s = queue.pop(0)
            print(s, end=' ')

            for i in self.graph[s]:
                if visited[i] == False:
                    visited[i] = True
                    queue.append(i)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is DFS from (starting from vertex 2)")
g.BFS(2)
