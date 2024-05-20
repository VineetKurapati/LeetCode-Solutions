class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        pq = []
        for n in matrix:
            for i in n:
                heapq.heappush(pq, i)
        res = -1
        while k > 0 and pq:
            res = heapq.heappop(pq)
            k-=1
        return res