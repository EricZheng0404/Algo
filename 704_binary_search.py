class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # Focus! 5/16/2025

        # We're using len(nums) - 1 for r is because len(nums) is out the bound of the possible search index
        l, r = 0, len(nums) - 1 
        # We're using l <= r, meaning [l, r] is the search range.
        # The termination condition is [r+1, r], meaning there's no elements in the search range.
        # [l, l] is still searchable, because there's still one element in the search range
        while l <= r:
            mid = l + ((r - l) // 2) # In case of integer overflow
            if nums[mid] == target:
                return mid
            elif nums[mid] > target: # The target is in the left range
                r = mid - 1 # We decrement by 1 because we've already searched mid just before
            elif nums[mid] < target:
                l = mid + 1 # We should push l pointer to the mid + 1, not mid - 1
        return -1
            