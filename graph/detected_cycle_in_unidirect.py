from collections import defaultdict


# this is normal graph
class Graph:

    def __init__(self, v):
        self.graph = defaultdict(list)
        self.v = v

    def addEdge(self, v, e):
        self.graph[v].append(e)

    def dfsutil(self, v, visited, last):
        visited.append(v)
        for x in self.graph[v]:
            if x not in visited:
                if self.dfsutil(x, visited, v):
                    return True
            elif x != last:
                return True
        return False

    def isCyclic(self):
        visited = []
        iteration_stack = []
        q = [index for index in range(self.v)]

        while q:
            item = q.pop(0)
            for x in self.graph[item]:
                if x not in visited:
                    if self.dfsutil(x, visited, -1):
                        return True

        return False


if __name__ == '__main__':
    # Create a graph given in
    # the above diagram
    g = Graph(4)
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    if g.isCyclic() == 1:
        print("Graph contains cycle")
    else:
        print("Graph doesn't contain cycle")

    g1 = Graph(4)
    g1.addEdge(0, 1)
    g1.addEdge(1, 2)
    g1.addEdge(2, 3)

    if g1.isCyclic() == 1:
        print("Graph contains cycle")
    else:
        print("Graph doesn't contain cycle")
