"""
LeetCode 986. Interval List Intersections
"""

from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i, j = 0, 0
        res = []
        while i < len(firstList) and j < len(secondList):
            a1, a2 = firstList[i][0], firstList[i][1]
            b1, b2 = secondList[j][0], secondList[j][1]
            # If there's an intersection: 
            if a2 >= b1 and b2 >= a1:
                res.append([max(a1, b1), min(a2, b2)])
            # If the end of the list2 exceed list1, we should go to the next element in list1
            if b2 > a2:
                i += 1
            else:
                j += 1
        return res