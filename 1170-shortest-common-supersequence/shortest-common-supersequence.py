class Solution:
    def lcs(self, str1, str2):
        n = len(str1)
        m = len(str2)
        dp = [[""] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + str1[i - 1]
                else:
                    dp[i][j] = dp[i - 1][j] if len(dp[i - 1][j]) > len(dp[i][j - 1]) else dp[i][j - 1]
        return dp[n][m]

    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        lcs = self.lcs(str1, str2)
        res = []
        i, j = 0, 0
        for c in lcs:
            while i < len(str1) and str1[i] != c:
                res.append(str1[i])
                i += 1
            while j < len(str2) and str2[j] != c:
                res.append(str2[j])
                j += 1
            res.append(c)
            i += 1
            j += 1

        # Append any remaining characters in str1 and str2.
        res.append(str1[i:])
        res.append(str2[j:])
        return "".join(res)
