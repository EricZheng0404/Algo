"""
2161. Partition Array According to Given Pivot
"""

from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        lessList = []
        pivotList = []
        greatList = []
        for num in nums:
            if num < pivot:
                lessList.append(num)
            elif num == pivot:
                pivotList.append(num)
            else:
                greatList.append(num)
        return lessList + pivotList + greatList