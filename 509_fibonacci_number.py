"""
Leetcode 509: Fibonacci Number
This is a dynamic programming problem.

"""

class Solution:
    """
    Brute force recursion
    Time complexity: O(2^n)
    Space complexity: O(n)
    """
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)
    
    """
    Recursive with memoization
    Top-down approach
    Time complexity: O(n)
    Space complexity: O(n)
    """
    def fib2(self, n: int) -> int:
        # Because 0 is also included. So, we need to have n + 1 slots.
        # For example, if n = 2, we need to have [0, 1, 2]: 3 slots.
        memo = [-1] * (n + 1)
        return self.dp2(memo, n)
    def dp2(self, memo, n):
        # Base case
        if n == 0 or n == 1:
            return n
        # If the result is already computed, we can just return it.
        if memo[n] != -1:
            return memo[n]
        # If the result is not computed, we compute it and store it in the memo.
        memo[n] = self.dp2(memo, n - 1) + self.dp2(memo, n - 2)
        return memo[n]
    
    """
    Bottom-up iterative dynamic programming
    Time complexity: O(n)
    Space complexity: O(n)
    """
    def fib3(self, n: int) -> int:
        if n == 0:
            return 0 
        if n == 1:
            return 1
        memo = [-1] * (n + 1)
        memo[0] = 0
        memo[1] = 1
        return self.dp3(memo, n)
    def dp3(self, memo, n):
        if memo[n] != -1:
            return memo[n]
        memo[n] = self.dp3(memo, n - 1) + self.dp3(memo, n - 2)
        return memo[n]
    
    """
    Dynamic programming with constant space
    """
    def fib4(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        dp = [0] * (n + 1)
        dp[0] = 0 
        dp[1] = 1
        for i in range(2, len(dp)):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
    
    """
    Optimized dynamic programming with constant space
    """
    def fib5(self, n: int) -> int: 
        if n == 0 or n == 1:
                return n
        dp_0 = 0
        dp_1 = 1
        for _ in range(2, n + 1):
            dp = dp_0 + dp_1
            dp_0 = dp_1
            dp_1 = dp
        return dp_1