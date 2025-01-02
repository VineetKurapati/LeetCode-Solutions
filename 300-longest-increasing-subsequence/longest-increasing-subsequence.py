class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1 for i in range(n + 1)]
        for i in range(1, n):
            j = 0 
            while j < i:
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])
                j += 1
        return max(dp)

