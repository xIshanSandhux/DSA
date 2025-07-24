# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()
        tail = dummyNode

        while list1 and list2:
            if list1.val<list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummyNode.next
 
Head = ListNode(1)
linkedList2 = ListNode(2)
linkedList3 = ListNode(4)
Head.next=linkedList2
linkedList2.next=linkedList3


Head2 = ListNode(1)
linkedList4 = ListNode(3)
linkedList5 = ListNode(4)
Head2.next=linkedList4
linkedList4.next=linkedList5

s=Solution()
print(s.mergeTwoLists(Head,Head2))


print(str(Head.val))
print(str(Head2.val))