# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def printList(self):
        temp = self
        while(temp):
            print (temp.val ,end=" ")
            temp = temp.next
        print('\n')
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not head or not head.next:
            return head
        current = head
        n = 1
        while current.next:
            if current.next != None:
                current = current.next
            else:
                break
            n += 1
        # print(n)
        # print(head)
        current.next = head
        # print(head)
        # print(current)
        # print(k%n)

        current, tail = head, current

        kth_value = n - k % n

        while kth_value > 0:
            tail = current
            current = current.next
            kth_value -= 1
        tail.next = None
        # print(kth_value)
        # print(current)

        return current

# [1,2,3,4,5]
list = ListNode(5)
list.next = ListNode(4)
list.next.next = ListNode(3)
list.next.next.next = ListNode(2)
list.next.next.next.next = ListNode(1)

list.printList()


solution = Solution()
res = solution.rotateRight(list, 2)
res.printList()

