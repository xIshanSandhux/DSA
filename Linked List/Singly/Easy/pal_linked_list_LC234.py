# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fastPointer = head
        slowPointer = head

        while fastPointer and fastPointer.next:
            slowPointer = slowPointer.next
            fastPointer = fastPointer.next.next
        
        cur = slowPointer
        prev = None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        
        first = head
        while prev:
            if prev.val != first.val:
                return False
            prev = prev.next
            first = first.next

        return True
 
Head = ListNode(3)
linkedList2 = ListNode(3)
linkedList3 = ListNode(2)
linkedList4 = ListNode(3)
linkedList5 = ListNode(3)
Head.next=linkedList2
linkedList2.next=linkedList3
linkedList3.next=linkedList4
linkedList4.next=linkedList5


s=Solution()
print(s.isPalindrome(Head))


# print(str(Head.val))
