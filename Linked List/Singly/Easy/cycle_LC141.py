from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
        
 
Head = ListNode(3)
linkedList2 = ListNode(2)
linkedList3 = ListNode(0)
linkedList4 = ListNode(4)
Head.next=linkedList2
linkedList2.next=linkedList3
linkedList3.next=linkedList4


s=Solution()
print(s.hasCycle(Head))


# print(str(Head.val))
