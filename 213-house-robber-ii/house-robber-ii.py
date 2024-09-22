from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:  # If there's only one house, return its value.
            return nums[0]
        
        # Helper DFS function with memoization
        def dfs(i, max_size, dp):
            if i >= max_size:
                return 0
            if dp[i] != -1:
                return dp[i]
            step1 = dfs(i + 1, max_size, dp)
            step2 = nums[i] + dfs(i + 2, max_size, dp)
            dp[i] = max(step1, step2)
            return dp[i]
        
        # Case 1: Rob houses from index 0 to n-2 (exclude the last house)
        dp1 = [-1] * n
        result1 = dfs(0, n - 1, dp1)  # Range is [0, n-2]
        
        # Case 2: Rob houses from index 1 to n-1 (exclude the first house)
        dp2 = [-1] * n
        result2 = dfs(1, n, dp2)  # Range is [1, n-1]
        
        # Return the maximum of the two cases
        return max(result1, result2)
