class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def depth(node):
    if node is None:
        return 0
    return 1+max(depth(node.left), depth(node.right))

def is_valid(node, d):
    if node is None:
        return True
    if node.left is None and node.right is None:
        return d==1

    if node.left is None or node.right is None:
        return False

    return  is_valid(node.left, d-1) and is_valid(node.right, d-1)


def check_pefect_tree(root):

    total_depth = depth(root)
    res = is_valid(root, total_depth)
    return res

# Binary tree
#           10
#        /     \
#      20       30
#     /  \     /  \
#   40    50  60   70
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(50)
root.right.left = Node(60)
root.right.right = Node(70)

output  = check_pefect_tree(root)
print(output)

