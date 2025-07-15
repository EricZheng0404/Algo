"""
LeetCode 977. Squares of a Sorted Array

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
"""

from typing import List
class Solution:
    """
    Two pointers:
    front: the pointer in the front of the nums
    back: the pointer in the back of the nums
    p: the pointer in the res
    We use two pointers to traverse the nums, and the pointer in the res to 
    store the result.
    We use two pointers to traverse the nums, and the pointer in the res to 
    store the result.

    The key is that nums are already sorted, and the larget the absolute value, 
    the larger the square.
    So we can use two pointers to traverse the nums, and the pointer in the res 
    to store the result.
    We use two pointers to traverse the nums, and the pointer in the res to 
    store the result.
    """
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        p = n - 1 # The pointer in the res
        front, back = 0, n - 1
        # while front <= back: #?
        while p >= 0:
            if abs(nums[front]) > abs(nums[back]):
                res[p] = nums[front] ** 2
                front += 1
            else:
                res[p] = nums[back] ** 2
                back -= 1
            p -= 1
        return res
        
            