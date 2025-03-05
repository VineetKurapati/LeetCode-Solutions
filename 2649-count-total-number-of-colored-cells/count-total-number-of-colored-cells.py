class Solution:
    def coloredCells(self, n: int) -> int:
        if n == 1:
            return 1
        count = 1
        for i in range(1, n):
            count += (i * 4)
        return count