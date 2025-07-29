from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
        
 
Head = ListNode(3)
linkedList2 = ListNode(2)
linkedList3 = ListNode(7)
linkedList4 = ListNode(4)
linkedList5 = ListNode(4)
Head.next=linkedList2
linkedList2.next=linkedList3
linkedList3.next=linkedList4


s=Solution()
s.deleteNode(linkedList3)


# print(str(Head.val))
