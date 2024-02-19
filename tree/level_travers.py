
class Node:

    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

level_data = {}
# def printLevelOrder(root, count):
#
#     # count = 0
#     if root:
#         print(root.data)
#         count+=1
#         if len(level_data)>0 and count in  level_data:
#             level_data[count].append(root.data)
#         else:
#             level_data[count] = [root.data]
#
#     if root.left:
#         printLevelOrder(root.left, count)
#     if root.right:
#         printLevelOrder(root.right, count)

def printLevelOrder(root, count):

    h  = height(root)
    # print(h)
    output = ''
    for index in range(h):
        print_level(root, index)
    print(output)

def print_level(root, i):
    if root is None:
        return
    if i==0:
        print(root.data, ' ')
    elif i>0:
        print_level(root.left, i-1)
        print_level(root.right,i-1)

def height(root):

    if root is None:
        return 0


    lheight = height(root.left)
    rheight = height(root.right)

    if lheight>rheight:
        return lheight+1
    else:
        return rheight+1

if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)

    print("Level order traversal of binary tree is -")
    printLevelOrder(root, 0)
    print(level_data)