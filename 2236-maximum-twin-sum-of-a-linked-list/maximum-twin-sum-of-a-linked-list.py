# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def length(self, head):
        if not head:
            return 0
        c = 0
        while head:
            c+=1 
            head = head.next 
        return c
    def reverse(self, head):
        prev = None
        while head:
            t = head.next 
            head.next = prev 
            prev = head 
            head = t
        return prev
    def pairSum(self, head: Optional[ListNode]) -> int:
        n = self.length(head)
        first_half = ListNode(-1)
        dummy = first_half
        i = 0
        while head and i < n//2:
            dummy.next = ListNode(head.val)
            dummy = dummy.next
            head = head.next 
            i += 1
        first_half = first_half.next 
        second_half = head
        second_half = self.reverse(second_half)
        global_max = 0
        while first_half and second_half:
            global_max = max(first_half.val + second_half.val, global_max)
            first_half = first_half.next 
            second_half = second_half.next 
        return global_max