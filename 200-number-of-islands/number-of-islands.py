class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        count = 0 
        def dfs(i, j):
            if i >= n or j >= m or i < 0 or j < 0 or grid[i][j] != "1":
                return 
            grid[i][j] = "2"
            dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for x, y in dirs:
                dfs(i + x, j + y)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        return count