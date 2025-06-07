"""
LeetCode 78. Subsets

Question I have: I don't know how to handle the case when the length of the
subset is 0.
"""
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.path = []
        self.backtrack(nums, 0)
        return self.res
    
    def backtrack(self, nums, start):
        print(f"path is {self.path}")
        #Pre-order position: we add the path as long as 
        self.res.append(list(self.path))
        for i in range(start, len(nums)):
            self.path.append(nums[i])
            self.backtrack(nums, i + 1)
            self.path.pop()

if __name__ == "__main__":
    sol = Solution()
    sol.subsets([1, 2, 3])