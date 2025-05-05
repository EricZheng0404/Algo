class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums) - 1
        while l < r:
            if nums[l] < nums[l + 1]:
                l += 1
            else:
                return nums[l + 1]
            if nums[r] > nums[r - 1]:
                r -= 1
            else: 
                return nums[r]
        return nums[0]