"""
LeetCode 47

Given a collection of numbers nums, that might contain duplicates, return all
possible permutations in any order
"""
from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.n = len(nums)
        self.res = []
        self.path = []
        nums.sort()
        self.visited = [False] * self.n
        self.backtrack(nums)
        return self.res

    def backtrack(self, nums):
        print(self.path)
        print(self.visited)
        print()

        if len(self.path) == self.n:
            self.res.append(self.path[:])
            
        for i in range(self.n):
            # If visited is True, meaning it has been visited, we continue
            if self.visited[i] is True:
                continue
            if i != 0 and nums[i - 1] == nums[i] and not self.visited[i - 1]:
                continue
            self.visited[i] = True
            self.path.append(nums[i])
            self.backtrack(nums)
            self.visited[i] = False
            self.path.pop()
            
sol = Solution()
sol.permuteUnique([1, 1, 2])