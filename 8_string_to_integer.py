"""
LeetCode 8. String to Integer (atoi)
"""

class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        sign = 1
        n = len(s)
        i = 0

        # skip the leading spaces
        while i < n and s[i] == ' ':
            i += 1
        if i == n:
            return 0
        
        # know the sign
        if i < n and s[i] == '-':
            sign = -1
            i += 1
        elif i < n and s[i] == '+':
            i += 1
        if i == n:
            return 0
        # calculate the number, we dont't advance if anything other than numbers
        while i < n and '0' <= s[i] <= '9':
            res = res * 10 + (ord(s[i]) - ord('0'))
            # During the calculation, we need to check if the result is out of 
            # the range of 32-bit signed integer.
            # If it is, we return the maximum or minimum value of 32-bit signed 
            # integer.
            if sign == 1 and res > 2**31 - 1:
                return 2**31 - 1
            elif sign == - 1 and res > 2**31:
                return -2**31
            i += 1
        
        return int(res) * sign