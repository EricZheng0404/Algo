"""
Leetcode 54: Spiral Matrix
"""
from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        upper, lower = 0, m - 1
        left, right = 0, n - 1
        res = []
        sz = m * n
        while len(res) < sz:
            # = means we still have more row
            # upper from left to right
            if upper <= lower:
                for i in range(left, right + 1):
                    res.append(matrix[upper][i])
                upper += 1
            # right from top to bottom
            if left <= right:
                for i in range(upper, lower + 1):
                    res.append(matrix[i][right])
                right -= 1
            # bottom from right to left
            if upper <= lower:
                for i in range(right, left - 1, -1):
                    res.append(matrix[lower][i])
                lower -= 1
            # left from bottom to top
            if left <= right:
                for i in range(lower, upper - 1, -1):
                    res.append(matrix[i][left])
                left += 1
        return res