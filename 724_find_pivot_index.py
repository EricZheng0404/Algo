from typing import List
"""
724. Find Pivot Index
"""

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        preSum = [0] * (n + 1)
        for i in range(1, n + 1):
            preSum[i] = preSum[i - 1] + nums[i - 1]
        # We iterate through every possible index in nums
        for i in range(0, n):
            leftSum = preSum[i] - preSum[0]
            rightSum = preSum[n] - preSum[i + 1]
            if leftSum == rightSum:
                return i
        return -1