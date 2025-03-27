class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        c = Counter(nums)
        n = len(nums)
        dominant = -1
        for i in c:
            if c[i] >= n//2:
                dominant = i
        if dominant == -1:
            return -1 
        res = float("inf")
        count_first = 0
        for i in range(n - 1):
            if nums[i] == dominant:
                count_first += 1
            count_second = c[dominant] - count_first
            a, b = i + 1, n - (i + 1)
            if count_first * 2 > a and count_second * 2 > b:
                res = min(res, i )
        return res if res != float("inf") else -1
