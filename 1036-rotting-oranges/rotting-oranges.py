class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n = len(grid) 
        m = len(grid[0])
        queue = deque()
        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))
                if grid[i][j] == 1:
                    count += 1
        res = 0
        vis = set()
        dirs = [[0,1], [1, 0], [-1, 0], [0,-1]]
        while queue:
            curr_i, curr_j, curr_time = queue.popleft()
            res = max(curr_time, res)
            for x, y in dirs:
                X = curr_i + x
                Y = curr_j + y 
                if 0 <= X < n and 0 <= Y < m and grid[X][Y] == 1 and (X, Y) not in vis:
                    vis.add((X, Y))
                    queue.append((X, Y, curr_time + 1))
                    count -=1
        if count > 0:
            return -1
        return res
            