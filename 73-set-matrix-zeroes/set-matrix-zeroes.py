class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        hash_table_row = set()
        hash_table_col = set()
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    hash_table_row.add(i)
                    hash_table_col.add(j)
        # Setting all the row values to Zero
        for row in hash_table_row:
            for col in range(m):
                matrix[row][col] = 0
        # Setting all the col values to Zero
        for col in hash_table_col:
            for row in range(n):
                matrix[row][col] = 0
        