class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    left = 1 if i >= 0 and j - 1 >= 0 and grid[i][j-1] >= 1 else 0
                    right = 1 if i >= 0 and j + 1 < m and grid[i][j+1] >= 1 else 0
                    top = 1 if i - 1 >= 0 and j >= 0 and grid[i-1][j] >= 1 else 0
                    bottom = 1 if i + 1 < n and j >= 0 and grid[i+1][j] >= 1 else 0
                    count += 4 - (left + right + top + bottom)  

        print(grid)
        return count