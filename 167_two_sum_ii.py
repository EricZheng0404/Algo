"""
Leetcode 167: Two Sum II - Input Array Is Sorted
This is a two pointer problem.
"""
from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l <= r:
            result = numbers[l] + numbers[r]
            if result == target:
                return [l + 1, r + 1]
            elif result < target:
                l += 1
            else:
                r -= 1
        # Although it's mentioned that there's only one solution, we still need to 
        # return [-1, -1] as fallback.
        return [-1, -1]