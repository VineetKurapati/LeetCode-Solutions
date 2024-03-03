class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def length(node):
            count = 0
            while node:
                count += 1
                node = node.next
            return count
        k = length(head)
        if n == k:
            return head.next
        k = k - n
        dummy = ListNode(0)
        dummy.next = head
        ans = dummy
        while k > 0:
            dummy = dummy.next
            k -= 1
        if dummy.next:
            dummy.next = dummy.next.next
        return ans.next
