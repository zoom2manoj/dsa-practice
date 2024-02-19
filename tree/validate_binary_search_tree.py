# Definition for a binary tree node.
from typing import List, Optional
import sys
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    def inRange(self, min, mid, max):
        return mid>min and mid<max

    def isValid( self, node, min, max):
        # flage = True
        # while flage:
        #
        #     if not node:
        #         return True
        #
        #     left = self.isValid(node.left, min, node.val)
        #     right = self.isValid(node.right, node.val, max)
        #     print(left, right, node.val, ' and resp ', ( not left and not right ))
        #     if ( not left and not right ):
        #         flage == False
        #
        #     print(min, node.val, max, self.inRange(min, node.val, max))
        #     flage =  self.inRange(min, node.val, max)
        #     # return self.inRange(min, node.val, max)

        if not node:
            return True

        if min>=node.val and node.val>=max:
            return False

        if not self.isValid(node.left, min, node.val):
            return False
        if not self.isValid(node.right, node.val, max):
            return False

        return True

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # root.left, root.val, root.right
        max_size = sys.maxsize
        min_size = -sys.maxsize - 1
        # return isValid(root, min, max)
        resp  = self.isValid(root, min_size, max_size)
        print(resp)
        return resp


input =[2,1,3]
# input = [5,1,4,None,None,3,6]

solution = Solution()
#
root = TreeNode(input[0])
root.left = TreeNode(input[1])

root.right = TreeNode(input[2])

# root =  TreeNode(input[0])
# root.left =  TreeNode(input[1])
# root.right =  TreeNode(input[2])
#
# root.left.left = None
# root.left.right = None
# root.right.left = TreeNode(input[5])
# root.right.right =  TreeNode(input[6])





res  = solution.isValidBST(root)
print(res)
