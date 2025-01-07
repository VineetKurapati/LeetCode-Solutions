class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # Find the middle of the linked list using slow and fast pointers
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Split the linked list into two halves and reverse the second half
        second_half = slow.next
        slow.next = None  # Terminate the first half
        rev_sechalf = None
        curr = second_half
        while curr:
            temp = curr.next
            curr.next = rev_sechalf
            rev_sechalf = curr
            curr = temp

        # Merge the two halves
        first, second = head, rev_sechalf
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
