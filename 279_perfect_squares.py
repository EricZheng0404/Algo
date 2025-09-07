class Solution:
    def numSquares(self, n: int) -> int:
        # definition: the minimum number of perfect squares that sum to i is dp[i]
        dp = [float('inf')] * (n + 1)
        # base case
        dp[0] = 0
        # state transition equation
        for i in range(1, n + 1):
            for j in range(1, int(i**0.5) + 1):
                # i - j * j can be made up to i by adding one more perfect square j * j
                dp[i] = min(dp[i], dp[i - j * j] + 1)
        return dp[n]