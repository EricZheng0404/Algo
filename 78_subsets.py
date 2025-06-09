"""
LeetCode 78. Subsets

Question I have: I don't know how to handle the case when the length of the
subset is 0.
Answer: Whenever we enter a backtrack function, we add the path to the result. 
That's actually the last path.


"""
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.path = []
        self.backtrack(nums, 0)
        return self.res
    
    def backtrack(self, nums, start):
        #Pre-order position: we add the path as long as 
        self.res.append(list(self.path))
        # We use this to control branching, avoiding duplicates
        for i in range(start, len(nums)): 
            self.path.append(nums[i])
            self.backtrack(nums, i + 1)
            self.path.pop()

if __name__ == "__main__":
    sol = Solution()
    print(sol.subsets([1, 2, 3]))