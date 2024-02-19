# User function Template for python3

# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:

    # Function to return a list of nodes visible from the top view
    # from left to right in Binary Tree.
    def topView(self, root):

        def dfs(node, head, level, path):
            # print('hi')

            if head not in path or level < path[head][1]:
                if node:
                    path[head] = [node.data, level]

            if node.left:
                dfs(node.left, head - 1, level + 1, path)
            if node.right:
                dfs(node.right, head + 1, level + 1, path)

        res = {}
        dfs(root, 0, 0, res)
        # print(res)
        r = []
        for key in sorted(res.keys()):
            r.append(res[key][0])

        return r


if __name__ == '__main__':
    """ Create following Binary Tree
         1
        / \
       2   3
        \
          4
           \
            5
              \
               6
    output 2 1 3 6 

    """
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.right = Node(4)
    root.left.right.right = Node(5)
    root.left.right.right.right = Node(6)
    print("The top view of the tree is: ")
    s = Solution()
    r = s.topView(root)
    print(r)
