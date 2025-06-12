"""
90. Subsets II
"""

from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.n = len(nums)
        self.path = []
        self.res = []
        nums.sort()
        self.backtrack(nums, 0)
        return self.res 

    def backtrack(self, nums, start):
        # if i != start and nums[]
        self.res.append(self.path[:])
        for i in range(start, self.n):
            if i != start and nums[i - 1] == nums[i]:
                continue
            self.path.append(nums[i])
            self.backtrack(nums, i + 1) # I put `start + 1` again 
            self.path.pop()