class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # i is the pointer in s
        i = 0
        # j is the pointer is t
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            # We need a else here because we need to move the pointer in t
            else:
                j += 1
        """
        I forgot that at the end of the loop, we need to check if i == len(s)
        because after the last check, i is pushed is the next index of s.
        """
        return i == len(s)