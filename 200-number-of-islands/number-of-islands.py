class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        count = 0
        def dfs(i, j, n, m):
            if i < 0 or j < 0 or i >=n or j >=m or grid[i][j] != "1":
                return 
            grid[i][j] = "2"
            dfs(i+1, j, n, m)
            dfs(i, j+1, n, m)
            dfs(i-1, j, n, m)
            dfs(i, j-1, n, m)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    dfs(i, j, n, m)
                    count += 1
        return count 