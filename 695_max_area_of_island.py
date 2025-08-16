from typing import List
"""
695. Max Area of Island
"""
class Solution1:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        maxArea = 0
        for row in range(self.m):
            for col in range(self.n):
                # If we find a land
                if grid[row][col] == 1:
                    # Initiate a self.are to 0
                    self.area = 0
                    self.dfs(grid, row, col)
                    maxArea = max(maxArea, self.area)
        return maxArea
    
    def dfs(self, grid, row, col):
        if row < 0 or col < 0 or row >= self.m or col >= self.n:
            return 
        if grid[row][col] == 0:
            return 
        self.area += 1
        grid[row][col] = 0
        self.dfs(grid, row + 1, col)
        self.dfs(grid, row - 1, col)
        self.dfs(grid, row, col + 1)
        self.dfs(grid, row, col - 1)

class Solution2:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        maxArea = 0
        for row in range(self.m):
            for col in range(self.n):
                # If we find a land
                if grid[row][col] == 1:
                    maxArea = max(maxArea, self.dfs(grid, row, col))
        return maxArea
    
    # dfs function is a function that returns the area of the island
    def dfs(self, grid, row, col):
        if row < 0 or col < 0 or row >= self.m or col >= self.n:
            return 0
        if grid[row][col] == 0:
            return 0
        grid[row][col] = 0
        upper = self.dfs(grid, row + 1, col)
        lower = self.dfs(grid, row - 1, col) 
        right = self.dfs(grid, row, col + 1)
        left = self.dfs(grid, row, col - 1)
        return 1 + upper + lower+ right + left
