class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        def dfs(i, nums, dp):
            if i >= len(nums):
                return 0 
            if i in dp:
                return dp[i]
            step1 = nums[i] + dfs(i + 2, nums, dp)
            step2 = dfs(i + 1, nums, dp)
            dp[i] = max(step1, step2)
            return dp[i]
        return max(dfs(0, nums[:n-1], {}), dfs(0, nums[1:n], {}))