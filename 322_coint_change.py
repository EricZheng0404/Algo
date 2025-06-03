from typing import List

"""
Leetcode 322: Coin Change
This is a dynamic programming problem.
"""

class Solution:
    """
    Implementation 1: Top-down recursive dynamic programming
    Time complexity: O(n * amount)
    Space complexity: O(amount)
    """
    def coinChange1(self, coins: List[int], amount: int) -> int:
        return self.dp1(coins, amount)
    def dp1(self, coins, amount):
        print(f"amount: {amount}")
        # base case
        if amount == 0: 
            return 0
        # If the amount is negative, it means we can't make up the amount.
        if amount < 0: 
            return -1

        res = float('inf')
        for coin in coins:
            # calculate the result of the subproblem. We'll use all three kinds
            # of coins and we'll have the min result because min is out of the
            # for loop.
            subProblem = self.dp1(coins, amount - coin)
            # If the subproblem has no solution, we skip this coin.
            if subProblem == -1: 
                continue
            # subproblem is the minimum number of coins to make up the amount - coin.
            # But the result is the minimum number of coins to make up the amount.
            # So, we add 1 to the subproblem to make up the amount.
            # The reason why we use min is because we want to compare all the 
            # possible choices and find the minimum one.
            res = min(res, subProblem + 1) 
        return res if res != float('inf') else -1
    

    """
    Implementation 2: Recursive with memoization.
    The memoization is the record of all the states (subproblems) that we have 
    already solved.
    """
    def coinChange2(self, coins: List[int], amount: int) -> int:
        memo = {}
        return self.dp2(coins, amount, memo)
    
    def dp2(self, coins, amount, memo):
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        if amount in memo:
            return memo[amount]
        res = float('inf')
        for coin in coins:
            subProblem = self.dp2(coins, amount - coin, memo)
            if subProblem == -1:
                continue
            res = min(res, subProblem + 1)
        # We should store amount when we finally
        memo[amount] = res if res != float('inf') else -1
        return memo[amount]
    
    """
    Implementation 3: Bottom-up iterative dynamic programming
    """
    def coinChange3(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(len(dp)):
            for coin in coins:
                if i - coin < 0:
                    continue
                # For example, when amount = 5, coins = [1, 2, 5], we're comparing
                # dp[4] + 1, dp[3] + 1, dp[0] + 1.
                dp[i] = min(dp[i], 1 + dp[i - coin])
        # If the dp[amount] is still amount + 1, it means we can't make up the
        # amount with the given coins.
        return -1 if dp[amount] == amount + 1 else dp[amount]
    


    
if __name__ == "__main__":
    sol = Solution()
    print(sol.coinChange2([1, 2, 5], 11))