class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def length(node):
            count = 0
            while node:
                count += 1
                node = node.next
            return count
        
        # Calculate the length of the linked list
        k = length(head)
        
        # Edge case: If the node to be removed is the head node
        if n == k:
            return head.next
        
        # Calculate the position of the node to be removed
        k = k - n
        
        # Initialize a dummy node
        dummy = ListNode(0)
        dummy.next = head
        ans = dummy
        
        # Traverse the list until reaching the node before the one to be removed
        while k > 0:
            dummy = dummy.next
            k -= 1
        
        # Remove the nth node from the end
        if dummy.next:
            dummy.next = dummy.next.next
        
        return ans.next
