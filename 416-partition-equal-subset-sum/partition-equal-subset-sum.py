class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        s = sum(nums)
        if s % 2 != 0:
            return False
        dp = {}
        def backtrack(i, count, target):
            if i>= len(nums):
                return False 
            if (i, count) in dp:
                return dp[(i, count)]
            if count == target:
                return True 
            dp[(i, count)] = backtrack(i+ 1, count + nums[i], target) or backtrack(i +1, count, target)
            return dp[(i, count)]
        return backtrack(0, 0, s//2)