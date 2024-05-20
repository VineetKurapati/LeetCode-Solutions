# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        turtle = head 
        hare = head.next 
        while hare and hare.next:
            if turtle == hare:
                return True
            turtle = turtle.next 
            hare = hare.next.next
        return False