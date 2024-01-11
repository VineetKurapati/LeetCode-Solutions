from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        fresh = 0
        time = 0
        queue = []
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for r in range(n):
            for c in range(m):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    queue.append([r, c])

        while queue and fresh > 0:
            size = len(queue)  # To process all oranges at the current time step
            for _ in range(size):
                row, col = queue.pop(0)
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if 0 <= r < n and 0 <= c < m and grid[r][c] == 1:
                        fresh -= 1
                        grid[r][c] = 2
                        queue.append([r, c])
            time += 1

        return -1 if fresh > 0 else time
