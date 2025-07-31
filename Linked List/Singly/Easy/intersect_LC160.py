# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        list1 = headA
        list2 = headB

        while list1!=list2:
            list1 = list1.next if list1 else headB
            list2 = list2.next if list2 else headA

        return list1
    


# Shared part of the lists
shared1 = ListNode(3)
shared2 = ListNode(4)
shared3 = ListNode(5)
shared1.next = shared2
shared2.next = shared3

# First linked list: 1 -> 2 -> 3 -> 4 -> 5
headA = ListNode(1)
nodeA2 = ListNode(2)
headA.next = nodeA2
nodeA2.next = shared1  # intersection starts here


headB = ListNode(1)
headB.next = shared1  # intersection starts here

s=Solution()
newHead = s.removeNthFromEnd(headA,headB)

while newHead:
    print(newHead.val)
    newHead = newHead.next



# print(str(Head.val))
