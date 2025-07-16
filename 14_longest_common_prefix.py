"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
"""
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        if not strs[0]:
            return res
        m = len(strs[0]) # col
        n = len(strs) # row
        if n == 1:
            return strs[0]
        
        for col in range(m):
            char = strs[0][col]
            for row in range(1, n):
                # When the length of a word is n, then we should break when i >= n
                # Length check should be done before the char check
                if col >= len(strs[row]) or char != strs[row][col]:
                    return strs[0][:col]
                    # return strs[row][:col] # We should return [:col] here because it's [left, right)
        return strs[0]

        