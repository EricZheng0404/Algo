"""
LeetCode 39. Combination Sum

Mistakes:
1. I didnt used the start parameter to control the branching. Because we need
unique combinations, we need to use the start parameter to control the branching.
The start parameter just control the order of the elements in the path. 
We always ensure to go from index from left to right, rather than maybe 2, 0, 3.
2. I was thinking using sum(self.path) along the way. However, it's not a good 
idea because that means it's O(n) for each backtrack call. On the oter hand, 
having sumPath is O(1) for each backtrack call.
"""
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.n = len(candidates)
        self.res = []
        self.path = []
        self.backtrack(candidates, target, 0, 0)
        return self.res 

    def backtrack(self, candidates, target, start, sumPath):
        if sumPath == target:
            self.res.append(self.path[:])
            return
        elif sumPath > target:
            return 
        for i in range(start, self.n):
            self.path.append(candidates[i])
            sumPath += candidates[i]
            self.backtrack(candidates, target, i, sumPath)
            self.path.pop()
            sumPath -= candidates[i]
