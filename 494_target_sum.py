from functools import lru_cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        @lru_cache(None)
        def backtrack(i, currSum):
            if i == len(nums):
                return 1 if currSum == target else 0
            return backtrack(i + 1, currSum + nums[i]) + backtrack(i + 1, currSum - nums[i])
        return backtrack(0, 0)
            