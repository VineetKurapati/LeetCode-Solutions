# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        curr = ListNode(0) 
        prev = curr
        for l in lists:
            while l:
                t = l.val 
                curr.next = ListNode(t)
                curr = curr.next
                l = l.next
        prev = prev.next
        pq = []
        res = ListNode(0)
        ans = res
        while prev:
            heapq.heappush(pq, prev.val)
            prev = prev.next
        while pq:
            v = heapq.heappop(pq)
            res.next = ListNode(v)
            res = res.next
        return ans.next