"""
79. Word Search
Because we're looking for a whole word, so we need the whole branch, so this
is a backtracking problem.
"""
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.res = False
        self.m = len(board)
        self.n = len(board[0])
        for i in range(self.m):
            for j in range(self.n):
                self.dfs(board, word, i, j, 0)
                # If we've found the word, we can return immediately
                if self.res:
                    return True
        return False
    
    def dfs(self, board, word, row, col, start):
        # if we've found the word, we can directly return
        if self.res:
            return 
        # If we've matched the keyword, we can return 
        if start == len(word):
            self.res = True
            return 
        # If we've gone beyond the border, we need to return 
        if row < 0 or col < 0 or row >= self.m or col >= self.n:
            return 
        if board[row][col] != word[start]:
            return 
        # If we can be here, that means the index p is the letter we're looking
        temp = board[row][col]
        board[row][col] = "#"
        self.dfs(board, word, row + 1, col, start + 1)
        self.dfs(board, word, row - 1, col, start + 1)
        self.dfs(board, word, row, col + 1, start + 1)
        self.dfs(board, word, row, col - 1, start + 1)
        board[row][col] = temp

