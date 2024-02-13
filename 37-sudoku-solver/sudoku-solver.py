class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        n = 9
        def validSudoku(r, c, k):
            for i in range(0,9):             
                if board[i][c]==k:
                    print(board[i][c],k) 
                    return False
                if board[r][i]==k: 
                    return False
                if board[3*(r//3) + i//3][3*(c//3) + i%3]==k: 
                    return False
            return True 
        def fillBoard(r, c):
            if r == n:
                return True
            if c == n:
                return fillBoard(r+1, 0)
            if board[r][c] == ".":
                for i in range(1,10):
                    if validSudoku(r,c, str(i)):
                        board[r][c] = str(i)
                        if fillBoard(r, c+1):
                            return True
                        board[r][c] = "."
                return False
            return fillBoard(r, c+1)
        fillBoard(0,0)        

