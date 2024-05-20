# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = head 
        temp_k = k
        while k > 1:
            dummy = dummy.next 
            k-=1
        def lengthlist(root):
            count = 0 
            while root:
                root = root.next 
                count +=1 
            return count 
        n = lengthlist(head)
        n-= temp_k
        dummy1 = head
        while n >= 1 and dummy1:  
            dummy1 = dummy1.next 
            n-=1
        print(dummy1.val)
        temp = dummy.val 
        dummy.val = dummy1.val
        dummy1.val = temp 
        return head
