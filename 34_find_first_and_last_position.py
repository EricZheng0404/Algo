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
    
class Solution2:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        return [self.findLeftRange(nums, target), self.findRightRange(nums, target)]

    def findLeftRange(self, nums, target):
        l, r = 0, len(nums)
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                r = mid
            # The case where the target is in the left
            elif nums[mid] > target: 
                r = mid
            else:
                l = mid + 1
        if l < 0 or l >= len(nums):
            return -1
        return l if nums[l] == target else -1
    
    def findRightRange(self, nums, target):
        l, r = 0, len(nums)
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid
            else:
                l = mid + 1
        if l - 1 < 0 or l - 1>= len(nums):
            return -1
        return l - 1 if nums[l - 1] == target else -1 




        