"""
Leetcode 41: First Missing Positive
Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.
"""

from typing import List

class Solution:
    """
    1. The largest number we can have with a length of n is n. So, the game plan is we put the
    number to nums[number - 1]
    """
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]: # As long as number in the the target index is not the number
                correctIndex = nums[i] - 1
                nums[correctIndex], nums[i] = nums[i], nums[correctIndex]
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1 