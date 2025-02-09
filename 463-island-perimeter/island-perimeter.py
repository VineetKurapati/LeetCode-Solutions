class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        vis = set()
        n = len(grid)
        m = len(grid[0])
        def dfs(i, j):
            if i >= n or j >= m or i < 0 or j < 0 or grid[i][j] == 0:
                return 1
            if (i, j) in vis:
                return 0 
            vis.add((i, j))
            ans = dfs(i + 1, j) + dfs(i - 1, j) + dfs(i, j + 1) + dfs(i, j - 1)
            return ans 
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return dfs(i, j)