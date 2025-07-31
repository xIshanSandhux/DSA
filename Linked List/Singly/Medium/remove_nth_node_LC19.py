# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        count = 0
        counter=0
        dummy = ListNode()
        tail = dummy
        cur1 = head
        cur2=head

        while cur1:
            count+=1
            cur1 = cur1.next
        
        count = count-n

        while cur2:
            if counter!=count:
                tail.next = cur2
                if tail.next:
                    tail = tail.next
            cur2 = cur2.next
            counter+=1
            
        
        tail.next = None

        return dummy.next
 
Head = ListNode(1)
linkedList2 = ListNode(2)
linkedList3 = ListNode(3)
linkedList4 = ListNode(4)
linkedList5 = ListNode(5)
Head.next=linkedList2
linkedList2.next=linkedList3
linkedList3.next=linkedList4
linkedList4.next=linkedList5

head2 = ListNode(1)



s=Solution()
newHead = s.removeNthFromEnd(Head,2)

while newHead:
    print(newHead.val)
    newHead = newHead.next



# print(str(Head.val))
