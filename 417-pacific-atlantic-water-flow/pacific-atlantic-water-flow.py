class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])
        pac, atl = set(), set()
        def dfs(i, j, vis, prevHeight):
            if i < 0 or j < 0 or i >= n or j >= m or heights[i][j] < prevHeight or (i, j) in vis:
                return 
            vis.add((i, j))
            dfs(i + 1, j, vis, heights[i][j])
            dfs(i - 1, j, vis, heights[i][j])
            dfs(i, j + 1, vis, heights[i][j])
            dfs(i, j - 1, vis, heights[i][j])

        for c in range(m):
            # check the pacific ocean in the first row 
            dfs(0, c, pac, heights[0][c])
            # check for the last row as well 
            dfs(n - 1, c, atl, heights[n-1][c])
        
        for r in range(n):
            # Check the first column for the pacific ocean 
            dfs(r, 0, pac, heights[r][0])
            
            # Check the last Column for the atlantic ocean 
            dfs(r, m - 1, atl, heights[r][m - 1])
        res = []
        for r in range(n):
            for c in range(m):
                if (r, c) in atl and (r, c) in pac:
                    res.append([r, c])
        return res