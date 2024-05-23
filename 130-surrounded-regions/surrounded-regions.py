class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n = len(board)
        m = len(board[0])
        def dfs(board, i, j):
            if i < 0 or j < 0 or i>=len(board) or j >= len(board[0]) or board[i][j] != "O":
                return 
            board[i][j] = "S"
            dfs(board, i+1, j)
            dfs(board, i-1, j)
            dfs(board, i, j+1)
            dfs(board, i, j-1)
        for i in range(n):
            for j in range(m):
                # Checking if they are in the boundry 
                if (i == 0 or j == 0 or i == n-1 or j == m-1) and board[i][j] == "O":
                    dfs(board, i, j)
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "S":
                    board[i][j] = "O"
