class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = []
        for g in gifts:
            heapq.heappush(heap, (-1 * g))
        while k:
            c = heapq.heappop(heap)
            s = floor(sqrt(-1 * c))
            heapq.heappush(heap, (-1 * s))
            k-=1
        return -1 * sum(heap)