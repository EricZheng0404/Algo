class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        self.m = len(obstacleGrid)
        self.n = len(obstacleGrid[0])
        self.memo = [[-1] * self.n for _ in range(self.m)]
        # Edge case: The start or the end is an obstacle
        if obstacleGrid[0][0] == 1 or obstacleGrid[self.m - 1][self.n - 1] == 1:
            return 0
        return self.dp(obstacleGrid, self.m - 1, self.n - 1)

    def dp(self, obstacleGrid, m, n):
        # Base case
        if m == 0 and n == 0:
            return 1
        # Boundary case
        if m < 0 or n < 0 or m >= self.m or n >= self.n or obstacleGrid[m][n] == 1:
            return 0
        if self.memo[m][n] != -1:
            return self.memo[m][n]
        self.memo[m][n] = self.dp(obstacleGrid, m - 1, n) + self.dp(obstacleGrid, m, n - 1)
        return self.memo[m][n]
        

