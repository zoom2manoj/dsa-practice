class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


# // Binary tree
#   //     5
#   //   / \
#   //   1   6
#   //  /   / \
#   // 3   7   4

def count(root):
    if root is None:
        return 0
    return count(root.left)+count(root.right)+1


def checkRec(node, n, ans):

    if node is None:
        return False

    left_count = count(node.left)
    right_count = count(node.right)

    if n==n-left_count+right_count+1:
        return True
    else:
        if checkRec(node.left, n , ans):
            return True
        if checkRec(node.right, n, ans):
            return True


    return False





def count_size_check(node):

    ans = False
    total_size = count(node)
    output = checkRec(node, total_size, ans)




    return output


root = Node(5)
root.left = Node(1)
root.right = Node(6)
root.left.left = Node(3)
# root.left.right = Node(2)  # if enable this output should come as False
root.right.left = Node(7)
root.right.right = Node(4)


output = count_size_check(root)
print(output)
# if both tree node count same then truee if not same then return false