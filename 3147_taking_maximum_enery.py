from typing import List
class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        res = float('-inf')
        n = len(energy)
        for i in range(n - k, n):
            currSum = 0
            j = i
            while j >= 0:
                currSum += energy[j]
                res = max(res, currSum)
                j -= k
        return res