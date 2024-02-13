class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)
        def solve(r,c):
            if r == n:
                return True
            if c == n:
                return solve(r+1, 0)
            if board[r][c] != ".":
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[r//3, c//3]:
                    return False
                else:
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])
                    squares[r//3, c//3].add(board[r][c])
                    return solve(r, c+1)
            else:
                return solve(r, c+1)
        return solve(0,0)