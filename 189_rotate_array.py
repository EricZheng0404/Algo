from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        self.reverse(nums, 0, n - 1)
        realK = k % n 
        self.reverse(nums, 0, realK - 1)
        self.reverse(nums, realK, n - 1)
    
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        