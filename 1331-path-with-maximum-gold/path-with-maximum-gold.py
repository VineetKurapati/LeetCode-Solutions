class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        max_gold = 0

        def dfs(i, j, current_gold):
            nonlocal max_gold
            # Collect gold in the current cell
            current_gold += grid[i][j]
            # Mark the cell as visited by setting its value to 0
            temp = grid[i][j]
            grid[i][j] = 0
            
            # Update the maximum gold collected
            max_gold = max(max_gold, current_gold)
            
            # Explore all four directions
            for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                if 0 <= x < n and 0 <= y < m and grid[x][y] > 0:
                    dfs(x, y, current_gold)
            
            # Backtrack: Restore the cell's gold value
            grid[i][j] = temp
        
        # Start DFS from each cell that contains gold
        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0:
                    dfs(i, j, 0)
        
        return max_gold
                        