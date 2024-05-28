class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        count = 0
        def dfs(grid, i, j, n, m):
            if i < 0 or j < 0 or i >=n or j >= m or grid[i][j] != "1":
                return 
            # Marking the spot as visited
            grid[i][j] = "2"
            directions  = [[0,1], [0, -1], [1,0], [-1, 0]]
            for u,v in directions:
                dfs(grid, i+v, j+u, n, m)
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    dfs(grid, i, j, n, m)
                    count += 1
        
        return count