from collections import defaultdict


# this is normal graph
class Graph:

    def __init__(self, v):
        self.graph = defaultdict(list)
        self.v = v

    def addEdge(self, v, e):
        self.graph[v].append(e)

    def dfsutil(self, v, visited, iteration_stack):
        print(v)
        visited.append(v)
        iteration_stack.append(v)

        for x in self.graph[v]:
            if x not in visited:
                if self.dfsutil(x, visited, iteration_stack):
                    return True
            elif x in iteration_stack:
                return True
        iteration_stack.pop()
        return False

    def isCyclic(self):
        visited = []
        iteration_stack = []
        for index in range(self.v):
            if index not in visited:
                if self.dfsutil(index, visited, iteration_stack):
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
