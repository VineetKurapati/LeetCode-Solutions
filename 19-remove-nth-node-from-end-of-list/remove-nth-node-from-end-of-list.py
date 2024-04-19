# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def countlen(self, head):
        count = 0 
        while head:
            head = head.next 
            count +=1 
        return count
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        k = self.countlen(head)
        if n == k:
            return head.next
        k-=n
        dummy = ListNode(0)
        dummy.next = head
        while k and dummy:
            dummy = dummy.next 
            k-=1 
        dummy.next = dummy.next.next
        return head