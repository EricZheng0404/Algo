from typing import List
lass Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        for i in range(n):
            self.dfs(board, 0, i)
            self.dfs(board, m - 1, i)
        for i in range(m):
            self.dfs(board, i, 0)
            self.dfs(board, i, n - 1)

        for row in range(m):
            for col in range(n):
                if board[row][col] == "#":
                    board[row][col] = "O"
                elif board[row][col] == "O":
                    board[row][col] = "X"
        
    def dfs(self, board, row, col):
        m, n = len(board), len(board[0])
        if row < 0 or row >= m or col < 0 or col >= n:
            return
        if board[row][col] != "O":
            return
        board[row][col] = "#"
        self.dfs(board, row + 1, col)
        self.dfs(board, row - 1, col)
        self.dfs(board, row, col + 1)
        self.dfs(board, row, col - 1)
        