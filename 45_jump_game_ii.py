"""
LeetCode 45. Jump Game II

You are given a 0-indexed array of integers nums of length n. You are initially
positioned at nums[0].

Each element nums[i] represents the maximum length of a forward jump from index
i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:


Example 1:
Input: nums = [2,3,1,1,4]

This is a greedy problem. We can use a window to record the farthest index we 
can go. We can use a variable to record the number of jumps.
"""

from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        # Record the farthest index we can go in the current step window
        # As long as we are in or within the windowEnd, we don't need to jump
        # again.
        windowEnd = 0
        farthest = 0
        jumps = 0 
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if farthest == n - 1:
                return jumps + 1
            if i == windowEnd:
                windowEnd = farthest
                jumps += 1
        return jumps