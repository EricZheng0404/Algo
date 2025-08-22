class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Memoization
        self.memo = [[0] * n for _ in range(m)] 
        # We want to know the number of path at the index (m - 1, n - 1)
        return self.dp(m - 1, n - 1)
    
    def dp(self, row, col):
        # Base case: when we're at the origin
        if row == 0 and col == 0:
            return 1
        # When it's out of range, there's zero way
        if row < 0 or col < 0:
            return 0
        if self.memo[row][col] > 0:
            return self.memo[row][col]
        # I forgot to put the result in the memo
        self.memo[row][col] = self.dp(row - 1, col) + self.dp(row, col - 1)
        return self.memo[row][col]