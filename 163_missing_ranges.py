from typing import List
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        if not nums:
            return [[lower, upper]]
        res = []
        for i in range(len(nums) - 1):
            num1 = nums[i]
            num2 = nums[i + 1]
            if num2 - num1 == 1:
                continue
            res.append([num1 + 1, num2 - 1])
        if nums[0] != lower:
            res.insert(0, [lower, nums[0] - 1])
        if nums[-1] != upper:
            res.append([nums[-1] + 1, upper])
        return res
            
        