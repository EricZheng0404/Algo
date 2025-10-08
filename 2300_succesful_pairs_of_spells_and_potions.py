import math
import bisect
from typing import List
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        potions.sort()
        for spell in spells:
            minPotion = math.ceil(success / spell)
            minIndex = bisect.bisect_left(potions, minPotion)
            if minIndex == len(potions):
                res.append(0)
            else:
                res.append(len(potions) - minIndex)

        return res