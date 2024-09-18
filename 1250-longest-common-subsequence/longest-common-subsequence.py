class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        res = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[j-1] == text2[i-1]:
                    print("Went in here")
                    res[i][j] = res[i-1][j-1] + 1
                else:
                    res[i][j] = max(res[i][j-1], res[i-1][j])
        return res[m][n]