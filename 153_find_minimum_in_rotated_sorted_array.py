"""
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/editorial
"""

class Solution:

    """
    The key is to find the "inflection point", AKA the cliff.

    """
    def findMin(self, nums: List[int]) -> int:
        # Forgot the edge case that there's only one number in nums
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums) - 1
        # We know that the original nums is sorted or not
        if nums[l] < nums[r]:
            return nums[l]
        while l <= r:
            mid = l + (r - l) // 2
            # Case [2, 3] with 3 being mid, so 2 is the inflection point
            if nums[mid - 1] > nums[mid]:
                return nums[mid]
            # Case [2, 1] with 2 being mid, so 1 is the inflection point
            if nums[mid + 1] < nums[mid]:
                return nums[mid + 1]
            if nums[mid] > nums[l]:
                l = mid + 1
            else: 
                r = mid - 1
        return nums[l]