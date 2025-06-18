class Solution:
    def climbStairs(self, n: int) -> int:
        self.memo = [0] * (n + 1)
        return self.dp(n)

    def dp(self, n):
        if n <= 2:
            return n
        if self.memo[n] != 0:
            return self.memo[n]
        # The number of ways to climb to the nth step is the sum of the 
        # number of ways to climb to the (n-1)th step and the number of ways 
        # to climb to the (n-2)th step.
        self.memo[n] = self.dp(n - 1) + self.dp(n - 2)
        return self.memo[n]
    
for i in range(0):
    print(i)