# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return None
        def length(node):
            count = 0 
            while node:
                count += 1
                node = node.next 
            return count 
        mid = (length(head)//2) - 1
        dummy = head 
        while mid > 0 and dummy:
            dummy = dummy.next 
            mid -= 1
        dummy.next = dummy.next.next
        return head
