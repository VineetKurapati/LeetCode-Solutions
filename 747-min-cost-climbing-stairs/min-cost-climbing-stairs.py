class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1] * n 
        
        def dfs(i):
            if i >= n:  
                return 0
            if dp[i] != -1:  
                return dp[i]
            
            one_step = cost[i] + dfs(i + 1)
            two_steps = cost[i] + dfs(i + 2)
            
            dp[i] = min(one_step, two_steps)
            return dp[i]
        
        return min(dfs(0), dfs(1))  