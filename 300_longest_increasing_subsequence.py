"""
300. Longest Increasing Subsequence

Given an integer array nums, return the length of the longest strictly increasing
subsequence.

Example 1:
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
"""
from typing import List

class Solution:
    """
    dp[i] represents the length of the longest strictly increasing subsequence ending
    with nums[i]. As long as nums[i], there'd be one definite prevNum.
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        # We need the same number of elements in the dp array
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    # We need to find the max value of all the possible dp[i],
                    # or we could run into a [0,1,0,3] problem.
                    dp[i] = max(dp[j] + 1, dp[i]) # I was confused on this line.
        return max(dp)