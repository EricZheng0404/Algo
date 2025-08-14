from typing import List
from collections import deque
"""
994. Rotting Oranges
"""
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
        dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        steps = 0
        while q:
            size = len(q)
            for _ in range(size):
                curr = q.popleft()
                for dir in dirs:
                    x, y = curr[0] + dir[0], curr[1] + dir[1]
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        grid[x][y] = 2
                        q.append((x, y))
            steps += 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return steps - 1 if steps else 0