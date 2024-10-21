class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        vis = {}
        def backtrack(i, holding):
            if i == len(prices):
                return 0
            if (i, holding) in vis:
                return vis[(i, holding)]
            if holding:
                sell = prices[i] + backtrack(i + 1, 0)
                hold = backtrack(i + 1, 1)   
                vis[(i, holding)] = max(sell, hold)
            else:
                buy = -prices[i] + backtrack(i + 1, 1)  
                skip = backtrack(i + 1, 0) 
                vis[(i, holding)] = max(buy, skip)
            return vis[(i, holding)]
        return backtrack(0, 0)