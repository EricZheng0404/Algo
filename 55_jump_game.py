"""
LeetCode 55. Jump Game

You are given an integer array nums. You are initially positioned at the array's
first index, and each element in the array represents your maximum jump length at
that position.

Return true if you can reach the last index, or false otherwise.
We can overstep the last index, but we can't go back.
"""

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        # Record all the steps we can go on the current step
        furtheset = 0
        for i in range(n - 1):
            furtheset = max(furtheset, i + nums[i])
            if furtheset >= n - 1:
                return True
            # The furtheset step we can go at the current step is just here,
            # meaning we're stuck
            if furtheset <= i: # I was confused whther < or <=
                return False
        # Edge case: if we can't go anywhere, we return False
        return furtheset >= n - 1 

