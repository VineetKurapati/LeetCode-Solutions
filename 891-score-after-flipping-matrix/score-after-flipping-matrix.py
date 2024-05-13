class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        # Optimize Row
        for i in range(n):
            if grid[i][0] == 0:
                # Since the mostt significant bit is 0 we start flipping 
                j = 0 
                while j < m:
                    if grid[i][j] == 1:
                        grid[i][j] = 0
                        j+=1
                        continue
                    else:
                        grid[i][j] = 1
                        j+=1
                        continue
        res = 0
        # Optimizing Col 
        for j in range(m):
            num_zeros = 0
            num_ones = 0
            i = 0
            while i < n:
                if grid[i][j] == 1:
                    num_ones += 1
                else:
                    num_zeros
                i+=1
            if num_ones < n/2:
                # Flipping the col
                i = 0
                while i < n:
                    if grid[i][j] == 0:
                        grid[i][j] = 1
                        i+=1
                        continue
                    else:
                        grid[i][j] = 0
                        i+=1
                        continue
        res = 0
        for row in grid:
            binary_str = ''.join(map(str, row))
            res += int(binary_str, 2)
        return res
                    