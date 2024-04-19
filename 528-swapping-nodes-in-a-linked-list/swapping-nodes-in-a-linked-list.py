# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy1 = ListNode(0)
        dummy1.next = head
        def getlen(head):
            count = 0
            while head:
                head = head.next 
                count += 1
            return count 
        n = getlen(head)
        n -= k
        dummy2 = head
        while k:
            dummy1 = dummy1.next 
            k-=1
        while n:
            dummy2 = dummy2.next
            n-=1
        temp = dummy1.val
        dummy1.val = dummy2.val
        dummy2.val = temp
        return head