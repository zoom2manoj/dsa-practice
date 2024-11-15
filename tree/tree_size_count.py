


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



def tree_count(node):
    count = 0
    if node is None:
        return 0
    left_count = tree_count(node.left)
    right_count = tree_count(node.right)
    return left_count+right_count+1

root = Node(5)
root.left = Node(1)
root.right = Node(6)
root.right.left = Node(7)
root.right.right = Node(4)
root.left.left = Node(3)

result = tree_count(root)
print(result)
