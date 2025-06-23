"""
256. Paint House

There is a row of n houses, where each house can be painted one of three colors:
red, blue, or green. The cost of painting each house with a certain color is
different. You have to paint all the houses such that no two adjacent houses have
the same color.

The cost of painting each house with a certain color is represented by a n x 3
matrix.
"""
from typing import List

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        """
        d[i][j]: the min cost to paint house i with color j
        """
        n = len(costs)
        dp = [[0] * 3 for _ in range(n)]
        for i in range(3):
            dp[0][i] = costs[0][i]
        for i in range(1, n):
            dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + costs[i][0]
            dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + costs[i][1]
            dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + costs[i][2]
        last = dp[-1]
        return min(last[0], last[1], last[2])