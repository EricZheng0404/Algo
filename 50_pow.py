class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Base case
        if n == 0:
            return 1
        # if n < 0
        if n < 0:
            return 1.0/self.myPow(x, -n)
        if n % 2 == 1:
            return x * self.myPow(x, n - 1)
        else:
            sub = self.myPow(x, n / 2)
            return sub * sub