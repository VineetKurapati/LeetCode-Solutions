class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        min_ = float("inf")
        for price in prices:
            min_ = min(price, min_)
            profit = price - min_
            result = max(profit, result)
        return result
