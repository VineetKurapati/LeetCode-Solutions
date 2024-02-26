class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = []
        stones.sort(reverse = True)
        for stone in stones:
            heapq.heappush(pq, -stone)
        while len(pq) >=2 and pq[0] != 0:
            a = -1 * heapq.heappop(pq)
            b = -1 * heapq.heappop(pq)
            if a != b:
                t = abs(a-b)
                heapq.heappush(pq, -t)
            if a == b:
                heapq.heappush(pq, 0)
        return -1 * pq[0]