"""
Leetcode 198: House Robber
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
"""

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        self.memo = [-1] * len(nums)
        return self.dp(nums, 0)

    def dp(self, nums, start):
        if start >= len(nums):
            return 0
        if self.memo[start] != -1:
            return self.memo[start]
        self.memo[start] = max(nums[start] + self.dp(nums, start + 2), self.dp(nums, start + 1))
        return self.memo[start]