from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        l, r = 0, 0
        window = {}
        maxLen = 0
        while r < len(nums):
            rightNum = nums[r]
            window[rightNum] = window.get(rightNum, 0) + 1
            r += 1

            while window.get(0, 0) > 1: # It should be while in here because we need possibly to remove multiple elements
                leftNum = nums[l]
                window[leftNum] -= 1
                l += 1
            maxLen = max(maxLen, r - l)
        return maxLen