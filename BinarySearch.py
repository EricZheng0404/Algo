"""
Function to the find the index of the first occurence of an element

Input:
    - A list of sorted numbers
    - A target number
NOTE:
If the target can't be found, then we return the least element that's greater 
than the target


The reason why we can find the left bound is in:
if nums[mid] == target:
    r = mid
This means even if we find the target, we continue to push the search range to
the left
"""

class BinarySearch:
    # left bound Implementation 1: [left, right)
    def leftBound(self, nums, target):
        l, r = 0, len(nums)
        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                r = mid 
            elif nums[mid] > target:
                r = mid 
            elif nums[mid] < target:
                l = mid + 1
        return l
    
    # left bound implementation 2: [left, right]
    def leftBound2(self, nums, target):
        l, r = 0, len(nums)
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
        if nums[l] == len(nums) - 1:
            return -1
        return l if nums[l] == target else -1
    
    def leftBound2(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] >= target:
                r = mid - 1
            else:
                l = mid + 1
        # if l < 0 or l >= len(nums):
        #     return -1
        # return l if nums[l] == target else -1
        return l
    

    def rightBound(self, nums, target):
        l, r = 0, len(nums)
        while l < r:
            mid = l + (r - l) // 2
            # NOTE
            if nums[mid] == target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid 
            # NOTE
            else: 
                l = mid + 1
        # NOTE
        return l - 1


    def rightBound2(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] > target:
                r = mid - 1
            else: 
                l = mid + 1
        """
        If the target is not found, the index of the greatest number that's less
        than the target is returned.
        If the target is less than all the numbers, -1 is returned. That's why 
        we need range check
        """
        if r < 0 or r >= len(nums):
            return -1
        return r if nums[r] == target else -1

nums = [1, 1, 1, 5, 7]
target = 8
b = BinarySearch()
print(b.leftBound2(nums, target))
# print(b.rightBound2(nums, 10))
