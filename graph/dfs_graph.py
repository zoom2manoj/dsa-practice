from collections import defaultdict

# this is normal graph
class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, v, e):
        self.graph[v].append(e)

    def dfsutil(self, v, visited):
        print(v)
        visited.append(v)
        for x in self.graph[v]:
            if x not in visited:
                self.dfsutil(x, visited)

    def dfs(self, v):

        visited = []
        self.dfsutil(v, visited)


if __name__ == '__main__':
    # Create a graph given in
    # the above diagram
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)
    print("Following is Breadth First Traversal"
          " (starting from vertex 2)")
    g.dfs(2)
    # output 2 0 3 1