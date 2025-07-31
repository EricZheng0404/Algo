"""
Leetcode 503: Next Greater Element II
Given a circular integer array nums (i.e., the next element of the last element is the first element of the array), return the next greater number for every element in nums.

The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it does not exist, return -1 for this number.

The main idea is to use a circular array to simulate the circular nature of the array.
"""
from typing import List
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        s = []
        # We double the size of the array, creating the illusion that 
        # we have another array that is the same as the original array
        # attached to the end of the original array
        for i in range(n * 2 - 1, -1, -1):
            while s and s[-1] <= nums[i % n]:
                s.pop()
            res[i % n] = -1 if not s else s[-1]
            s.append(nums[i % n])
        return res