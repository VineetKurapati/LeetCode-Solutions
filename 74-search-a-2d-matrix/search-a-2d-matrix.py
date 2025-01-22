class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        total_length = m * n 
        l, r = 0, total_length - 1
        while l <= r:
            mid = l + (r - l)//2
            row = mid // m
            col = mid % m
            if matrix[row][col] == target:
                return True 
            if matrix[row][col] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False
