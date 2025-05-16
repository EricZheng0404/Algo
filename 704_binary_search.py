"""
LeetCode 704: Binary Search

Given a sorted (in ascending order) integer array nums, and an integer target.

Find the index of target in nums. If target does not exist in nums, return -1.

"""
class Solution(object):
    def search(self, nums, target):
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
            elif midNum > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1