# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        cur = head
        dummy = ListNode()
        tail = dummy

        while cur and cur.next:
            if cur.val != val:
                tail.next = cur
                tail = tail.next
            cur = cur.next

        tail.next = None
        return dummy.next
 




Head = ListNode(1)
linkedList2 = ListNode(1)
linkedList3 = ListNode(2)
linkedList4 = ListNode(3)
linkedList5 = ListNode(3)
Head.next=linkedList2
linkedList2.next=linkedList3
linkedList3.next=linkedList4
linkedList4.next=linkedList5


s=Solution()
newHead = s.removeElements(Head,3)

while newHead:
    print(newHead.val)
    newHead=newHead.next



# print(str(Head.val))
