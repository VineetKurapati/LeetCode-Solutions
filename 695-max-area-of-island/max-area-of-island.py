class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        count = 0 
        n = len(grid)
        m = len(grid[0])
        vis = set()
        def dfs(i, j, c):
            if i >=n or j >= m or i < 0 or j < 0 or grid[i][j] != 1 or (i, j) in vis:
                return 0
            c = 1
            vis.add((i, j))
            dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for x, y in dirs:
                c += dfs(i + x, j + y, c)
            return c
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (i, j) not in vis:
                    count = max(count, dfs(i, j, 0))
        return count

            
