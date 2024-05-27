class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = {}
        for num in nums:
            if num not in d:
                d[num] = 0
            d[num] += 1
        for num in d:
            if d[num] == 1:
                return num