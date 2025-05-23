class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        num = n
        while num % 2 == 0:
            num //= 2
        while num % 3 == 0:
            num //= 3
        while num % 5 == 0:
            num //= 5
        return num == 1
        