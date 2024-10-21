class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for coin in coins:
            for amount in range(coin, amount + 1):
                dp[amount] = min(dp[amount], 1 + dp[(amount - coin)])
        if dp[amount] == float("inf"):
            return -1
        return dp[amount]