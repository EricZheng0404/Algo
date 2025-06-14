"""
LeetCode 13. Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D, and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

"""

class Solution:
    def romanToInt(self, s: str) -> int:
        lookupTable = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        i = 0
        res = 0
        n = len(s)
        while i < n:
            if i < n - 1 and lookupTable[s[i]] < lookupTable[s[i + 1]]:
                res += (lookupTable[s[i + 1]] - lookupTable[s[i]])
                i += 2
            else:
                res += lookupTable[s[i]]
                i += 1
        return res