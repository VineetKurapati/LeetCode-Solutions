# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(sel, head):
        prev = None
        curr = ListNode(0)
        curr.next = head
        
        while curr.next:
            temp = curr.next
            curr.next = temp.next
            temp.next = prev
            prev = temp
            
        return prev
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev_head = self.reverse(head)
        l = []
        curr_max = float("-inf")
        dummy = rev_head
        while dummy:
            if dummy.val >= curr_max:
                l.append(dummy.val)
                curr_max = max(curr_max, dummy.val)
            dummy = dummy.next
        res = ListNode(0)
        d = res
        for i in range(len(l)-1, -1 , -1):
            d.next = ListNode(l[i])
            d = d.next
        return res.next
        
