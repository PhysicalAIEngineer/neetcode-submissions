# Brute Force Code 
class Solution:
    def __init__(self):
        # list to store all valid board configurations
        self.result = []
    # check whether placing a queen at row & col is safe
    def isValid(self, board: list[str], row: int, col: int) -> bool:
        # total number of rows or columns on the board
        n = len(board)
        # check the same column in all previous rows
        for i in range(row, -1, -1):
            if board[i][col] == 'Q':
                return False
        # check the upper-left diagonal
        i = row
        j = col
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        # check the upper-right diagonal
        i = row
        j = col
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        # no need to check downward directions because queens are placed row by row from top to bottom
        return True
    # backtracking function to place queens row by row
    def solve(self, board: list[list[str]], row: int) -> None:
        # if queens have been placed in all rows, store the board
        if row == len(board):
            self.result.append(["".join(r) for r in board])
            return
        # try placing a queen in every column of the current row
        for col in range(len(board)):
            # check whether the current position is safe
            if self.isValid(board,row,col):
                # place the queen
                board[row][col] = 'Q'
                # recur for the next row
                self.solve(board,row + 1)
                # remove the queen to explore other possibilities
                board[row][col] = '.'
    # return all valid N-Queens configurations
    def solveNQueens(self, n: int) -> list[list[str]]:
        # if the board size is zero, return an empty list
        if n == 0:
            return []
        # clear any previous results
        self.result = []
        # create an empty n x n chessboard
        board = [['.' for _ in range(n)] for _ in range(n)]
        # start placing queens from the first row
        self.solve(board,0)
        # return all valid board configurations
        return self.result

# Time Complexity : O(N! * N)
# Space Complexity : O(N^2)