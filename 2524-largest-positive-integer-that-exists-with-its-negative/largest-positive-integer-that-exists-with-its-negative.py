class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        res = float("-inf")
        s = set()
        for n in nums:
            if -1*n in nums:
                res = max(res, n)
        return res if res!=float("-inf") else -1