"""
Given a positive integer n, write a function that returns the number of set bits
in its binary representation.

Bit manipulation question. 
n & (n - 1) removes the least significant 1
"""

def hammingWeight(n):
    res = 0
    while n != 0:
        n = n & (n - 1)
        res += 1
    return res