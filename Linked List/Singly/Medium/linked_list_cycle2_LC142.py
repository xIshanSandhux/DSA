from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow= head
        fast=head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow==fast:
                slow=head

                while slow!=fast:
                    slow = slow.next
                    fast = fast.next
                
                return slow
            
        return None
 
Head = ListNode(3)
linkedList2 = ListNode(2)
linkedList3 = ListNode(0)
linkedList4 = ListNode(4)
Head.next=linkedList2
linkedList2.next=linkedList3
linkedList3.next=linkedList4


s=Solution()
print(s.detectCycle(Head))


# print(str(Head.val))
