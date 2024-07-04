# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode(0)
        dummy = res
        while head:
            count = 0
            while head.val != 0 and head:
                count += head.val
                head = head.next
            head = head.next
            if count != 0:
                res.next = ListNode(count)
                res = res.next
        return dummy.next