class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for j in range(n)] for i in range(m)]
        for i in range(n):
            dp[m-1][i] = 1
        for i in range(m-2, -1, -1):
            for j in range(n-1, -1, -1):
                down = 0
                right = 0
                if i + 1 < m:
                    down = dp[i+1][j]
                if j + 1 < n:
                    right = dp[i][j+1]
                dp[i][j] = (down + right)
        return dp[0][0]
