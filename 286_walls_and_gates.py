from typing import List
from collections import deque
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m = len(rooms)
        n = len(rooms[0])
        q = deque()
        for row in range(m):
            for col in range(n):
                if rooms[row][col] == 0:
                    q.append((row, col, 0))
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        while q:
            curr = q.popleft()
            for dir in dirs:
                newRow = curr[0] + dir[0]
                newCol = curr[1] + dir[1]
                # We only want to put empty room in
                if newRow < 0 or newCol < 0 or newRow >= m or newCol >= n or rooms[newRow][newCol] != 2147483647:
                    continue
                rooms[newRow][newCol] = curr[2] + 1
                q.append((newRow, newCol, curr[2] + 1))