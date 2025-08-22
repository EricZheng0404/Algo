from typing import List
"""
1219. Path with Maximum Gold
"""
class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        self.res = 0
        self.m = len(grid)
        self.n = len(grid[0])
        for row in range(self.m):
            for col in range(self.n):
                # WE can only start from non-0 mine
                if grid[row][col] != 0:
                    # We initialize a new gold for each path
                    self.gold = 0
                    # Let the dfs function do all the iteration
                    self.dfs(grid, row, col)
        return self.res

    def dfs(self, grid, row, col):
        if row < 0 or col < 0 or row >= self.m or col >= self.n:
            return 
        if grid[row][col] == 0:
            return 
        # Pre-order position: We record the temp and add it to the self.gold value
        temp = grid[row][col]
        self.gold += temp
        # Every time we add new gold the sum, we check if it's greater than the 
        # sum we got before
        self.res = max(self.res, self.gold)
        grid[row][col] = 0
        self.dfs(grid, row + 1, col)
        self.dfs(grid, row - 1, col)
        self.dfs(grid, row, col + 1)
        self.dfs(grid, row, col - 1)
        # Post-order position: we give it back
        grid[row][col] = temp
        # I forgot to subtract the value
        self.gold -= temp