"""
Leetcode 59: Spiral Matrix II
"""
from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # Set up the matrix first.
        # Before I was thinking about apppend
        res = [[0] * n for _ in range(n)]
        upper, lower, left, right = 0, n - 1, 0, n - 1
        num = 1
        # It has to be <=, or the last number won't go into the loop
        while num <= n ** 2:
            # 1. Upper from left to right
            if upper <= lower:
                for i in range(left, right + 1):
                    res[upper][i] = num
                    num += 1
                upper += 1
            # 2. Right from upper to lower
            if left <= right:
                for i in range(upper, lower + 1):
                    res[i][right] = num
                    num += 1
                right -= 1
            # 3. Lower from right to left
            if upper <= lower:
                for i in range(right, left - 1, -1):
                    res[lower][i] = num
                    num += 1
                lower -= 1
            # 4. Left from lower to upper
            if left <= right:
                for i in range(lower, upper - 1, -1):
                    res[i][left] = num
                    num += 1
                left += 1
        return res
