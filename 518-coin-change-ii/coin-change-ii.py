from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        
        def dfs(amount, index):
            if amount == 0:
                return 1
            if amount < 0 or index >= len(coins):
                return 0
            if (amount, index) in dp:
                return dp[(amount, index)]
            include = dfs(amount - coins[index], index)
            exclude = dfs(amount, index + 1)
            dp[(amount, index)] = include + exclude
            return dp[(amount, index)]

        return dfs(amount, 0)
