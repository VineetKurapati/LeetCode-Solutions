class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = max(piles)
        l, r = 1, n
        res = float("inf")
        while l <= r:
            mid = l + (r - l)//2
            total_hours = 0
            for p in piles:
                total_hours += ceil(p/mid)
            if total_hours <= h:
                res = min(mid, res)
                r = mid - 1
            else:
                l = mid + 1
        return res
                