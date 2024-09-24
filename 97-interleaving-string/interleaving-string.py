class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)
        
        # Early return if the lengths don't match
        if len(s3) != n + m:
            return False
        
        dp = {}

        # DFS with memoization
        def dfs(i, j):
            if i == n and j == m:
                return True
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            k = i + j  
            
            if i < n and s1[i] == s3[k] and dfs(i + 1, j):
                dp[(i, j)] = True
                return True
            if j < m and s2[j] == s3[k] and dfs(i, j + 1):
                dp[(i, j)] = True
                return True
            
            dp[(i, j)] = False
            return False

        return dfs(0, 0)
