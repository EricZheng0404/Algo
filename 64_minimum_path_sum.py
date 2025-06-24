"""
Leetcode 64: Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
"""
from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        if self.m == 1 and self.n == 1:
            return grid[0][0]
        self.memo = [[-1] * self.n for _ in range(self.m)]
        return self.dp(grid, self.m - 1, self.n - 1)
    
    def dp(self, grid, row, col):
        # Base case
        if row == 0 and col == 0:
            return grid[0][0]
        # Out of range
        if row < 0 or col < 0 or row >= self.m or col >= self.n:
            return float("inf")
        if self.memo[row][col] != -1: # I put self.memo in here
            return self.memo[row][col] # I put self.memo in here
        self.memo[row][col] = min(self.dp(grid, row - 1, col), self.dp(grid, row, col - 1)) + grid[row][col]
        return self.memo[row][col]