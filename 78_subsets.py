"""
LeetCode 78. Subsets

Mistakes:
1. In line 31, I used start + 1 instead of i + 1.

1. We use start to control the branching. Because there's a limited number of 
elements in the nums list, we can just use range and start.
2. We add the path to the result in the pre-order position because we want to 
add the empty subset first.

"""
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.path = []
        self.backtrack(nums, 0)
        return self.res 
    
    # Parameters:
    #   - nums: a list of number in the list
    #   - start: for backtracking branching
    def backtrack(self, nums, start):
        # Pre-order position
        self.res.append(self.path[:])
        for i in range(start, len(nums)):
            self.path.append(nums[i])
            # It's not start cuz we want to further the branching
            self.backtrack(nums, i + 1) 
            self.path.pop()