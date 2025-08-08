from typing import List
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.path = []
        # sort to make identical num group together
        candidates.sort()
        self.backtrack(candidates, target, 0, 0)
        return self.res 

    """
    start controls the branching
    
    """
    def backtrack(self, candidates, target, start, sumPath):
        if sumPath == target:
            self.res.append(self.path[:])
            return
        if sumPath > target:
            return
        # if start >= len(candidates):
        #     return 
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            self.path.append(candidates[i])
            sumPath += candidates[i]
            self.backtrack(candidates, target, i + 1, sumPath)
            self.path.pop()
            sumPath -= candidates[i]