from typing import List
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        s = []
        for i in range(n * 2 - 1, -1, -1):
            while s and s[-1] <= nums[i % n]:
                s.pop()
            res[i % n] = -1 if not s else s[-1]
            s.append(nums[i % n])
        return res