from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def push(self, new_data):
        new_node = ListNode(new_data)
        new_node.next = self.next
        self.next = new_node
    def printList(self):
        temp = self
        while(temp):
            print (temp.val ,end=" ")
            temp = temp.next
        print('\n')


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        def reverseList(start, end):
            start.printList()
            end.printList()
            current_inner = start
            previous = None
            while current_inner != end:
                next  = current_inner.next
                current_inner.next = previous
                previous = current_inner
                current_inner = next
            # current = end
            return previous, end

        counter = 0
        dummy =  ListNode()
        dummy.next = head
        prev = head
        current = head
        running = ListNode()
        result  = running
        manoj_temp = None
        while current:
            counter+=1
            if counter % k==0:
                back_output, current = reverseList(prev, current.next)
                # prev.printList()
                prev = current
                running.next = back_output
                manoj_temp = current
                # running = running.next
                # current = current.next
                # print('asdf')
            else:
                while running.next:
                    running = running.next

                current = current.next
                if current==None:
                    running.next = manoj_temp


        return result.next




head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
# head.next.next.next.next = ListNode(5)
# print(head)
head.printList()

solution  = Solution()
resp = solution.reverseKGroup(head, 3)
print('==============')
resp.printList()
# llist.push(5)
# llist.push(4)
# llist.push(3)
# llist.push(2)
# llist.push(1)
# print(llist)

