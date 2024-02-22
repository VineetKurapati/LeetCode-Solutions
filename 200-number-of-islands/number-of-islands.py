class Solution:
    def search(self, grid, i, j, n, m):
        if i < 0 or j < 0 or j >=m or i>=n or grid[i][j] != '1':
            return 
        grid[i][j] = '2'
        self.search(grid, i+1, j, n,m)
        self.search(grid, i-1,j, n,m)
        self.search(grid, i, j+1, n,m)
        self.search(grid, i, j-1,n,m)
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    self.search(grid, i,j, n,m)
                    count+=1
        return count