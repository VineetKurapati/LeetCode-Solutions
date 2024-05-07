# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head):
        prev = None 
        curr = head
        while curr:
            temp = curr.next 
            curr.next = prev
            prev = curr
            curr = temp
        return prev
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev_head = self.reverse(head)
        carry = 0
        res = ListNode(0)
        dummy = res
        while rev_head:
            curr_val = rev_head.val
            temp = (curr_val * 2) + carry
            carry = (temp // 10)
            dummy.next = ListNode(temp % 10)
            rev_head = rev_head.next
            dummy = dummy.next
        if carry > 0:
            dummy.next = ListNode(carry)
        result = self.reverse(res.next)
        return result
            
   