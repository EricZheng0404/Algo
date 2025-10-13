from typing import List
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        # dp[i][j] represent using the first i coins to get to the amount j
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        # Base case: to get to amount 0, there's only 1 way
        for i in range(n + 1):
            dp[i][0] = 1
        for i in range(1, n + 1):
            for j in range(1, amount + 1):
                if j >= coins[i - 1]:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - coins[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n][amount]