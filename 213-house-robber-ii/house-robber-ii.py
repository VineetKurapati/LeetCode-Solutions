class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        n = len(nums)
        def dfs(i, n, nums, dp):
            if i >= n:
                return 0
            if dp[i] != -1:
                return dp[i]
            # rob the current house
            step1 = nums[i] + dfs(i+ 2, n, nums, dp)
            step2 = dfs(i + 1, n, nums, dp)
            dp[i] = max(step1, step2)
            return dp[i]
        return max(dfs(0, n-1, nums, [-1] * n), dfs(1, n, nums, [-1] * n))            