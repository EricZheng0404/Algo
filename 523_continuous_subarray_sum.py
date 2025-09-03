from typing import List
class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        preSum = [0] * (n + 1)
        for i in range(1, n + 1):
            preSum[i] = preSum[i - 1] + nums[i - 1]
        index = {}
        for i in range(n + 1):
            val = preSum[i] % k
            # If the number is not met before
            if val not in index:
                index[val] = i
            else:
                # We need to make sure that the length is at least 2
                if i - index[val] >= 2:
                    return True
        return False