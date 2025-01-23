class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        pq = []
        for i in d:
            freq = d[i]
            heapq.heappush(pq, (-1 * freq, i))
        res = []
        while k:
            _, r = heapq.heappop(pq)
            res.append(r)
            k-=1 
        return res 