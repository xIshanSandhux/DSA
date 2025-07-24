# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        cur = head

        while cur is not None:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
            
        
        return prev
 
Head = ListNode(1)
linkedList2 = ListNode(2)
linkedList3 = ListNode(3)
linkedList4 = ListNode(4)
Head.next=linkedList2
linkedList2.next=linkedList3
linkedList3.next=linkedList4
print(str(Head.next.val))