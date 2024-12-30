class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10**9 + 7
        dp = {}
        def backtrack(temp):
            if low <= temp and high == temp:
                return 1
            if temp in dp:
                return dp[temp]
            if high < temp:
                return 0
            dp[temp] = 1 if temp >= low else 0
            dp[temp] += backtrack(temp + zero) + backtrack(temp + one)
            return dp[temp] % MOD 
        return backtrack(0)