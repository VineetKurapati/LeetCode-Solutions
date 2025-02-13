class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0
        for n in s:
            if n - 1 not in s:
                x = n 
                count = 0
                while x in s:
                    count += 1
                    x += 1
                res = max(count, res)
        return res
