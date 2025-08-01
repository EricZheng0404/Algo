from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
    # Forgot the edge case that there's only one number in nums
        if len(nums) == 1:
            return nums[0]
        l, r = 0, len(nums) - 1
        # We know that the original nums is sorted or not
        if nums[l] < nums[r]:
            return nums[l]
        # Before we get into the loop, we already know there're at least two numbers
        while l <= r:
            mid = l + (r - l) // 2
            # Case [2, 3] with 3 being mid, so 2 is the inflection point
            if nums[mid - 1] > nums[mid]:
                return nums[mid - 1]
            # Case [2, 1] with 2 being mid, so 1 is the inflection point
            if nums[mid + 1] < nums[mid]:
                return nums[mid]
            if nums[mid] > nums[l]:
                l = mid + 1
            else: 
                r = mid - 1
        return nums[l]

sol = Solution()
print(sol.findMin([3, 4, 5, 1, 2]))