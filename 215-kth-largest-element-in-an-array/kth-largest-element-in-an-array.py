class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []
        for n in nums:
            heapq.heappush(pq, -1 * n)
        while k:
            res = -1 * heapq.heappop(pq)
            k-=1
        return res