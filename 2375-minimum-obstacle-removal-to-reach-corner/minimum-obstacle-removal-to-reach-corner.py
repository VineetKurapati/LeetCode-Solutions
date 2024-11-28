from heapq import heappop, heappush
from typing import List

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = [[False] * cols for _ in range(rows)]
        heap = [(0, 0, 0)]  # (obstacles, row, col)
        
        while heap:
            obstacles, i, j = heappop(heap)
            
            if i == rows - 1 and j == cols - 1:  # Reached the bottom-right corner
                return obstacles
            
            if visited[i][j]:
                continue
            visited[i][j] = True
            
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols and not visited[ni][nj]:
                    heappush(heap, (obstacles + grid[ni][nj], ni, nj))
        
        return -1  # In case there's no valid path
