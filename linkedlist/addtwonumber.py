# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], trailing=0) -> Optional[ListNode]:
        val = l1.val + l2.val + trailing
        trailing = 1 if val >= 10 else 0
        result = ListNode(val % 10)

        if (l1.next or l2.next or trailing):
            if l1.next == None:
                l1.next = ListNode(0)
            if l2.next == None:
                l2.next = ListNode(0)
            result.next = self.addTwoNumbers(l1.next, l2.next, trailing)
        return result



