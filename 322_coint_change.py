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
            
            # calculate the result of the subproblem
            subProblem = self.dp1(coins, amount - coin)
            # If the subproblem has no solution, we skip this coin.
            if subProblem == -1: 
                continue
            # subproblem is the minimum number of coins to make up the amount - coin.
            # But the result is the minimum number of coins to make up the amount.
            # So, we add 1 to the subproblem to make up the amount.
            res = min(res, subProblem + 1) 
        return res if res != float('inf') else -1
    

    """
    Implementation 2: Recursive with memoization.
    The memoization is the record of all the states (subproblems) that we have already solved.
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
        memo[amount] = res if res != float('inf') else -1
        return memo[amount]

    
if __name__ == "__main__":
    sol = Solution()
    print(sol.coinChange2([1, 2, 5], 11))