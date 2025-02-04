class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res = float("-inf")
        n = len(nums)
        count = nums[0]
        for r in range(1, n):
            if nums[r] <= nums[r - 1]:
                res = max(count, res)
                count = 0 
            count += nums[r]
        return max(res, count)