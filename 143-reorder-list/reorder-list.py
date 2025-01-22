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
            count += 1
            head = head.next
        return count

    def getFirstHalf(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second_half = slow.next  # Save the head of the second half
        slow.next = None  # Break the list into two halves
        return second_half

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next or not head.next.next:
            return
        
        # Step 1: Get the second half of the list and reverse it
        secondHalf = self.reverse(self.getFirstHalf(head))
        
        # Step 2: Merge the two halves
        firstHalf = head
        while secondHalf:
            temp1, temp2 = firstHalf.next, secondHalf.next
            firstHalf.next = secondHalf
            secondHalf.next = temp1
            firstHalf = temp1
            secondHalf = temp2
