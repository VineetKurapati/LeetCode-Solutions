class Solution:
    def canJump(self, nums: List[int]) -> bool:
        curr = nums[0] - 1
        n = len(nums)
        for i in range(1, n):
            if curr < 0:
                return False 
            curr = max(curr, nums[i])
            curr -=1 
        return True