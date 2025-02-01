class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = {}
        def dfs(i, curr):
            if curr > amount:
                return 0
            if curr == amount:
                return 1
            if i >= len(coins):
                return 0
            if (i, curr) in dp:
                return dp[(i, curr)]
            use_coin_and_stay = dfs(i, curr + coins[i])
            dont_use_coin = dfs(i + 1, curr)
            dp[(i, curr)] = use_coin_and_stay + dont_use_coin
            return dp[(i, curr)]
        return dfs(0, 0)