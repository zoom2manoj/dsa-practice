#
#
# a = [35, 10, 31, 11, 26]
#
# for i in range(len(a)):
#     # print(i)
#
#     for j in range(i, len(a)-1):
#         print(i, j)
#         temp  = a[j]
#         next = a[j+1]
#         if temp> next:
#             a[j] = next
#             a[j+1] = temp
# print(a)




# Using a Python dictionary to act as an adjacency list
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = set() # Set to keep track of visited nodes.

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

# Driver Code
dfs(visited, graph, 'A')