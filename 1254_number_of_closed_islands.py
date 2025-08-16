from typing import List
"""
1254. Number of Closed Islands

Closed island is an island that is completely surrounded by 1s.
So we need to flood the edges of the grid with 1s.
Then we can count the number of islands that are completely surrounded by 1s.
"""
class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            # To flood the left edge 
            self.dfs(grid, i, 0)
            # To flood the right edge
            self.dfs(grid, i, n - 1)
        for j in range(n):
            # To flood the upper edge
            self.dfs(grid, 0, j)
            # To flood the bottom edge
            self.dfs(grid, m - 1, j)
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    res += 1
                    self.dfs(grid, i, j)
        return res
    
    def dfs(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        if i < 0 or j < 0 or i >= m or j >= n:
            return 
        if grid[i][j] == 1:
            return 
        grid[i][j] = 1
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j + 1)
        self.dfs(grid, i, j - 1)