# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        prev = dummy

        for x in range(left - 1):
            prev = prev.next
        curr = prev.next
        print('curr', curr.val, prev.val)
        for i in range(right - left):
            cache = curr.next
            curr.next = cache.next
            cache.next = prev.next
            prev.next = cache
        return dummy.next

    def prints(self, head):

        while (head != None):
            print(head.val, end=' ')
            head = head.next

        print()

root= ListNode(1)
root.next = ListNode(2)
root.next.next = ListNode(3)
root.next.next.next = ListNode(4)
root.next.next.next.next = ListNode(5)
solution = Solution()
resp = solution.reverseBetween(root, 2, 4)
print(resp)
solution.prints(resp)
