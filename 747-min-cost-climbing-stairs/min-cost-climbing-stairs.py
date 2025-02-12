class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = {}
        def dfs(i):
            if i >= len(cost):
                return 0 
            if i in dp:
                return dp[i]
            step1 = cost[i] + dfs(i + 1)
            step2 = cost[i] + dfs(i + 2)
            dp[i] = min(step1, step2)
            return dp[i]
        return min(dfs(0), dfs(1)) 
