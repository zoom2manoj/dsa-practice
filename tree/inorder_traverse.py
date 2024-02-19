# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # root.left, root.val, root.right
        root_value = []

        def collect_value(nodes):
            if nodes != None:
                collect_value(nodes.left)

                root_value.append(nodes.val)
                collect_value(nodes.right)

        collect_value(root)
        return root_value




input =[1,None,2,3]

solution = Solution()
root = TreeNode(input[0])
root.right = TreeNode(2)
root.right.left = TreeNode(3)



print(root)


res  = solution.inorderTraversal(root)
print(res)
