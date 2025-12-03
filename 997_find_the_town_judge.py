class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) < n - 1:
            return -1
        points = [0] * (n + 1)
        for x, y in trust:
            points[x] -= 1
            points[y] += 1
        for i, point in enumerate(points[1:], 1):
            if point == n - 1:
                return i 
        return -1