from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        preSum = [0] * (n + 1)
        res = 0
        index = {0: 1}
        for i in range(1, n + 1):
            # We construct the preSum list while in the loop
            preSum[i] = preSum[i - 1] + nums[i - 1]
            need = preSum[i] - k
            
            if need in index:
                res += index[need]
            # If the preSum is never met before, we initialize its value to 1, 
            # meaning we've met it once
            if preSum[i] not in index:
                index[preSum[i]] = 1
            # If we meet this preSum value one more time, we need to increment its
            # value in the map, the value means how many times we've met it before
            else:
                index[preSum[i]] = index[preSum[i]] + 1
        return res