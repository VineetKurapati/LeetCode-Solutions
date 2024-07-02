class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        number_of_fresh = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    number_of_fresh += 1
        queue = deque()
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i,j,0))
        res = 0
        dirs = [[1,0], [-1, 0], [0,1], [0, -1]]
        while queue:
            curr_i, curr_j, curr_time = queue.popleft()
            res = max(res, curr_time)
            for x, y in dirs:
                next_i = curr_i + x
                next_j = curr_j + y
                next_time = curr_time + 1
                if next_i >=0 and next_i < n and next_j >=0 and next_j < m:
                    if grid[next_i][next_j] != 1:
                        continue
                    else:
                        grid[next_i][next_j] = 2
                        queue.append((next_i, next_j, next_time))
                        number_of_fresh -=1 
                    if number_of_fresh == 0:
                        return next_time
        return -1 if number_of_fresh != 0 else res

