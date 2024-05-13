from typing import List

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        # Toggle rows if the first element is 0
        for i in range(n):
            if grid[i][0] == 0:
                grid[i] = [1 - x for x in grid[i]]  # Invert the row

        # Toggle columns if the number of zeros is greater than the number of ones
        for j in range(1, m):
            num_ones = sum(grid[i][j] for i in range(n))
            if num_ones < n / 2:
                for i in range(n):
                    grid[i][j] = 1 - grid[i][j]  # Invert the column

        # Calculate the final sum
        res = 0
        for row in grid:
            binary_str = ''.join(map(str, row))
            res += int(binary_str, 2)

        return res
