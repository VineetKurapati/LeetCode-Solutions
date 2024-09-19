from collections import defaultdict

class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10**9 + 7
        max_num = 0
        while pow(max_num + 1, x) <= n:
            max_num += 1
        
        # dp[i] will be the number of ways to write i as sum of xth powers
        dp = [0] * (n + 1)
        dp[0] = 1
        
        for current in range(1, max_num + 1):
            power = pow(current, x)
            for i in range(n, power - 1, -1):
                dp[i] = (dp[i] + dp[i - power]) % MOD
        
        return dp[n]
