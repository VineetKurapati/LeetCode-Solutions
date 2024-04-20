class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        n = len(land)
        m = len(land[0])
        def dfs (i, j, n, m, start_row, start_col, end_row, end_col):
            nonlocal land
            if i < 0 or j < 0 or i>=n or j>=m or land[i][j] != 1:
                return start_row, start_col, end_row, end_col
            land[i][j] = 2
            start_row = min(start_row, i)
            start_col = min(start_col, j)
            end_row = max(end_row, i)
            end_col = max(end_col, j)
            start_row, start_col, end_row, end_col = dfs(i+1, j, n, m, start_row, start_col, end_row, end_col)
            start_row, start_col, end_row, end_col = dfs(i-1, j, n, m, start_row, start_col, end_row, end_col)
            start_row, start_col, end_row, end_col = dfs(i, j+1, n, m, start_row, start_col, end_row, end_col)
            start_row, start_col, end_row, end_col = dfs(i, j-1, n, m, start_row, start_col, end_row, end_col)
            return start_row, start_col, end_row, end_col
        res = []
        for i in range(n):
            for j in range(m):
                if land[i][j] == 1:
                    start_row, start_col, end_row, end_col = dfs(i, j,n, m , i, j, i, j)
                    res.append([start_row, start_col, end_row, end_col])
        return res
        
