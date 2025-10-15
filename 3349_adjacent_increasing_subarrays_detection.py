from typing import List
class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if k == 1:
            return True
        for i in range(n):
            if i + 2 * k > n:
                break
            valid = True
            for j in range(k - 1):
                if nums[i + j] >= nums[i + j + 1]:
                    valid = False
                    break
                for m in range(k - 1):
                    if nums[i + k + m] >= nums[i + k + m + 1]:
                        valid = False
                        break
                if valid is False:
                    break
            if valid is True:
                return True
        return False
            