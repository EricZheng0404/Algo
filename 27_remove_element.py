"""
Leetcode 27: Remove Element
This is a two pointer problem.
"""
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow = 0
        fast = 0
        while fast < len(nums):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow # because slow is in the index of the next element to be replaced, so we don't need to `+ 1` in this case.
        