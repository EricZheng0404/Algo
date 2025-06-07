class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.path = []
        self.backtracking(nums, 0)
        return self.res
    
    def backtracking(self, nums, start):
        #Pre-order position: we add the path as long as 
        self.res.append(list(self.path))
        for i in range(start, len(nums)):
            self.path.append(nums[i])
            self.backtracking(nums, i + 1)
            self.path.pop()