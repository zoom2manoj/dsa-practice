from collections import defaultdict

# this is normal graph
class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, v, e):
        self.graph[v].append(e)
    def bfs(self, v):

        visited = [v]
        q = [v]

        while q:
            item = q.pop(0)
            print(item)
            for x in self.graph[item]:
                if x not in visited:
                    visited.append(x)
                    q.append(x)

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
    g.bfs(2)
    # output 2 0 3 1