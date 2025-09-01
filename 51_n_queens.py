from typing import List
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        self.res = []
        self.n = n
        self.board = [["."] * self.n for _ in range(self.n)] 
        print(self.board)
        # A set to record all the viisted cols
        self.cols = set()
        # Upper right diagonal: row + col are the same
        self.diag1 = set() 
        # Upper right diagonal: row - col are the same
        self.diag2 = set()
        self.backtrack(0)
        return self.res
    
    def backtrack(self, row):
        # Base case: If we've already reached the end
        if row == self.n:
            # I forgot to append the board to the result
            print(self.board)
            solution = ["".join(row) for row in self.board]
            print(solution)
            self.res.append(solution)
        # We will try all the possible columns for the current row
        for col in range(self.n):
            if col in self.cols or row + col in self.diag1 or row - col in self.diag2:
                continue
            # Place Queen
            self.board[row][col] = "Q"
            self.cols.add(col)
            self.diag1.add(row + col)
            self.diag2.add(row - col)
            # Go into the next level
            self.backtrack(row + 1)
            # Unplace queen
            self.board[row][col] = "."
            self.cols.remove(col)
            self.diag1.remove(row + col)
            self.diag2.remove(row - col)
