class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def calculate_depth(node, count=0):
    if node is None:
        print(count)
        return count

    lef = calculate_depth(node.left, count + 1)
    value = node.value
    # print(value)
    rig = calculate_depth(node.right, count + 1)

    return max(lef, rig)


root = Node(5)
root.left = Node(1)
root.right = Node(6)
root.right.left = Node(7)
root.right.right = Node(4)
root.left.left = Node(3)

result = calculate_depth(root)
print('result', result)

# output should 3
