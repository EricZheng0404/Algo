"""
1905. Count Sub Islands

To be a sub-island, the island in grid2 must be a sub-set of the island 
in grid1.
Each piece of land in grid2 must be a piece of an establised land in grid1. 
If all the piece of land in grid2 don't form a island in grid1, then it's not 
a sub-island.

Key:
If any piece in island2 is water and land in island1, then it's not a sub-island.,
"""
from typing import List
class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        self.m = len(grid1)
        self.n = len(grid1[0])
        for row in range(self.m):
            for col in range(self.n):
                # If the piece is land in grid2 but water in grid1,
                # that means the whole land is grid1 is not a sub-island
                # in grid2. We flood it.
                if grid2[row][col] == 1 and grid1[row][col] == 0:
                    self.dfs(grid2, row, col)
        # Now all islands in grid2 are sub-islands, we can start 
        # calculating how many islands in here
        res = 0
        for row in range(self.m):
            for col in range(self.n):
                if grid2[row][col] == 1:
                    res += 1
                    self.dfs(grid2, row, col)
        return res


    def dfs(self, grid, row, col):
        # Base case: If we go out of range
        if row < 0 or col < 0 or row >= self.m or col >= self.n:
            return 
        # If the piece is water
        if grid[row][col] == 0:
            return 
        # We mark it water
        grid[row][col] = 0
        self.dfs(grid, row + 1, col)
        self.dfs(grid, row - 1, col)
        self.dfs(grid, row, col + 1)
        self.dfs(grid, row, col - 1)