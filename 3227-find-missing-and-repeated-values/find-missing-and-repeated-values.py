class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        m = len(grid[0])
        s = set()
        res = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] in s:
                    res.append(grid[i][j])
                s.add(grid[i][j])
        for i in range(1, n**2 + 1):
            if i not in s:
                res.append(i)
        return res