class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        def dfs(i, j):
            if i < 0 or j < 0 or i >=n or j >=m or board[i][j] != "O":
                return
            board[i][j] = "S"
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        for i in range(n):
            for j in range(m):
                if (i == 0 or j == 0 or i == n - 1 or j == m - 1) and board[i][j] == "O":
                    dfs(i, j)
        for i in range(n):
            for j in range(m):
                if board[i][j] == "S":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"

            