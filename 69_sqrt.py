class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        l, r = 1, x
        while l <= r:
            mid = l + (r - l) // 2
            # We should save pivot as a variable, it saves so much runtime.
            pivot = mid * mid
            if pivot == x:
                return mid
            elif pivot > x:
                r = mid - 1
            elif pivot < x:
                l = mid + 1
        return l - 1
        