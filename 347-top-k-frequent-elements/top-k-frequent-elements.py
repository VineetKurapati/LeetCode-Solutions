class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = Counter(nums)
        pq = []
        res = []
        for n in d:
            heapq.heappush(pq, (-1 * d[n], n))
        while k:
            _, num = heapq.heappop(pq)
            res.append(num)
            k-=1
        return res