from typing import List
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        left, right = 0, 0
        window = 0
        while right < len(nums):
            num = nums[right]
            window += num
            right += 1
            while left < right and window >= target:
                # Check the min length when we're greater than or equal 
                # to the target
                res = min(res, right - left)
                leftNum = nums[left]
                window -= leftNum
                left += 1
        return res if res != float('inf') else 0