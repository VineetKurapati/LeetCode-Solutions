from typing import List

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        def dfs(x, y, min_row, min_col, max_row, max_col):
            if x < 0 or y < 0 or x >= rows or y >= cols or land[x][y] != 1 or (x, y) in visited:
                return min_row, min_col, max_row, max_col
            
            visited.add((x, y))
            
            min_row = min(min_row, x)
            min_col = min(min_col, y)
            max_row = max(max_row, x)
            max_col = max(max_col, y)
            
            min_row, min_col, max_row, max_col = dfs(x + 1, y, min_row, min_col, max_row, max_col)
            min_row, min_col, max_row, max_col = dfs(x - 1, y, min_row, min_col, max_row, max_col)
            min_row, min_col, max_row, max_col = dfs(x, y + 1, min_row, min_col, max_row, max_col)
            min_row, min_col, max_row, max_col = dfs(x, y - 1, min_row, min_col, max_row, max_col)
            
            return min_row, min_col, max_row, max_col
        
        rows, cols = len(land), len(land[0])
        visited = set()
        result = []
        
        for i in range(rows):
            for j in range(cols):
                if land[i][j] == 1 and (i, j) not in visited:
                    min_row, min_col, max_row, max_col = dfs(i, j, i, j, i, j)
                    result.append([min_row, min_col, max_row, max_col])
        
        return result
