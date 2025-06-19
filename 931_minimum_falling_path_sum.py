"""
931. Minimum Falling Path Sum
Given an n x n integer matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

Example 1:
Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum as shown.
"""

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        self.n = len(matrix) # matrix is a square
        self.memo = [[float("inf")] * self.n for _ in range(self.n)]
        res = float("inf")
        for i in range(self.n):
            res = min(res, self.dp(matrix, self.n - 1, i))
        return res

    def dp(self, matrix, row, col):
        # Out of range, we just return something unreasonable
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
