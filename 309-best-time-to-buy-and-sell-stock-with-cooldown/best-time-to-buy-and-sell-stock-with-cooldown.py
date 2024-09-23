class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}
        
        def dfs(i: int, buying: bool) -> int:
            if i >= len(prices):
                return 0
            if (i, buying) in dp:
                return dp[(i, buying)]
            if buying:
                buy = dfs(i + 1, False) - prices[i]
                skip = dfs(i + 1, True)
                dp[(i, buying)] = max(buy, skip)
            else:
                sell = dfs(i + 2, True) + prices[i]  
                skip = dfs(i + 1, False)
                dp[(i, buying)] = max(sell, skip)
            
            return dp[(i, buying)]
        
        return dfs(0, True)
