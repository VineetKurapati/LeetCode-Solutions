class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1] * n 
        def dfs(i, cost, n):
            nonlocal dp 
            if i >=n:
                return 0
            if dp[i] != -1:
                return dp[i]
            step1 = cost[i] + dfs(i + 1, cost, n)
            step2 = cost[i] + dfs(i + 2, cost, n)
            dp[i] = min(step1, step2)
            return dp[i]
        return min(dfs(0, cost, n), dfs(1, cost, n))