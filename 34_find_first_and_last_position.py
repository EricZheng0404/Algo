class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return[self.leftBound2(nums, target), self.rightBound2(nums, target)]
        
    
    def leftBound2(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
        if l < 0 or l >= len(nums):
            return -1
        return l if nums[l] == target else -1

    def rightBound2(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] > target:
                r = mid - 1
            else: 
                l = mid + 1
        if r < 0 or r >= len(nums):
            return -1
        return r if nums[r] == target else -1


        