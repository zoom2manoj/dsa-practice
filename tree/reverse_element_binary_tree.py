# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def mirror(node_left, node_right, level):
            # print(node)
            if node_left == None or node_right == None:
                return

            # print('node level', level)
            if level % 2 == 0:
                # print('changes level next', level)
                # t = node_left.val
                # node_left.val = node_right.val
                # node_right.val = t
                n1 = node_left
                n2 = node_right
                t1 = TreeNode(n1.val)
                t2 = TreeNode(n2.val)
                t2.left = n1.left
                t2.right = n1.right
                t1.left = node_right.left
                t1.right = node_right.right
                node_left = t2
                node_right = t1



            mirror(node_left.left, node_right.right, level + 1)
            mirror(node_left.right, node_right.left, level + 1)

        curr = root
        if root != None:
            mirror(curr.left, curr.right, 0)

        return curr


root = [2,3,5,8,13,21,34]
head = TreeNode(2)
head.left = TreeNode(3)
head.right = TreeNode(5)
head.left.left  = TreeNode(8)
head.left.right = TreeNode(13)
head.right.left  = TreeNode(21)
head.right.right = TreeNode(34)


curr = head
solution = Solution()
res = solution.reverseOddLevels(curr)
print(res)