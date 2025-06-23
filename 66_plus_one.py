"""
66. Plus One

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
"""
from typing import List

class Solution:
    
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        ndigits = digits[:]
        for i in range(len(ndigits) - 1, -1, -1):
            if carry == 0:
                break
            number = carry + ndigits[i]
            carry = number // 10
            ndigits[i] = number % 10
        # If the carry is not 0, it means the number is like 999, 
        # and we need to add a 1 at the front.
        if carry != 0:
            ndigits.insert(0, carry)
        return ndigits
