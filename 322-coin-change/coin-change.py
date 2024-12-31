class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        for i in coins:
            for j in range(1, amount + 1):
                rest = j - i
                if rest >= 0:
                # print(f"For coin {i}, rest {rest}, amount {j}, dp[i] = {min(dp[i], 1 + dp[rest])}")
                    dp[j] = min(dp[j], 1 + dp[rest])    
        return dp[amount] if dp[amount] != float("inf") else -1