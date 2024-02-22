from typing import List

class Solution:
    def search(self, board, i, j, n, m):
        if i < 0 or j < 0 or i >= n or j >= m or board[i][j] != "O":
            return
        board[i][j] = "Y"
        self.search(board, i+1, j, n, m)
        self.search(board, i-1, j, n, m)
        self.search(board, i, j+1, n, m)
        self.search(board, i, j-1, n, m)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        n = len(board)
        m = len(board[0])

        # Search and mark 'O's connected to the boundary
        for i in range(n):
            for j in range(m):
                if (i == 0 or j == 0 or i == n - 1 or j == m - 1) and board[i][j] == "O":
                    self.search(board, i, j, n, m)

        # Flip 'O's to 'X's and revert marked 'Y's back to 'O's
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "Y":
                    board[i][j] = "O"
