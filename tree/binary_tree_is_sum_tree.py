from collections import deque
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def binary_tree_is_sum_tree(node):

    q = deque()

    q.append((node, node.value))
    result = {}
    node_child_sum_result = {}
    while q:
        temp_node = q.popleft()
        print(temp_node[0].value)
        if temp_node[1] in result:
            result[temp_node[1]] += temp_node[0].value
        else:
            result[temp_node[1]] = temp_node[0].value

        if temp_node[0].left:
            q.append((temp_node[0].left, temp_node[0].left.value))
        if temp_node[0].right:
            q.append((temp_node[0].right, temp_node[0].right.value))


    print(result)
    return False




root = Node(26)
root.left = Node(10)
root.right = Node(3)
root.right.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(6)

"""
    26
  10   3
 4  6   3
"""

result = binary_tree_is_sum_tree(root)
print('result', result)
