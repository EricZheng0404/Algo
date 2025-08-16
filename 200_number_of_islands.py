from typing import List
"""
200. Number of Islands

The number in the grid is string "1" or "0", not int.
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        res = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == "1":
                    res += 1
                    self.dfs(grid, i, j)
                    print(grid)
        return res

    def dfs(self, grid, row, col):
        # Always check the index first
        if row < 0 or col < 0 or row >= self.m or col >= self.n:
            return 
        if grid[row][col] == "0":
            return 
        grid[row][col] = "0"
        self.dfs(grid, row + 1, col)
        self.dfs(grid, row - 1, col)
        self.dfs(grid, row, col + 1)
        self.dfs(grid, row, col - 1)
