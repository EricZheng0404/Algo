"""
Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
"""

class Solution:
    """
    If a char has been mapped, then it can't be mapped again. 

    """
    def isIsomorphic(self, s: str, t: str) -> bool:
        lookup = {}
        used = set()
        for i in range(len(s)):
            if s[i] not in lookup:
                if t[i] in used: # If the char is already used, then it can't be mapped again.
                    return False
                lookup[s[i]] = t[i]
                used.add(t[i])
            else: # If the char is already in lookup
                if lookup[s[i]] != t[i]:
                    return False
        return True