from typing import List
from functools import lru_cache
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        maxArea = 0
        n = len(points)

        @lru_cache(None)
        def distance(ax, ay, bx, by):
            return ((ax - bx)**2 + (ay - by)**2)**0.5

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    a = distance(*points[i], *points[j])
                    b = distance(*points[j], *points[k])
                    c = distance(*points[k], *points[i])
                    if not self.validTriangle(a, b, c):
                        continue
                    # se is the semi-parameter
                    se = (a + b + c) / 2
                    area = (se * (se - a) * (se - b) * (se - c)) ** 0.5
                    maxArea = max(maxArea, area)
        return maxArea

    def validTriangle(self, a, b, c):
        return a + b > c and a + c > b and b + c > a