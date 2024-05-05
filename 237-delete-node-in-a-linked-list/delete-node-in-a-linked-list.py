# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        n = node
        h = node.next
        temp = h.val
        while h:
            n.val = temp
            n = n.next
            h = h.next
            if not h:
                break
            else:
                temp = h.val
        n = node
        while n.next.next is not None:
            n = n.next
        n.next = None
        
