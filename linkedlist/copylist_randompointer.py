"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:

    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        curr = head
        while curr != None:
            newNode = Node(curr.val)
            newNode.next = curr.next
            curr.next = newNode
            curr = newNode.next

        curr = head

        while curr != None:
            if curr.random != None:
                curr.next.random = curr.random.next
            curr = curr.next.next

        curr = head
        clonedhead = curr.next
        clonedcurr = clonedhead

        while clonedcurr.next != None:
            curr.next = curr.next.next
            clonedcurr.next = clonedcurr.next.next
            curr = curr.next
            clonedcurr = clonedcurr.next

        curr.next = None
        clonedcurr.next = None
        return clonedhead

# [[7, null], [13, 0], [11, 4], [10, 2], [1, 0]]

head = Node(7)
head.next = Node(13)
head.next.next = Node(11)
head.next.next.next = Node(10)
head.next.next.next.next = Node(1)

head.next.random = head
head.next.next.random = head.next.next.next.next
head.next.next.next.random = head.next.next
head.next.next.next.next.random = head

solution = Solution()
clonedhead = solution.copyRandomList(head)

print(clonedhead)