class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n 
        def dfs(i):
            if i >= n:
                return 0 
            if dp[i] != -1:
                return dp[i]
            step1 = dfs(i + 1)
            step2 = nums[i] + dfs(i + 2)
            dp[i] = max(step1, step2)
            return dp[i]
        return dfs(0)