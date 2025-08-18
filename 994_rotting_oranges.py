from typing import List
from collections import deque
"""
994. Rotting Oranges
"""

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = deque()
        # We first add all existing rotten orages to the queue
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
        step = 0
        # Four directions we can go
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q:
            size = len(q)
            for _ in range(size):
                point = q.popleft()
                for dir in dirs:
                    x, y = point[0] + dir[0], point[1] + dir[1]
                    # If the new index is within range and it's a rotten orange
                    if x >= 0 and y >= 0 and x < m and y < n and grid[x][y] == 1:
                        grid[x][y] = 2
                        q.append((x, y))
            step += 1
        print(grid)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        # In the last level, 1 is also added. So, we need to subtract this one
        return step - 1 if step else 0
        