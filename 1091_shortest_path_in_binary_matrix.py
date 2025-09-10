class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if grid[0][0] == 1:
            return -1
        q = deque()
        q.append([0, 0, 1])
        while q:
            curr = q.popleft()
            if curr[0] == m - 1 and curr[1] == n - 1:
                return curr[2]
            for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]:
                newX = curr[0] + x
                newY = curr[1] + y
                if newX < 0 or newX >= m or newY < 0 or newY >= n or grid[newX][newY] != 0:
                    continue
                q.append((newX, newY, curr[2] + 1))
                grid[newX][newY] = 1
        return -1
