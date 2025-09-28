class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0 
        n, m = len(grid), len(grid[0])
        dirs = [[1, 0], [0,1], [-1, 0], [0,  -1]]
        queue = deque()
        visited = set()
        def bfs(row, col):
            nonlocal visited
            nonlocal queue
            queue.append((row, col))
            while queue:
                tR, tC = queue.popleft()
                visited.add((row, col))
                for x, y in dirs:
                    nR, nC = (x + tR), (y + tC)
                    if nR >= 0 and nC >=0 and  nR < n and nC < m and grid[nR][nC] == "1" and (nR, nC) not in visited:
                        queue.append((nR, nC))
                        visited.add((nR,nC))
        numIslands = 0
        for row in range(n):
            for col in range(m):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    numIslands += 1
        return numIslands