from typing import List
"""
Mistakes:
1. I made the mistake of returning 0 insteasd of "0".
"""
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(num) for num in nums]
        nums.sort(key = lambda x: x * 10, reverse = True)
        # When all the numbers are 0, return "0"
        if nums[0] == "0":
            return "0"
        return "".join(nums)