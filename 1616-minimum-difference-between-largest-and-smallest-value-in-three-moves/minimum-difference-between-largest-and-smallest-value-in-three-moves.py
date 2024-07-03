class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n<=4:
            return 0
        nums.sort()
        min_diff = float("inf")
        for left in range(4):
            right = n - 4 + left
            min_diff = min(min_diff, nums[right] - nums[left])
        return min_diff