class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_exist(node, s, ans):

    if node is None:
        return "N"

    if node.left is None and node.right is None:
        return str(node.value)

    curr = node.value

    left = is_exist(node.left, s, ans)
    right = is_exist(node.right, s, ans)
    if left!="" and right!="":
        curr = curr+"*"+left+"*"+right
    else:
        return ""

    if curr in s:
        ans[0]=1
    else:
        s.add(curr)

    return ""



def exist_duplicate_sub_tree(root):

    ans = [0]
    s = set()
    is_exist(root, s, ans)
    return ans[0]


root = Node('A')
root.left = Node('B')
root.right = Node('C')
root.left.left = Node('D')
root.left.right = Node('E')
root.right.right = Node('B')
root.right.right.right = Node('E')
root.right.right.left = Node('D')


result = exist_duplicate_sub_tree(root)
print(result)