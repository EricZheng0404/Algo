"""
LeetCode 16: 3Sum Closest
This is a two-pointer problem.

The goal is to find the closest sum of three numbers to the target.
"""
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        delta = float('inf')
        for i in range(len(nums) - 2):
            sum_ = nums[i] + self.twoSumClosest(i + 1, nums, target - nums[i])
            if abs(delta) > abs(target - sum_):
                delta = target - sum_
            # This could optimize the algorith,
            # If delta is 0, that means we've found the target already.
            # There's no need to continue the loop.
            # So we can break the loop and return immediately.
            if delta == 0:
                break
        return target - delta
    
    def twoSumClosest(self, start, nums, target):
        l, r = start, len(nums) - 1
        delta = float('inf')
        while l < r:
            sum_ = nums[l] + nums[r]
            if abs(delta) > abs(target - sum_):
                delta = target - sum_
            # This could optimize the algorithm,
            # If delta is 0, that means we've found the target already.
            # There's no need to continue the loop.
            # So we can break the loop and return immediately.
            if delta == 0:
                break
            if sum_ > target:
                r -= 1
            # The reason why we want to continue 
            elif sum_ < target:
                l += 1
        return target - delta