"""
368. Largest Divisible Subset

Given a set of distinct positive integers nums, return the largest subset of nums
such that every pair (nums[i], nums[j]) of elements in the subset satisfies:

nums[i] % nums[j] == 0, or
nums[j] % nums[i] == 0

If there are multiple solutions, return any of them.

Input: nums = [1,2,3]
Output: [1,2]
Explanation: [1,3] is also accepted.
"""
from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [[num] for num in nums]
        for i in range(1, n):
            maxSubLen = 1
            subIndex = -1
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[j]) >= maxSubLen:
                    maxSubLen = len(dp[j])
                    subIndex = j
            if subIndex != -1:
                dp[i] = dp[subIndex] + [nums[i]] # It's subIndex, not j.
        dp.sort(key=lambda x: -len(x))
        return dp[0]