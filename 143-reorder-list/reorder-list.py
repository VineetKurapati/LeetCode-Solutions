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
    def getLength(self, head):
        count = 0
        while head:
            count +=1 
            head = head.next 
        return count 
    def getFirstHalf(self, head):
        slow, fast = head, head.next 
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
        second_half = slow.next 
        slow.next = None 
        return second_half
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next:
            return 
        secondHalf = self.reverse(self.getFirstHalf(head))
        firstHalf = head 
        while secondHalf:
            temp1, temp2 = firstHalf.next, secondHalf.next 
            firstHalf.next = secondHalf
            secondHalf.next = temp1 
            firstHalf = temp1
            secondHalf = temp2
        