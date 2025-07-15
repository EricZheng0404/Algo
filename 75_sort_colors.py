"""
LeetCode 75. Sort Colors

Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.
"""

from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.

        Three pointers:
        p0: the index of the next number 0, range [0, p0)
        p2: the index of the next number 2, range (p2, len(nums) - 1]
        p: to iterate through the next number
        """
        p, p0 = 0, 0
        p2 = len(nums) - 1
        # because the left of p2 is open, so the number at index p2 is not processed
        while p <= p2: 
            
            if nums[p] == 0:
                self.swap(nums, p, p0)
                p0 += 1
            elif nums[p] == 2:
                self.swap(nums, p, p2)
                p2 -= 1
            # We go on the find the next number, this 1 probably will be replaced
            elif nums[p] == 1:
                p += 1
            # all the number to the left of p0 should be 0's
            if p < p0:
                p = p0
            print(nums)

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]