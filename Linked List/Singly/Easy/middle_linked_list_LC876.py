from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow = head

        if head.next:
            fast = head.next.next
        else:
            return head
        
        counter = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            counter +=2
        
        if counter%2==0:
            return slow.next
        else:
            return slow

