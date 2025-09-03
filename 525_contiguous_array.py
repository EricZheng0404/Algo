from typing import List
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        preSum = [0] * (n + 1)
        for i in range(1, n + 1):
            preSum[i] = preSum[i - 1] + (-1 if nums[i- 1] == 0 else 1)
        res = 0
        countIndex = {}
        for i in range(n + 1):
            # If the sum is new, we record its index in the dictionary
            if preSum[i] not in countIndex:
                countIndex[preSum[i]] = i
            # We have met the sum before already
            else:
                res = max(res, i - countIndex[preSum[i]])
        return res