"""
Leetcode 264: Ugly Number II

An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return the nth ugly number.

Example 1:
Input: n = 10
Output: 12
Explanation: [1, 2, 3, 4, 5, 6, 8, 9, 10, 12] is the sequence of the first 10 ugly numbers.

Notes: the first ugly number is 1, since 1 is not divisible by 2, 3, or 5.


"""

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        product2, product3, product5 = 1, 1, 1
        p2, p3, p5 = 1, 1, 1
        p = 1
        res = [0] * (n + 1)
        while p <= n:
            min_val = min(product2, product3, product5)
            res[p] = min_val
            p += 1
            if min_val == product2:
                product2 = 2 * res[p2]
                p2 += 1
            if min_val == product3:
                product3 = 3 * res[p3]
                p3 += 1
            if min_val == product5:
                product5 = 5 * res[p5]
                p5 += 1
        return res[n] 