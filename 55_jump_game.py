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

class Solution2:
    # main function
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        # initialize memo to n, which is equivalent to INT_MAX
        # because from 0 to n - 1 at most n - 1 steps
        memo = [n] * n

        return self.dp(nums, 0, memo)
    
    # definition: at least dp(nums, p) steps are needed to jump from index p to the last cell
    def dp(self, nums: List[int], p: int, memo: List[int]) -> int:
        n = len(nums)
        # base case
        if p >= n - 1:
            return 0
        # the subproblem has been calculated
        if memo[p] != n:
            return memo[p]
        steps = nums[p]
        # you can choose to jump 1 step, 2 steps...
        for i in range(1, steps + 1):
            # enumerate every choice
            # calculate the result of each subproblem
            subProblem = self.dp(nums, p + i, memo)
            # take the smallest as the final result
            memo[p] = min(memo[p], subProblem + 1)
        return memo[p]