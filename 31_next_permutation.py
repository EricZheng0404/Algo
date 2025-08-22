from typing import List
"""
31. Next Permutation
"""
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # If the list is already in descending order, the reverse it
        if nums == sorted(nums, reverse=True):
            self.reverse(nums, 0, n - 1)
            return
        for i in range(n - 1, 0, -1):
            # To find the first nums[i - 1] < nums[i] pair
            if nums[i - 1] < nums[i]:
                targetIndex = n - 1
                # From the right, find the index of the first number that's 
                # less than nums[i - 1]
                while nums[targetIndex] <= nums[i - 1]:
                    targetIndex -= 1
                # Swap these two numbers
                nums[i - 1], nums[targetIndex] = nums[targetIndex], nums[i - 1]
                # To make all the numbers to the right of i - 1 in ascending
                # order
                self.reverse(nums, i, n - 1)
                break
            
            # if foundIndex:
            #     break
                     
    
    def reverse(self, nums, l, r):
        while l <= r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1