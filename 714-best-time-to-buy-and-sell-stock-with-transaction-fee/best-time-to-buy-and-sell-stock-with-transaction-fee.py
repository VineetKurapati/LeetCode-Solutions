class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        dp = {}
        
        def dfs(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            
            if buying:
                dp[(i, buying)] = max(dfs(i + 1, False) - prices[i], dfs(i + 1, True))
            else:
                dp[(i, buying)] = max(dfs(i + 1, True) + prices[i] - fee, dfs(i + 1, False))
            
            return dp[(i, buying)]
        
        return dfs(0, True)
