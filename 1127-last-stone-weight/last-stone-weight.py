class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []
        for s in stones:
            heapq.heappush(pq, -1 * s)
        while len(pq) >= 2:
            a = -1 * heapq.heappop(pq)
            b = -1 * heapq.heappop(pq)
            if a == b:
                continue 
            else:
                heapq.heappush(pq, -1 * (a - b))
        return -1 * pq[0] if len(pq) == 1 else 0