"""
931. Minimum Falling Path Sum
Given an n x n integer matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

Example 1:
Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.
"""
from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        self.n = len(matrix) # matrix is a square
        self.memo = [[float("inf")] * self.n for _ in range(self.n)]
        res = float("inf")
        for i in range(self.n):
            res = min(res, self.dp(matrix, self.n - 1, i))
        return res

    def dp(self, matrix, row, col):
        # This condition needs to be before row == 0 check
        # Because row == 0 but col could be out of range.
        if row < 0 or col < 0 or row >= self.n or col >= self.n:
            return 9999 # Because this is a recursion, this has to return something.
        # If the result is in the memo
        if self.memo[row][col] != float("inf"):
            return self.memo[row][col]
        # Base case
        if row == 0:
            return matrix[0][col]
        # Get into dp
        self.memo[row][col] = min(self.dp(matrix, row - 1, col), self.dp(matrix, row - 1, col - 1), self.dp(matrix, row - 1, col + 1)) + matrix[row][col]
        return self.memo[row][col]

class Solution2:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        # We set up a (m + 1) * (n + 1) matrix to avoid boundary check.
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0
        dp[1][1] = 1
        for row in range(1, m + 1):
            for col in range(1, n + 1):
                if row == 1 and col == 1:
                    continue
                # I forgot to add this condition.
                # If the current cell is an obstacle, we don't need to calculate
                # the number of paths.
                if obstacleGrid[row - 1][col - 1]:
                    continue
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]
        return dp[m][n] 