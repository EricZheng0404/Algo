"""
LeetCode 39. Combination Sum

Given a set of candidate numbers (candidates) (without duplicates) and a target
number (target), find all unique combinations in candidates where the candidate
numbers sum to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:
- All numbers (including target) will be positive integers.

Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
"""
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.n = len(candidates)
        self.res = []
        self.path = []
        self.total = 0
        self.backtrack(candidates, target, 0)
        return self.res 

    def backtrack(self, candidates, target, start):
        # Base case
        print(f"path is {self.path}")
        if self.total == target:
            self.res.append(self.path[:])
            # As long as we find a path, we should return. Because we'd the total will only be even bigger.
            # (Only positive values for candidate values)
            return
        if self.total > target:
            return 
        for i in range(start, self.n):
            self.path.append(candidates[i])
            self.total += candidates[i]
            self.backtrack(candidates, target, start)
            self.path.pop()
            self.total -= candidates[i]


sol = Solution()
print(sol.combinationSum([1, 2, 3], 5))

