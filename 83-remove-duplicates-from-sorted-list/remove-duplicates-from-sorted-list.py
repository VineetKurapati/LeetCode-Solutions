# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None 
        if not head.next:
            return head
        slow, fast = head, head.next
        while fast:
            while fast and slow.val == fast.val:
                fast = fast.next
            slow.next = fast 
            slow = slow.next
            if slow:
                fast = fast.next 
        return head