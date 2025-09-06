import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        s = {}
        for n in nums:
            s[n] = s.get(n, 0) + 1
        h = []
        for n in s:
            heapq.heappush(h, (-1 *s[n], n))
        res = []
        if k > len(s):
            return []
        for i in range(k):
            t = heapq.heappop(h)
            res.append(t[1])
        return res