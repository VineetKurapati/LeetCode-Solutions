class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        def dfs(i, j):
            if i >= n or j >= m or i < 0 or j < 0 or board[i][j] != "O":
                return 
            board[i][j] = "S"
            dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for x, y in dirs:
                dfs(i + x, j + y)
        for i in range(n):
            for j in range(m):
                if (i == 0 or j == 0 or i == n-1 or j == m- 1) and board[i][j] == "O":
                    dfs(i, j)
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "S":
                    board[i][j] = "O"
