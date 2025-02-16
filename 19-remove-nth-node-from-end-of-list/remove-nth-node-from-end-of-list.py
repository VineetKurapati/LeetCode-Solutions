# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getLength(self, head):
        count = 0 
        while head:
            count +=1 
            head = head.next 
        return count 
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        c = self.getLength(head)
        if n == c:
            return head.next 
        k = c - n - 1
        curr = head
        while k >  0:
            curr = curr.next 
            k-= 1
        if curr.next:
            curr.next = curr.next.next 
        return head