class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        n = len(nums)
        d = {}
        for num in nums:
            d[num] = d.get(num, 0) + 1
        pairs = n // 2
        for num in nums:
            if d[num] % 2 != 0:
                return False 
        return True