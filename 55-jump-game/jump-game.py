class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr = nums[0]
        n = len(nums)
        if n == 0 or n ==1:
            return True
        for i in range(n):
            if i == n-1 and curr >= 0:
                return True 
            if curr < 0:
                return False
            curr = max(curr, nums[i])
            curr-=1 
        return False 