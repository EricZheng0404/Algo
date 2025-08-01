"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/editorial
"""
from typing import List
class Solution:
    """
    There's only cliff in the numbers, we only need to identify it.
    """ 
    def findMin(self, nums: List[int]) -> int:
        # Base cases
        # 1. If there's only one number
        n = len(nums)
        if n == 1:
            return nums[0]
        # If the list is already sorted
        l, r = 0, n - 1
        if nums[l] < nums[r]:
            return nums[l]
        while l <= r:
            mid = l + (r - l) // 2
            # [3, 2] as 2 being the middle, then 2 is the min
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            # [2, 1] as 2 being the middle, then 1 is the min
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            # If nums[mid] is greater than nums[l], that means all the numbers to the
            # left is sorted, the min must be on the right
            if nums[l] < nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        return nums[l]
                