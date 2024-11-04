# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        EVEN = ListNode(-1)
        ODD = ListNode(-1)
        i = 1
        res = ODD
        t = EVEN
        while head:
            if i % 2 == 0:
                EVEN.next = ListNode(head.val)
                EVEN = EVEN.next 
            else:
                ODD.next = ListNode(head.val)
                ODD = ODD.next 
            head = head.next 
            i+=1 
        t = t.next
        ODD.next = t

        return res.next