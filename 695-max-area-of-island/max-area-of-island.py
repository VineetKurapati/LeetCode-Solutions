class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        curr_max = 0
        vis = set()
        n = len(grid)
        m = len(grid[0])

        def dfs(i, j, curr):
            if i >= n or j >= m or i < 0 or j < 0 or grid[i][j] == 0:
                return curr
            
            if (i, j) in vis:
                return curr
            
            vis.add((i, j))
            curr += 1
            
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for x, y in directions:
                curr = dfs(i + x, j + y, curr)
                
            return curr

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1 and (i, j) not in vis:
                    curr_max = max(curr_max, dfs(i, j, 0))
        
        return curr_max
