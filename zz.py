class Solution:
    def combination(self, nums, k):
        self.res = []
        self.path = []
        self.backtrack(nums, k, 0)
        return self.res
    
    def backtrack(self, nums, k, start):
        if len(self.path) == k:
            self.res.append(self.path[:])
            return 
        for i in range(start, len(nums)):
            self.path.append(nums[i])
            self.backtrack(nums, k, i + 1)
            self.path.pop()

sol = Solution()
print(sol.combination([1, 2, 3, 4], 2))