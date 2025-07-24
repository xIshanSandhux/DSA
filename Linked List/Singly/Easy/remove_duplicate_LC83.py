# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
 
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
print(s.deleteDuplicates(Head))


print(str(Head.val))
