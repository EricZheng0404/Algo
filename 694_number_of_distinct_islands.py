from typing import List
"""
694. Number of Distinct Islands

The key is to serialize the island: as we traverse the island, we can record the
direction we've taken. If the dirs in the island are the same, then the islands 
are the same.
"""
class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        res = set()
        for row in range(self.m):
            for col in range(self.n):
                # If we've found an island
                if grid[row][col] == 1:
                    # We can only use list because string is immutable
                    island = []
                    # The initial dir doesn't matter.
                    # This just means we've found an island.
                    self.dfs(grid, row, col, island, 0)
                    res.add("".join(island))
        return len(res)

    def dfs(self, grid, row, col, island, dir):
        if row < 0 or col < 0 or row >= self.m or col >= self.n:
            return 
        if grid[row][col] == 0:
            return 
        grid[row][col] = 0
        island.append(str(dir))
        self.dfs(grid, row + 1, col, island, 1)
        self.dfs(grid, row - 1, col, island, 2)
        self.dfs(grid, row, col + 1, island, 3)
        self.dfs(grid, row, col - 1, island, 4)
        island.append(str(-dir))
