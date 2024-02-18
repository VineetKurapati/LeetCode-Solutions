class Solution:
    def furthestBuilding(self, h: List[int], bricks: int, ladders: int) -> int:
        n = len(h)
        pq = []
        for i in range(n-1):
            diff = h[i+1] - h[i]
            if diff <= 0:
                continue
            bricks -= diff
            heapq.heappush(pq, -diff)
            if bricks < 0:
                if ladders == 0:
                    return i
                ladders -=1
                bricks += -heapq.heappop(pq)

        return n-1