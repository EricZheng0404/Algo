"""
Leetcode 122: Best Time to Buy and Sell Stock II
"""
from typing import List

class Solution:
    """
    Implementation 1: Top-down recursive dynamic programming
    """
    def maxProfit1(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProfit = 0
        for i in range(1, len(prices)):
            profit = prices[i] - minPrice
            maxProfit = max(maxProfit, profit)
            minPrice = min(prices[i], minPrice)
        return maxProfit