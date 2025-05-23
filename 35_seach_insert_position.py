"""
LeetCode 35: Search Insert Position

Given a sorted array of distinct integers and a target value, return the index 
if the target is found. If not, return the index where it would be if it were 
inserted in order.

You must write an algorithm with O(log n) runtime complexity.

"""
class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + ((right - left) // 2)
            midNum = nums[mid]
            if midNum == target:
                return mid
            # This is a left bound problem
            elif midNum > target: # We should go to the left half
                right = mid - 1
            else: # We should go to the right half
                left = mid + 1
        return left